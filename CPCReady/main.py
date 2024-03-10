import click
from CPCReady import __version__
from CPCReady import run as emulador
from CPCReady import palette as pal
from CPCReady import sprite as sprites
from CPCReady import screen as screens
from CPCReady import new as projects
from CPCReady import save as compile
from CPCReady import load as loading
from CPCReady import upgrade as update
from CPCReady import about as my
from CPCReady import common as cm
from CPCReady import yaml as proyecto
from CPCReady import merge as command_merge

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


#, type=click.STRING, help="Input file name.", required=True)

@main.command()
@click.argument('emulator',required=True)
def run(emulator):
    """ Execute DSK/CDT in emulator. """
    try:
        cm.verificar_linux()
        emulador.launch(emulator)
    except Exception as e:
        raise Exception(f"Error {str(e)}")

@main.command()
@click.argument('image')
def palette(image):
    """ Extract the color palette from the image. """
    cm.verificar_linux()
    pal.getSettingPalette(image)

@main.command()
@click.argument('image')
def sprite(image):
    """ Extract the color palette from the image. """
    cm.verificar_linux()
    sprites.getSettingSprite(image)


@main.command()
@click.argument('image')
def screen(image):
    """ Convert an image to Amstrad scr format. Get data Setting project """
    cm.verificar_linux()
    screens.getSettingImage(image)

@main.command()
def new():
    """ Create the project structure for CPCReady. """
    cm.verificar_linux()
    projects.new()


@main.command()
def save():
    """ Create project disk and cdt image. """
    # try:
    #     cm.verificar_linux()
    compile.create()
    # except Exception as e:
    #     raise Exception(f"Error {str(e)}")

@main.command()
def about():
    """ About info CPCReady. """
    try:
        cm.verificar_linux()
        my.show(True)
    except Exception as e:
        raise Exception(f"Error {str(e)}")

@main.command()
def upgrade():
    """ Upgrade CPCReady. """
    try:
        update.version(False)
    except Exception as e:
        raise Exception(f"Error {str(e)}")

@main.command()
def merge():
    """ Merge BAS files in one file. """
    try:
        command_merge.merge()
    except Exception as e:
        raise Exception(f"Error {str(e)}")
    
if __name__ == '__main__':
    main()
