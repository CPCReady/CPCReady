import yaml
import sys

from CPCReady import common as cm


def readProyect():
    if not cm.fileExist("/home/destroyer/Github/CPCReady/sdk/proyect.yml"):
        sys.exit(1)
    with open("/home/destroyer/Github/CPCReady/sdk/proyect.yml", 'r') as archivo:
        dic = yaml.safe_load(archivo)
    return dic

def getNameProjec():
    project = readProyect()
    return project["metadata"]["name"]


def getMergeFiles():
    project = readProyect()
    return project["metadata"]["merge"]


def getImages():
    project = readProyect()
    return project["spec"]["images"]

def getSprites():
    project = readProyect()
    return project["spec"]["sprites"]    

def getEmulators():
    project = readProyect()
    return project["spec"]["emulators"] 

def getCdtFiles():
    project = readProyect()
    return project["spec"]["cdtfiles"] 

def execute():
    print(getNameProjec())
    print(getMergeFiles())
    print(getImages())
    print(getSprites())
    print(getEmulators())
    print(getCdtFiles())