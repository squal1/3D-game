from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL import shaders

#Text
from UI.UIText import UIText

#Image
from PIL import Image

def init():
    global _uiObjects
    global _uiIds
    global _uiNames
    _uiObjects = []
    _uiIds = {}
    _uiNames = {}

    helloworld = UIText("Hello World")
    _uiObjects.append(helloworld)

    pass

def Update(deltaTime):
    global _uiObjects
    for i in _uiObjects:
        i.Update(deltaTime)

def Render(screen):
    global _uiObjects
    for i in _uiObjects:
        i.Render(screen)

def Cleanup():
    pass

def GetElementByID(id):
    global _uiIds
    return _uiIds[id]

def GetElementByName(name):
    global _uiNames
    return _uiNames[name]