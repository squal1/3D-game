import numpy as np
import pygame
import Border
import GamePlay
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import UI.UI as UI
import UI.UICommon as UICommon

import Cube

# Main Init
pygame.init()

# Set screen size
size = width, height = 640, 750
UICommon.ScreenSize[0] = width
UICommon.ScreenSize[1] = height

# Init cube
Cube.Init()


screen = pygame.display.set_mode(size, DOUBLEBUF | OPENGL)

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (width/height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)

glTranslate(1.0, 0.0, -20)
glRotate(-15, 0, 1, 0)
glRotate(30, 1, 0, 0)

# Init UI
UI.init()
# Init GamePlay
GamePlay.Init()


def Update(deltaTime):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if GamePlay.ProcessEvent(event):
            continue

    if UICommon.TogglePause:
        UICommon.Paused = not UICommon.Paused
        UICommon.TogglePause = False
    GamePlay.Update(deltaTime)
    UI.Update(deltaTime)
    return True


def Render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    

    GamePlay.Render()
    Border.Render()
    UI.Render()
    pygame.display.flip()


_gTickLastFrame = pygame.time.get_ticks()
_gDeltaTime = 0.0

while Update(_gDeltaTime):
    Render()
    t = pygame.time.get_ticks()
    _gDeltaTime = (t - _gTickLastFrame) / 1000.0
    _gTickLastFrame = t
