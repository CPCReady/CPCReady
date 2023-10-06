import jsonschema
import yaml


def validate(file_proyect):
    schema = {
        "Version": {"type": "string"},
        "kind": {"type": "string", "allowed": ["cpc"]},
        "project": {
            "type": "dict",
            "schema": {
                "data": {
                    "type": "dict",
                    "schema": {
                        "name": {"type": "string"},
                        "author": {"type": "string"}
                    },
                    "required": True
                },
                "concatenate": {"type": ["string", "null"], "nullable": True},  # Permitir cadena o nulo
                "emulators": {
                    "type": "dict",
                    "schema": {
                        "rvm-web": {
                            "type": "dict",
                            "schema": {
                                "model": {"type": "integer", "allowed": [464, 6128, 664]},
                                "run": {"type": "string"}
                            },
                            "required": True
                        },
                        "rvm-desktop": {
                            "type": "dict",
                            "schema": {
                                "model": {"type": "integer", "allowed": [464, 6128, 664]},
                                "path": {"type": ["string", "null"], "nullable": True},  # Permitir cadena o nulo
                                "run": {"type": "string"}
                            },
                            "required": True
                        },
                        "m4board": {
                            "type": "dict",
                            "schema": {
                                "ip": {"type": "string"},
                                "run": {"type": "string"}
                            },
                            "required": True
                        }
                    },
                    "required": True
                }
            },
            "required": True
        },
        "spec": {
            "type": "dict",
            "schema": {
                "files": {
                    "type": "list",
                    "schema": {
                        "type": "dict",
                        "schema": {
                            "kind": {"type": "string"},
                            "name": {"type": "string"},
                            "concat": {"type": ["boolean"]},
                            "address": {"type": "integer"},
                            "include": {"type": "string"},
                            "mode": {"type": "integer", "allowed": [0, 1, 2]},
                            "pal": {"type": "boolean"},
                            "width": {"type": "integer"},
                            "height": {"type": "integer"}
                        },
                        "required": ["kind", "name"]
                    }
                }
            },
            "required": True
        }
    }


    try:
        with open(file_proyect, "r") as yaml_file:
            yaml_content = yaml_file.read()

        data = yaml.safe_load(yaml_content)
        jsonschema.validate(data, schema)
        print(f"{file_proyect}[green] ==> [/green]Validated structure")
        return True
    except (FileNotFoundError, yaml.YAMLError, jsonschema.exceptions.ValidationError) as e:
        print(f'Error ' + file_proyect + f' The structure is not valid: {e}')
        return False

validate("cpcready.cfg")