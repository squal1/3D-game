from OpenGL.GL import *
import numpy as np
from Cube import Cube


class TetrisPieces:
    def __init__(self, components):
        self.components = components
        self.pos = np.asfarray([0, 0, 0])

    def Update(self, deltaTime):
        for component in self.components:
            component.Update(deltaTime)

    def Render(self):
        m = glGetDouble(GL_MODELVIEW_MATRIX)
        for component in self.components:
            component.Render()
        glLoadMatrixf(m)


class IBlock(TetrisPieces):
    def __init__(self):
        components = [Cube("LightBlue", np.asfarray([-2, 0, 0])),
                      Cube("LightBlue", np.asfarray([0, 0, 0])),
                      Cube("LightBlue", np.asfarray([2, 0, 0])),
                      Cube("LightBlue", np.asfarray([4, 0, 0]))]
        super().__init__(components)


class OBlock(TetrisPieces):
    def __init__(self):
        components = [Cube("Yellow", np.asfarray([-2, 0, 0])),
                      Cube("Yellow", np.asfarray([-2, 2, 0])),
                      Cube("Yellow", np.asfarray([0, 0, 0])),
                      Cube("Yellow", np.asfarray([0, 2, 0]))]
        super().__init__(components)


class TBlock(TetrisPieces):
    def __init__(self):
        components = [Cube("Purple", np.asfarray([-2, 0, 0])),
                      Cube("Purple", np.asfarray([0, 0, 0])),
                      Cube("Purple", np.asfarray([2, 0, 0])),
                      Cube("Purple", np.asfarray([0, 2, 0]))]
        super().__init__(components)


class SBlock(TetrisPieces):
    def __init__(self):
        components = [Cube("Red", np.asfarray([2, 2, 0])),
                      Cube("Red", np.asfarray([0, 2, 0])),
                      Cube("Red", np.asfarray([0, 0, 0])),
                      Cube("Red", np.asfarray([-2, 0, 0]))]
        super().__init__(components)


class ZBlock(TetrisPieces):
    def __init__(self):
        components = [Cube("Green", np.asfarray([-2, 2, 0])),
                      Cube("Green", np.asfarray([0, 2, 0])),
                      Cube("Green", np.asfarray([0, 0, 0])),
                      Cube("Green", np.asfarray([2, 0, 0]))]
        super().__init__(components)


class JBlock(TetrisPieces):
    def __init__(self):
        components = [Cube("Blue", np.asfarray([-2, 0, 0])),
                      Cube("Blue", np.asfarray([0, 0, 0])),
                      Cube("Blue", np.asfarray([2, 0, 0])),
                      Cube("Blue", np.asfarray([-2, 2, 0]))]
        super().__init__(components)


class LBlock(TetrisPieces):
    def __init__(self):
        components = [Cube("Orange", np.asfarray([-2, 0, 0])),
                      Cube("Orange", np.asfarray([0, 0, 0])),
                      Cube("Orange", np.asfarray([2, 0, 0])),
                      Cube("Orange", np.asfarray([2, 2, 0]))]
        super().__init__(components)
