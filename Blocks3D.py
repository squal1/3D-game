import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import UI.UICommon as UICommon

from SlowCube import SlowCube
from TetrisPieces import I, O, T, S, Z, J, L



# Main Init
pygame.init()

# Set screen size
size = width, height = 640, 750
UICommon.ScreenSize[0] = width
UICommon.ScreenSize[1] = height

# Init UI
import UI.UI as UI
UI.init()

screen = pygame.display.set_mode(size, DOUBLEBUF | OPENGL)

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (width/height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)

glTranslate(0.0, 0.0, -10)

cube = SlowCube()
IBlock = I()
OBlock = O()
TBlock = T()
SBlock = S()
ZBlock = Z()
JBlock = J()
LBlock = L()


def Update(deltaTime):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    IBlock.Update(deltaTime)
    OBlock.Update(deltaTime)
    TBlock.Update(deltaTime)
    SBlock.Update(deltaTime)
    ZBlock.Update(deltaTime)
    JBlock.Update(deltaTime)
    LBlock.Update(deltaTime)
    UI.Update(deltaTime)
    return True


def Render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    IBlock.Render()
    OBlock.Render()
    TBlock.Render()
    SBlock.Render()
    ZBlock.Render()
    JBlock.Render()
    LBlock.Render()
    UI.Render()
    pygame.display.flip()


_gTickLastFrame = pygame.time.get_ticks()
_gDeltaTime = 0.0

while Update(_gDeltaTime):
    Render()
    t = pygame.time.get_ticks()
    _gDeltaTime = (t - _gTickLastFrame) / 1000.0
    _gTickLastFrame = t
