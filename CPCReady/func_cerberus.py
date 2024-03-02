import cerberus
import yaml
import re


# Definicion esquema de validacion

# def es_direccion_ip(value, field, error):
#     # Patrón para validar una dirección IP
#     patron_ip = re.compile(r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])){3}$')
    
#     if not patron_ip.match(value):
#         error(field, f"'{value}' no es una dirección IP válida.")



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
            'emulators': {
                'type': 'dict',
                'nullable': True,
                'valueschema': {
                    'type': 'dict',
                    'schema': {
                        'model': {'type': 'integer', 'allowed': [464, 6128, 664]},
                        'run': {'type': 'string'},
                        'ip': {'type': 'string', 'nullable': True}
                    }
                }
            },
            'cdtfiles': {'type': 'list', 'nullable': True, 'schema': {'type': 'string'}}
        }
    }
}

def validar_yaml(yaml_data):
    v = cerberus.Validator(schema)
    return v.validate(yaml_data), v.errors

