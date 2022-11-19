import pygame
from OpenGL.GL import *
import numpy as np
import math
import random

import UI.UI as UI
import UI.UICommon as UICommon
import Cube



def Init():
    global _cube
    global _pos
    _cube = Cube.Cube()
    _pos = np.asfarray([-1, 7, -1])


def ProcessEvent(event):
    if event.type == pygame.KEYDOWN:
        if event.key in UICommon.keypressed:
            UICommon.keypressed[event.key] = True
            if UICommon.keypressed[pygame.K_ESCAPE]:
                UICommon.TogglePause = True
            return True
        elif event.type == pygame.KEYUP:
            if event.key in UICommon.keypressed:
                UICommon.keypressed[event.key] = False
                return True
    return False


def Update(deltaTime):
    global _cube
    global _pos

    
    if not UICommon.Paused:
        # let it fall
        if _pos[1] > -5: #Change -5 into piece height later
            _pos[1] -= 1 * deltaTime
        # if _pos[1] <= -5:
        #     _pos[1] = 7
        # make it collect at bottom
        if _pos[1] < -5: #Change -5 into piece height later
            _pos[1] = -5
    _cube.Update(deltaTime)


def Render():
    global _cube
    global _pos
    m = glGetDouble(GL_MODELVIEW_MATRIX)
    glTranslatef(*_pos)
    if not UICommon.Paused:
        _cube.Render()
    glLoadMatrixf(m)
