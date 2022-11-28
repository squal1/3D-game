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

    helloworld = UIText("Hello World", align = "center")
    scoretag = UIText("Score", size = 16, align = "right", xoffset= -20, yoffset=-30)
    score = UIText("0", align = "right", xoffset= -20, yoffset=-50)
    preview = UIText("Next Block", size = 16, align = "right", valign = "center", xoffset= -25, yoffset=-30)
    _paused = UIText("Game Paused", align = "center", valign = "center", visible = False)
    I = UIImage("UI/Data/I.png", align = "right", valign = "center", xoffset= -40, yoffset=-75, visible = False)
    O = UIImage("UI/Data/O.png", align = "right", valign = "center", xoffset= -40, yoffset=-75, visible = False)
    T = UIImage("UI/Data/T.png", align = "right", valign = "center", xoffset= -40, yoffset=-75, visible = False)
    S = UIImage("UI/Data/S.png", align = "right", valign = "center", xoffset= -40, yoffset=-75, visible = False)
    Z = UIImage("UI/Data/Z.png", align = "right", valign = "center", xoffset= -40, yoffset=-75, visible = False)
    J = UIImage("UI/Data/J.png", align = "right", valign = "center", xoffset= -40, yoffset=-75, visible = False)
    L = UIImage("UI/Data/L.png", align = "right", valign = "center", xoffset= -40, yoffset=-75, visible = False)
    
    _uiObjects.append(helloworld)
    _uiObjects.append(scoretag)
    _uiObjects.append(score)
    _uiNames["score"] = score
    _uiObjects.append(preview)
    _uiObjects.append(_paused)
    # _uiObjects.append(I)
    # _uiObjects.append(O)
    # _uiObjects.append(T)
    # _uiObjects.append(S)
    # _uiObjects.append(Z)
    # _uiObjects.append(J)
    # _uiObjects.append(L)
    
    UICommon.Blocks = [J, L, Z, S,
               T, I, O]


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
    for i in UICommon.Blocks:
        i.Update(deltaTime)
        # print(i.path + str(i.visible))
    


def Render():
    global _uiObjects
    
    for i in _uiObjects:
        if i.visible:
            i.Render()
    for i in UICommon.Blocks:
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