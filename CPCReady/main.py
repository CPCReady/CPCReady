
import click
from CPCReady import __version__
from CPCReady import func_run as emulador
from CPCReady import common as cm



@click.group()
def main():
    """ CLI Software Developer Kit for programming in Amstrad Basic and Ugbasic """

@main.command()
@click.option('--file', '-f',required=False, help="File with emulator configurations")
@click.option('--setting', '-s',required=True, help="Emulator Settings Name")

def run(file, setting):
    """ Execute DSK/CDT in emulator """
    try:
        if not file:
            file = cm.CFG_EMULATORS
        emulador.launch(file,setting)
    except Exception as e:
        raise Exception(f"Error {str(e)}")

# @main.command()
# @click.option('--issue', '-i',required=True, help="issue key")

# def delete(issue):
#     """ Delete issue """
#     try:
#         func.delete_issue(issue)
#     except Exception as e:
#         logging.error(f"ERROR: {str(e)}")
#         raise Exception(f"Error {str(e)}")

# @main.command()
# @click.option('--issue', '-i',required=True, help="issue key")
# @click.option('--user', '-u',required=True, help="User to be assigned with X format")

# def assign(user,issue):
#     """ Assign user to issue """
#     try:
#         func.assignment_issue(issue,user)
#     except Exception as e:
#         logging.error(f"ERROR: {str(e)}")
#         raise Exception(f"Error {str(e)}")

# @main.command()
# @click.option('--issue', '-i',required=True, help="issue key")
# @click.option('--user', '-u',required=True, help="User to be assigned with X format")

# def observer(user,issue):
#     """ Add observer user to issue """
#     try:
#         func.observer_issue(issue,user)
#     except Exception as e:
#         logging.error(f"ERROR: {str(e)}")
#         raise Exception(f"Error {str(e)}")

# @main.command()
# @click.option('--issue', '-i',required=True, help="issue key")
# @click.option('--summary', '-s',required=False, help="update field summay")
# @click.option('--description', '-d',required=False, help="update field description")

# def update(issue,summary, description):
#     """ Update fields issue (summary, description) """
#     try:
#         func.update_issue(issue,summary,description)
#     except Exception as e:
#         logging.error(f"ERROR: {str(e)}")
#         raise Exception(f"Error {str(e)}")

# @main.command()
# @click.option('--issue', '-i',required=True, help="issue key")
# @click.option('--name', '-n',required=True, help="Tag to add")

# def label(issue,name):
#     """ Update issue labels """
#     try:
#         func.update_label(issue,name)
#     except Exception as e:
#         logging.error(f"ERROR: {str(e)}")
#         raise Exception(f"Error {str(e)}")

# @main.command()
# @click.option('--issue', '-i',required=True, help="issue key")
# @click.option('--state', '-n',type=click.Choice(['PROGRESS', 'CLOSE'], case_sensitive=False), required=True)

# def transition(issue,state):
#     """ Transitions issue state (PROGRESS, CLOSE) """
#     try:
#         func.transition_issue(issue,state)
#     except Exception as e:
#         logging.error(f"ERROR: {str(e)}")
#         raise Exception(f"Error {str(e)}")

if __name__ == '__main__':
    main()