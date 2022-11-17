from OpenGL.GL import *
import numpy as np
import math


class TetrisPieces:
    def __init__(self, verts, surfaces):
        self.verts = verts
        self.surfaces = surfaces
        self.color = np.asfarray([0, 0, 1])
        self.ang = 0
        self.axis = (3, 1, 1)

    def Update(self, deltaTime):
        self.ang += 50.0 * deltaTime

    def _DrawBlock(self):
        glBegin(GL_QUADS)
        for n, surface in enumerate(self.surfaces):
            for vert in surface:
                glColor3fv(self.color)
                glVertex3fv(self.verts[vert])
        glEnd()

    def Render(self):
        m = glGetDouble(GL_MODELVIEW_MATRIX)

        glRotatef(self.ang, *self.axis)
        self._DrawBlock()

        glLoadMatrixf(m)


class I(TetrisPieces):
    def __init__(self):
        verts = np.asfarray([(0, -1, 0), (1, -1, 0), (0, 3, 0), (1, 3, 0),
                             (0, -1, 1), (1, -1, 1), (0, 3, 1), (1, 3, 1)])
        surfaces = np.array([(0, 1, 2, 3),
                             (3, 2, 7, 6),
                             (6, 7, 5, 4),
                             (4, 5, 1, 0),
                             (1, 5, 7, 3),
                             (4, 0, 2, 6)])
        super().__init__(verts, surfaces)


class O(TetrisPieces):
    def __init__(self):
        verts = np.asfarray([(-1, -1, 0), (1, -1, 0), (-1, 1, 0), (1, 1, 0),
                             (-1, -1, 1), (1, -1, 1), (-1, 1, 1), (1, 1, 1)])
        surfaces = np.array([(0, 1, 2, 3),
                             (3, 2, 7, 6),
                             (6, 7, 5, 4),
                             (4, 5, 1, 0),
                             (1, 5, 7, 3),
                             (4, 0, 2, 6)])
        super().__init__(verts, surfaces)


class T(TetrisPieces):
    def __init__(self):
        verts = np.asfarray([(0, -1, 0), (1, -1, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0), (1, 1, 0), (1, 2, 0), (0, 2, 0),
                             (0, -1, 1), (1, -1, 1), (1, 0, 1), (2, 0, 1), (2, 1, 1), (1, 1, 1), (1, 2, 1), (0, 2, 1)])
        surfaces = np.array([(0, 1, 6, 7),
                             (2, 3, 4, 5),
                             (8, 9, 14, 15),
                             (10, 11, 12, 13),
                             (0, 7, 15, 8),
                             (6, 7, 15, 14),
                             (5, 6, 14, 13),
                             (4, 5, 13, 12),
                             (3, 4, 12, 11),
                             (2, 3, 11, 10),
                             (1, 2, 10, 9),
                             (0, 1, 9, 8)])
        super().__init__(verts, surfaces)


class S(TetrisPieces):
    pass


class Z(TetrisPieces):
    pass


class J(TetrisPieces):
    pass


class L(TetrisPieces):
    pass
