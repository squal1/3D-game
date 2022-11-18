from OpenGL.GL import *
from OpenGL.GLU import *

#Text
from UI.UIText import UIText
#Image
from UI.UIImage import UIImage

def init():
    global _uiObjects
    global _uiIds
    global _uiNames
    _uiObjects = []
    _uiIds = {}
    _uiNames = {}

    helloworld = UIText("Hello World",align= "center")
    _uiObjects.append(helloworld)


def Update(deltaTime):
    global _uiObjects
    for i in _uiObjects:
        i.Update(deltaTime)

def Render():
    global _uiObjects
    for i in _uiObjects:
        i.Render()

def Cleanup():
    pass

def GetElementByID(id):
    global _uiIds
    return _uiIds[id]

def GetElementByName(name):
    global _uiNames
    return _uiNames[name]