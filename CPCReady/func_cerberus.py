import cerberus
import yaml

# Definicion esquema de validacion
schema = {
    'kind': {'type': 'string', 'allowed': ['BasicProject']},
    'apiVersion': {'type': 'string', 'allowed': ['v1']},
    'metadata': {
        'type': 'dict',
        'schema': {
            'name': {'type': 'string', 'regex': '^[^\s]+$'},
            'files_8_3': {'type': 'boolean'},
            'merge': {
                'type': 'dict',
                'schema': {
                    'destination_File': {'type': 'string', 'nullable': True},
                    'files_to_merge': {'type': 'list', 'nullable': True, 'schema': {'type': 'string'}}
                }
            }
        }
    },
    'spec': {
        'type': 'dict',
        'schema': {
            'images': {'type': 'dict', 'nullable': True, 'valueschema': {'type': 'dict', 'schema': {'mode': {'type': 'integer'}, 'include_pal': {'type': 'boolean'}}}},
            'sprites': {'type': 'dict', 'nullable': True, 'valueschema': {'type': 'dict', 'schema': {'mode': {'type': 'integer'}, 'width': {'type': 'integer'}, 'height': {'type': 'integer'}}}},
            'emulators': {'type': 'dict', 'nullable': True, 'valueschema': {'type': 'dict', 'schema': {'model': {'type': 'integer'}, 'run': {'type': 'string'}}}},
            'cdtfiles': {'type': 'list', 'nullable': True, 'schema': {'type': 'string'}}
        }
    }
}


def validar_yaml(yaml_data):
    v = cerberus.Validator(schema)
    return v.validate(yaml_data), v.errors

