from OpenGL.GL import *
import numpy as np
from Cube import Cube


class TetrisPieces:
    def __init__(self, components, pos):
        self.componemts = []
        self.pos = pos

    def _DrawBlock(self):
        pass

    def _RotateX(self):
        self.angX = 90 * pi/180

    def _RotateY(self):
        self.angY = 90 * pi/180

    def _RotateZ(self):
        self.angZ = 90 * pi/180

    def Update(self, deltaTime):
        pass

    def Render(self):
        pass


class I(TetrisPieces):
    def __init__(self):
        pass

    def Update(self, deltaTime):
        pass


class O(TetrisPieces):
    def __init__(self):
        pass

    def Update(self, deltaTime):
        pass


class T(TetrisPieces):
    def __init__(self):
        pass

    def Update(self, deltaTime):
        pass


class S(TetrisPieces):
    def __init__(self):
        pass

    def Update(self, deltaTime):
        pass


class Z(TetrisPieces):
    def __init__(self):
        pass

    def Update(self, deltaTime):
        pass


class J(TetrisPieces):
    def __init__(self):
        pass

    def Update(self, deltaTime):
        pass


class L(TetrisPieces):
    def __init__(self):
        pass

    def Update(self, deltaTime):
        pass
