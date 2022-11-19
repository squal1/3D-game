from OpenGL.GL import *
from OpenGL.GLU import *

import UI.UICommon as UICommon
#Text
from UI.UIText import UIText
#Image
from UI.UIImage import UIImage

def init():
    global _uiObjects
    global _uiIds
    global _uiNames
    global _paused
    _uiObjects = []
    _uiIds = {}
    _uiNames = {}

    # helloworld = UIText("Hello World", align = "center")
    # score = UIText("", align = "center")
    I = UIImage("/I.png", align = "right")
    _paused = UIText("Paused", align = "center", valign = "center", visible = False)
    # _uiObjects.append(helloworld)
    _uiObjects.append(_paused)


def Update(deltaTime):
    global _uiObjects
    global _paused
    for i in _uiObjects:
        i.Update(deltaTime)
        if UICommon.Paused:
            i.visible = False
            _paused.visible = True
        else:
            i.visible = True
            _paused.visible = False


def Render():
    global _uiObjects
    for i in _uiObjects:
        if i.visible:
            i.Render()

def Cleanup():
    pass

def GetElementByID(id):
    global _uiIds
    return _uiIds[id]

def GetElementByName(name):
    global _uiNames
    return _uiNames[name]