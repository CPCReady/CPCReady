from prompt_toolkit.shortcuts import radiolist_dialog, message_dialog, input_dialog,yes_no_dialog,button_dialog


def getSpriteWidth():
    while True:
        # Pregunta sobre el nombre del proyecto
        width_name_question = "Sprite height:"
        widthname = input_dialog(
            title="New Project",
            text=width_name_question
        ).run()

        if widthname is None:
            return
        
        try:
            # Intenta convertir la cadena a un número entero
            int(widthname)
            break 
        except ValueError:
            button_dialog(
                title="New Project",
                text='Error: el valor no es un numero.',
                buttons=[('OK', True)]).run()
    return widthname

def getSpriteHeight():
    while True:
        # Pregunta sobre el nombre del proyecto
        height_name_question = "Sprite height:"
        heightname = input_dialog(
            title="New Project",
            text=height_name_question
        ).run()

        if heightname is None:
            return
        
        try:
            # Intenta convertir la cadena a un número entero
            int(heightname)
            break 
        except ValueError:
            button_dialog(
                title="New Project",
                text='Error: el valor no es un numero.',
                buttons=[('OK', True)]).run()
    return heightname

def getSpriteName(nomenclature):
    while True:
        # Pregunta sobre el nombre del proyecto
        sprite_name_question = "Sprite name:"
        spritename = input_dialog(
            title="New Project",
            text=sprite_name_question
        ).run()

        if spritename is None:
            return

        if nomenclature and len(spritename) > 8:
            button_dialog(
                title="New Project",
                text='Error: El nombre de la imagen no puede tener más de 8 caracteres.',
                buttons=[('OK', True)]).run()
        else:
            break
    return  spritename 

def getImageName(nomenclature):
    while True:
        # Pregunta sobre el nombre del proyecto
        image_name_question = "Image name:"
        imagename = input_dialog(
            title="New Project",
            text=image_name_question
        ).run()

        if imagename is None:
            return

        if nomenclature and len(imagename) > 8:
            button_dialog(
                title="New Project",
                text='Error: El nombre de la imagen no puede tener más de 8 caracteres.',
                buttons=[('OK', True)]).run()
        else:
            break
    return  imagename 
    
def getProjectName(nomenclature):
    while True:
        # Pregunta sobre el nombre del proyecto
        project_name_question = "Image name:"
        projectname = input_dialog(
            title="New Project",
            text=project_name_question
        ).run()

        if projectname is None:
            return

        if nomenclature and len(projectname) > 8:
            button_dialog(
                title="New Project",
                text='Error: El nombre del proyecto no puede tener más de 8 caracteres.',
                buttons=[('OK', True)]).run()
        else:
            break
    return  projectname 

def main():
    Title = "New Project"

    nomenclature83 = yes_no_dialog(
        title=Title,
        text='You want to activate the nomenclature 8:3?').run()

    project = getProjectName(nomenclature83)

    add_image = yes_no_dialog(
        title=Title,
        text="Do you want to add an image?").run()


    if add_image:
        while True:
            image_name = getImageName(nomenclature83)
            
            mode_pal_question = "Enter image details:"
            mode_pal_values = [
                ("0", "Mode 0"),
                ("1", "Mode 1"),
                ("2", "Mode 2"),
            ]
            mode_pal_answer = radiolist_dialog(
                title=Title,
                text=mode_pal_question,
                values=mode_pal_values
            ).run()
            
            add_pal= yes_no_dialog(
                title=Title,
                text="Include Pal file in disk?").run()

            
            add_new_image= yes_no_dialog(
                title=Title,
                text="Desea añadir otra imagen").run()
            
            if not add_new_image:
                break

    add_sprite = yes_no_dialog(
        title=Title,
        text="Do you want to add an sprite?").run()


    if add_sprite:
        while True:
            sprite_name = getSpriteName(nomenclature83)
            
            sprite_question = "Enter Sprite details:"
            sprite_values = [
                ("0", "Mode 0"),
                ("1", "Mode 1"),
                ("2", "Mode 2"),
            ]
            sprite_answer = radiolist_dialog(
                title=Title,
                text=sprite_question,
                values=sprite_values
            ).run()
            

            
            add_new_image= yes_no_dialog(
                title=Title,
                text="Desea añadir otra imagen (sprite)").run()
            
            if not add_new_image:
                break

        
    # Imprimir respuestas
    message_dialog(
        title=Title,
        text=f'FFINAL'
    ).run()

if __name__ == '__main__':
    main()

