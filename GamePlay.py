import pygame
from OpenGL.GL import *
import numpy as np
import math
import random

import UI.UI as UI
import UI.UICommon as UICommon

from Quaternion import Quaternion
from TetrisPieces import *


def Init():
    global _blocks
    global _curBlock
    global _fallingSpeed
    global _nextBlock
    global _collectedBlock
    global _order
    global _pos
    global _worldQuat
    global _rotationX
    global _rotationY
    global _rotationZ
    global _rotationXQuat
    global _rotationYQuat
    global _rotationZQuat

    _worldQuat = Quaternion()
    _rotationXQuat = Quaternion().setRotationQuat(np.asfarray([1, 0, 0]), 90.0)
    _rotationYQuat = Quaternion().setRotationQuat(np.asfarray([0, 1, 0]), 90.0)
    _rotationZQuat = Quaternion().setRotationQuat(np.asfarray([0, 0, 1]), 90.0)
    _rotationX = False
    _rotationY = False
    _rotationZ = False

    _blocks = []
    _order = [0, 1, 2, 3, 4, 5, 6]
    random.shuffle(_order)
    _order = _order[:2]
    for order in _order:
        if order == 0:
            _blocks.append(JBlock())
        if order == 1:
            _blocks.append(LBlock())
        if order == 2:
            _blocks.append(ZBlock())
        if order == 3:
            _blocks.append(SBlock())
        if order == 4:
            _blocks.append(TBlock())
        if order == 5:
            _blocks.append(IBlock())
        if order == 6:
            _blocks.append(OBlock())

    _curBlock = _blocks[-2]
    _nextBlock = _blocks[-1]
    _collectedBlock = []
    print("Next:" + _nextBlock.__class__.__name__)
    UICommon.Blocks[_order[-1]].visible = True
    _pos = np.asfarray([-1, 7, -1])

    _fallingSpeed = 3


def ProcessEvent(event):
    global _curBlock
    global _rotationX
    global _rotationY
    global _rotationZ

    if event.type == pygame.KEYDOWN:
        if event.key in UICommon.keypressed:
            UICommon.keypressed[event.key] = True
            if UICommon.keypressed[pygame.K_ESCAPE]:
                UICommon.TogglePause = True
            # Only rotate when not pause
            if not UICommon.Paused:
                if UICommon.keypressed[pygame.K_UP]:
                    _pos[2] -= 2
                if UICommon.keypressed[pygame.K_DOWN]:
                    _pos[2] += 2
                if UICommon.keypressed[pygame.K_LEFT]:
                    _pos[0] -= 2
                if UICommon.keypressed[pygame.K_RIGHT]:
                    _pos[0] += 2
                if UICommon.keypressed[pygame.K_a]:
                    _rotationX = True
                if UICommon.keypressed[pygame.K_s]:
                    _rotationY = True
                if UICommon.keypressed[pygame.K_d]:
                    _rotationZ = True
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
            UICommon.Blocks[_order[-1]].visible = False
            _collectedBlock.append(_curBlock)
            _curBlock.position = _pos
            _curBlock.position[1] = -5
            print(_curBlock.position)
            newBlock = random.randint(0, 6)
            _order.append(newBlock)
            if newBlock == 0:
                _blocks.append(JBlock())
            if newBlock == 1:
                _blocks.append(LBlock())
            if newBlock == 2:
                _blocks.append(ZBlock())
            if newBlock == 3:
                _blocks.append(SBlock())
            if newBlock == 4:
                _blocks.append(TBlock())
            if newBlock == 5:
                _blocks.append(IBlock())
            if newBlock == 6:
                _blocks.append(OBlock())
            _curBlock = _blocks[-2]  # Get new block
            _nextBlock = _blocks[-1]  # Set next block
            UICommon.Blocks[_order[-1]].visible = True
            _pos[1] = 7  # Reset block to top
            UICommon.Score += 40
    # a single line clear is worth 40 points, clearing four lines at once (known as a Tetris) is worth 1200 4*4 lines 36000
    # Score update
    Score = UI.GetElementByName("score")
    Score.text = str(UICommon.Score)
    # # make it collect at bottom
    # if _pos[1] < -5: #Change -5 into piece height later
    #     _pos[1] = -5

    _curBlock.Update(deltaTime)


def Render():
    global _curBlock
    global _collectedBlock
    global _pos
    global _worldQuat
    global _rotationX
    global _rotationY
    global _rotationZ
    global _rotationXQuat
    global _rotationYQuat
    global _rotationZQuat

    if _rotationX:
        _worldQuat = _worldQuat.mult(_rotationXQuat)
        _rotationX = False
    if _rotationY:
        _worldQuat = _worldQuat.mult(_rotationYQuat)
        _rotationY = False
    if _rotationZ:
        _worldQuat = _worldQuat.mult(_rotationZQuat)
        _rotationZ = False

    if not UICommon.Paused:
        m = glGetDouble(GL_MODELVIEW_MATRIX)
        glTranslatef(*_pos)
        glMultMatrixf(_worldQuat.getRotMat4())
        _curBlock.Render()
        # for i in _collectedBlock:
        #     # print(i.position)
        #     glTranslatef(*i.position)
        #     i.Render()
        glLoadMatrixf(m)
