import pygame
from OpenGL.GL import *
import numpy as np
import math
import random

import UI.UI as UI
import UI.UICommon as UICommon


from TetrisPieces import *


def Init():
    global _blocks
    global _curBlock
    global _fallingSpeed
    global _nextBlock
    global _order
    global _pos

    _blocks = [JBlock(), LBlock(), ZBlock(), SBlock(),
               TBlock(), IBlock(), OBlock()]

    _order = [0, 1, 2, 3, 4, 5, 6]
    random.shuffle(_order)
    _order = _order[:3]
    _curBlock = _blocks[_order.pop(0)]
    _nextBlock = _blocks[_order[0]]
    _pos = np.asfarray([-1, 7, -1])

    _fallingSpeed = 3


def ProcessEvent(event):
    global _curBlock
    # Do nothing during paused unless it's for resuming the game
    if UICommon.Paused == True and event.key != pygame.K_ESCAPE:
        return
    if event.type == pygame.KEYDOWN:
        if event.key in UICommon.keypressed:
            UICommon.keypressed[event.key] = True
            if UICommon.keypressed[pygame.K_ESCAPE]:
                UICommon.TogglePause = True
            if UICommon.keypressed[pygame.K_UP]:
                _pos[2] -= 2
            if UICommon.keypressed[pygame.K_DOWN]:
                _pos[2] += 2
            if UICommon.keypressed[pygame.K_LEFT]:
                _pos[0] -= 2
            if UICommon.keypressed[pygame.K_RIGHT]:
                _pos[0] += 2
            return True
    elif event.type == pygame.KEYUP:
        if event.key in UICommon.keypressed:
            UICommon.keypressed[event.key] = False
            return True
    return False


def Update(deltaTime):
    global _curBlock
    global _fallingSpeed
    global _nextBlock
    global _order
    global _pos

    if not UICommon.Paused:
        _pos[1] -= _fallingSpeed * deltaTime
        if _pos[1] <= -5:  # If height of the block <= -5
            _curBlock = _blocks[_order.pop(0)]  # Get new block
            _nextBlock = _blocks[_order[0]]  # Set next block
            print("Next:" + _nextBlock.__class__.__name__)
            _order.append(random.randint(0, 6))  # Append new block to order
            _pos[1] = 7  # Reset block to top

        # # make it collect at bottom
        # if _pos[1] < -5: #Change -5 into piece height later
        #     _pos[1] = -5

    _curBlock.Update(deltaTime)


def Render():
    global _curBlock
    global _pos
    m = glGetDouble(GL_MODELVIEW_MATRIX)
    glTranslatef(*_pos)
    if not UICommon.Paused:
        _curBlock.Render()
    glLoadMatrixf(m)
