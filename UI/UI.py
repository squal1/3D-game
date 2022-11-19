from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

import UI.UICommon as UICommon
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

    
    helloworld = UIText("Hello World", align= "center")
    _uiObjects.append(helloworld)

def ProcessEvent(event):
    # global _uiObjects
    # for i in reversed(_uiObjects):
    #     if i.ProcessEvent(event) == True:
    #         return True
    if event.type == pygame.KEYDOWN:
        if event.key in UICommon.keypressed:
            UICommon.keypressed[event.key] = True
            if UICommon.keypressed[pygame.K_ESCAPE]:
                if UICommon.Paused != True:
                    UICommon.Paused = True
                    # print("Paused")
                else:
                    UICommon.Paused = False
                    # print("Unpaused")
            return True
    return False

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