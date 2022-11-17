from OpenGL.GL import *
import numpy as np
import math

# Light always from the camera
_lightVector = np.asfarray([0, 0, 1])


class SlowCube:
    def __init__(self):
        self.verts = np.asfarray([(1, -1, -1),  # Distance from (0,0,0)
                                  (1, 1, -1),
                                  (-1, 1, -1),
                                  (-1, -1, -1),
                                  (1, -1, 1),
                                  (1, 1, 1),
                                  (-1, -1, 1),
                                  (-1, 1, 1)])

        self.surfaces = np.array([(0, 1, 2, 3),  # Surface of first 4 vertices
                                  (3, 2, 7, 6),
                                  (6, 7, 5, 4),
                                  (4, 5, 1, 0),
                                  (1, 5, 7, 2),
                                  (4, 0, 3, 6)])

        self.normals = np.asfarray([(0, 0, -1),
                                    (-1, 0, 0),
                                    (0, 0, 1),
                                    (1, 0, 0),
                                    (0, 1, 0),
                                    (0, -1, 0)])

        self.color = np.asfarray([0, 0, 1])
        self.ang = 0
        self.axis = (3, 1, 1)

    def Update(self, deltaTime):
        self.ang += 50.0 * deltaTime

    def _DrawBlock(self):
        global _lightVector

        invT = np.linalg.inv(glGetDouble(GL_MODELVIEW_MATRIX)).transpose()
        glBegin(GL_QUADS)
        for n, surface in enumerate(self.surfaces):
            for vert in surface:
                # Append 1 at the end to apply inverse transform
                norm = np.append(self.normals[n], 1)
                modelNorm = np.matmul(norm, invT)
                # Delete it afterwards
                modelNorm = np.delete(modelNorm, 3)
                np.linalg.norm(modelNorm)

                dotP = np.dot(_lightVector, modelNorm)
                mult = max(min(dotP, 1), 0)

                glColor3fv(self.color * mult)
                glVertex3fv(self.verts[vert])
        glEnd()

    def Render(self):
        m = glGetDouble(GL_MODELVIEW_MATRIX)

        glRotatef(self.ang, *self.axis)
        self._DrawBlock()

        glLoadMatrixf(m)
