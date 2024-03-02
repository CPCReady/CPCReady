import click
from CPCReady import __version__
from CPCReady import func_run as emulador
from CPCReady import func_palette as pal
from CPCReady import func_sprite as sprites
from CPCReady import func_screen as screens
from CPCReady import func_project as projects
from CPCReady import func_build as compile
from CPCReady import func_info as information
from CPCReady import func_update as update
from CPCReady import func_about as my
from CPCReady import common as cm
from CPCReady import func_yaml as proyecto

import logging
import requests
import os

requests.packages.urllib3.disable_warnings()
logging.getLogger("requests").setLevel(logging.WARNING)

module_path = os.path.dirname(os.path.abspath(__file__))

@click.version_option(version=__version__)
@click.group()
def main():
    """ CLI SDK for programming in Amstrad Locomotive Basic. """


@main.command()
@click.option('--setting', '-s', required=False, default="", help="Emulator Settings Name")
def run(setting):
    """ Execute DSK/CDT in emulator. """
    try:
        cm.verificar_linux()
        if not setting:
            setting = cm.getFirstEmulator()
        emulador.launch(setting)
    except Exception as e:
        raise Exception(f"Error {str(e)}")


@main.command()
@click.option("-i", "--image", "image", type=click.STRING, help="Input file name", required=True)
@click.option("-m", "--mode", "mode", type=click.Choice(["0", "1", "2"]), help="Image Mode (0, 1, 2)", required=True)
def palette(image, mode):
    """ Extract the color palette from the image. """
    cm.verificar_linux()
    pal.getData(image, mode)


@main.command()
@click.option("-i", "--image", type=click.STRING, help="Input file name", required=True)
@click.option("-m", "--mode", type=click.Choice(["0", "1", "2"]), help="Image Mode (0, 1, 2)", required=True)
@click.option("-o", "--out", type=click.STRING, help="Out path file name", required=True)
@click.option("-h", "--height", type=click.INT, help="Height sprite size", required=True)
@click.option("-w", "--width", type=click.INT, help="Width sprite size", required=True)
def sprite(image, mode, out, height, width):
    """ Extract the color palette from the image. """
    cm.verificar_linux()
    sprites.create(image, mode, out, height, width)


@main.command()
@click.option("-i", "--image", type=click.STRING, help="Input file name.", required=True)
@click.option("-m", "--mode", type=click.Choice(["0", "1", "2"]), help="Image Mode (0, 1, 2)", required=True)
@click.option("-o", "--out", type=click.STRING, help="Out path file name.", required=True)
@click.option("-d", "--dsk", is_flag=True, help="Generate DSK with only the scr image.", required=False)
def screen(image, mode, out, dsk):
    """ Convert an image to Amstrad scr format. """
    cm.verificar_linux()
    screens.create(image, mode, out, dsk)


@main.command()
def project():
    """ Create the project structure for CPCReady. """
    cm.verificar_linux()
    projects.create()


@main.command()
def build():
    """ Create project disk and cdt image. """
    try:
        cm.verificar_linux()
        compile.create()
    except Exception as e:
        raise Exception(f"Error {str(e)}")


@main.command()
def info():
    """ Info Project. """
    try:
        cm.verificar_linux()
        information.projectInformation()
    except Exception as e:
        raise Exception(f"Error {str(e)}")

@main.command()
def about():
    """ About info CPCReady. """
    try:
        cm.verificar_linux()
        my.show(True)
    except Exception as e:
        raise Exception(f"Error {str(e)}")



# @main.command()
# def upgrade():
#     """ Upgrade CPCReady. """
#     try:
#         update.version(False)
#     except Exception as e:
#         raise Exception(f"Error {str(e)}")


if __name__ == '__main__':
    main()
