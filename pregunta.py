import os
import sys
from pprint import pprint
sys.path.append(os.path.realpath("."))
import inquirer

def project_validation(answers, current):

        
    if not current:
        raise inquirer.errors.ValidationError("", reason="The project name cannot be blank.")
    
    if os.path.exists(current):
        raise inquirer.errors.ValidationError("", reason="The project name already exists in this path.")
    
    if answers and answers.get("nomenclature83") and current is not None:
        if len(current) <= 8:
            return True
        else:
            raise inquirer.errors.ValidationError("", reason="Error: Project name cannot be more than 8 characters.")
    return True
    
    
questions = [
    inquirer.Confirm("nomenclature83", message="You want to activate the nomenclature 8:3?", default=True),
    inquirer.Text("project", message="Project name?", validate=project_validation),
]

answers = inquirer.prompt(questions)

questions2 = [
    inquirer.Confirm("images", message="Do you want to add an image?", default=True),
]

answers2 = inquirer.prompt(questions2)

if answers2.get("images"):
    while True:
        questions3 = [
            inquirer.Text("project", message="Image name?"),
            inquirer.List(
                "mode",
                message="Select the image mode:",
                choices=["0", "1", "2"],
                default="0",
            ),
            inquirer.Confirm("palFile", message="Include the pal file in the disk image?", default=True)
        ]
        answers3 = inquirer.prompt(questions3)
        answers2 = inquirer.prompt(questions2)
        
        if not answers2.get("images"):
            break

        
print()
# if answers.get("continue"):
pprint(answers)
pprint(answers2)
pprint(answers3)



# import inquirer
# from inquirer.errors import EndOfInput

# answers = {}

# def validate_project_name(_, response):
#     return (
#         not response.isspace() 
#         and len(response) <= 8
#     ) if answers.get("nomenclature83") == "True" else True

# def validate_image_name(_, response):
#     return (
#         not response.isspace()
#         and len(response) <= 8
#         and response.endswith((".jpg", ".jpeg", ".png"))
#     ) if answers.get("nomenclature83") == "True" else True

# questions = [
#     inquirer.List(
#         "nomenclature83",
#         message="You want to activate the nomenclature 8:3?",
#         choices=["True", "False"],
#     ),
#     inquirer.Text(
#         "project_name",
#         message="Project name?",
#         validate=validate_project_name,
#     ),
#     inquirer.List(
#         "add_image",
#         message="Do you want to add an image to the project?",
#         choices=["Yes", "No"],
#     ),
#     inquirer.List(
#         "add_sprite",
#         message="Do you want to add an sprite image to the project?",
#         choices=["Yes", "No"],
#     ),
# ]

# while True:
#     try:
#         answers = inquirer.prompt(questions)
#     except EndOfInput:
#         break

#     if answers["add_image"] == "Yes":
#         image_questions = [
#             inquirer.Text(
#                 "image_name",
#                 message="Enter the image name:",
#                 validate=validate_image_name,
#             ),
#             inquirer.List(
#                 "image_mode",
#                 message="Enter the image mode:",
#                 choices=["0", "1", "2"],
#             ),
#             inquirer.List(
#                 "include_pal",
#                 message="Does it include Pal?",
#                 choices=["True", "False"],
#             ),
#         ]

#         while True:
#             try:
#                 image_answers = inquirer.prompt(image_questions)
#                 print("Image details:", image_answers)
#             except EndOfInput:
#                 break

#             add_more_images = inquirer.prompt(
#                 [
#                     inquirer.List(
#                         "add_more_images",
#                         message="Do you want to add more images?",
#                         choices=["Yes", "No"],
#                     )
#                 ]
#             )

#             if add_more_images["add_more_images"] == "No":
#                 break

#     if answers["add_sprite"] == "Yes":
#         sprite_questions = [
#             inquirer.Text(
#                 "sprite_name",
#                 message="Enter the sprite name:",
#                 validate=validate_image_name,
#             ),
#             inquirer.List(
#                 "image_mode",
#                 message="Enter the image mode:",
#                 choices=["0", "1", "2"],
#             ),
#             inquirer.List(
#                 "include_width",
#                 message="Width?",
#                 choices=["True", "False"],
#             ),
#             inquirer.List(
#                 "include_height",
#                 message="Height?",
#                 choices=["True", "False"],
#             ),
#         ]

#         while True:
#             try:
#                 sprite_answers = inquirer.prompt(sprite_questions)
#                 print("Image details:", sprite_answers)
#             except EndOfInput:
#                 break

#             add_more_sprites = inquirer.prompt(
#                 [
#                     inquirer.List(
#                         "add_more_sprites",
#                         message="Do you want to add more Sprites?",
#                         choices=["Yes", "No"],
#                     )
#                 ]
#             )

#             if add_more_images["add_more_sprites"] == "No":
#                 break

#     add_more_projects = inquirer.prompt(
#         [
#             inquirer.List(
#                 "add_more_projects",
#                 message="Do you want to add more projects?",
#                 choices=["Yes", "No"],
#             )
#         ]
#     )

#     if add_more_projects["add_more_projects"] == "No":
#         break
