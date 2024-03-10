from CPCReady import common as cm
import inquirer
import os
import sys
from pprint import pprint
sys.path.append(os.path.realpath("."))
import yaml


def merge_validation(answers, current):
    """Valida que los datos sean correctos. 
       Que el nombre no este vacio y que se cumpla la
       momenclatura 8:3 si esta activada.

    Args:
        answers (_type_): _description_
        current (_type_): _description_

    Raises:
        inquirer.errors.ValidationError: _description_
        inquirer.errors.ValidationError: _description_

    Returns:
        _type_: _description_
    """
    if not current:
        raise inquirer.errors.ValidationError("", reason="bas script name cannot be empty")
    
    if cm.get83Files():
        if cm.validar_nomenclatura_8_3(current):
            return True
        else:
            raise inquirer.errors.ValidationError("", reason="Error: File name cannot be more than 8 characters.")
    return True

def merge_files_validation(answers, current):
    """Valida que los datos sean correctos.
       Que exista el fichero en scr y que el nombre no este vacio.

    Args:
        answers (_type_): _description_
        current (_type_): _description_

    Raises:
        inquirer.errors.ValidationError: _description_
        inquirer.errors.ValidationError: _description_
        inquirer.errors.ValidationError: _description_

    Returns:
        _type_: _description_
    """
    
    if not current:
        raise inquirer.errors.ValidationError("", reason="bas script name cannot be empty")
    
    FILE = cm.PATH_SRC + "/" + cm.getFileExt(current)
    if not os.path.exists(FILE):
        raise inquirer.errors.ValidationError("", reason="Bas script not exist in src")
    
    if cm.get83Files():
        if cm.validar_nomenclatura_8_3(current):
            return True
        else:
            raise inquirer.errors.ValidationError("", reason="Error: File name cannot be more than 8 characters.")
    return True

# def buscar_en_metadata(archivo_a_buscar, ruta_archivo_yaml):
#     with open(ruta_archivo_yaml, 'r') as archivo_yaml:
#         contenido_yaml = yaml.safe_load(archivo_yaml)
#         if 'files_8_3' in contenido_yaml['metadata'] and 'merge' in contenido_yaml['metadata']:
#             merge_metadata = contenido_yaml['metadata']['merge']
#             if 'files_to_merge' in merge_metadata:
#                 if archivo_a_buscar in merge_metadata['files_to_merge']:
#                     return True

#     return False


def merge():
    """
    Añade fichero para mergerar al proyecto
    
    return 
    """
    print()
    cm.showInfoTask(f"Add BAS to merge...")
    questions = [
        inquirer.Text("merge_file", message="File where it is merged?", default=cm.getMergeDestinationFile(), validate=merge_validation),
    ]

    answers = inquirer.prompt(questions)
    cm.modifyMergeDestinationFile(answers.get("merge_file"))

    project = cm.readProyect()
    while True:
        questions = [
            inquirer.Confirm("file_to_add", message="Desea añadir fichero a mergar?", default=True),
        ]

        answers = inquirer.prompt(questions)

        if not answers.get("file_to_add"):
            break
        questions = [
            inquirer.Text("file_to_add_name", message="File name?", validate=merge_files_validation),
        ]

        answers = inquirer.prompt(questions)
        if not answers.get("file_to_add_name") in project['metadata']['merge']['files_to_merge']:
            project['metadata']['merge']['files_to_merge'].append(answers.get("file_to_add_name"))

    with open(cm.CFG_PROJECT, 'w') as file:
        yaml.dump(project, file, default_flow_style=False)
    
    cm.showFoodDataProject("Configurations added to the project", 0)


