import numpy as np
from math import *


class Quaternion:
    def __init__(self, w=1, x=0, y=0, z=0):
        # Initial state of the quaternion
        self.quat = np.asfarray([w, x, y, z])

    def mult(self, q):
        q1 = self.quat
        q2 = q.quat
        w1, x1, y1, z1 = q1
        w2, x2, y2, z2 = q2
        w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
        x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
        y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
        z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
        self.quat = np.asfarray([w, x, y, z])
        return self

    def setRotationQuat(self, axisVector=np.asfarray([0, 0, 0]), angle=0.0):
        # Convert vector to normal vector
        axisVector /= np.linalg.norm(axisVector)
        angle *= np.pi / 180
        angle /= 2
        w = cos(angle)
        x = axisVector[0] * sin(angle)
        y = axisVector[1] * sin(angle)
        z = axisVector[2] * sin(angle)
        self.quat = np.asfarray([w, x, y, z])
        return self

    def getRotMat4(self):
        w, x, y, z = self.quat
        c00 = 1 - 2 * y * y - 2 * z * z
        c01 = 2 * (x * y - w * z)
        c02 = 2 * (x * z + w * y)
        c10 = 2 * (x * y + w * z)
        c11 = 1 - 2 * x * x - 2 * z * z
        c12 = 2 * (y * z - w * x)
        c20 = 2 * (x * z - w * y)
        c21 = 2 * (y * z + w * x)
        c22 = 1 - 2 * x * x - 2 * y * y

        rotMat4 = np.asfarray([[c00, c01, c02, 0],
                              [c10, c11, c12, 0],
                              [c20, c21, c22, 0],
                              [0, 0, 0, 1]])
        return rotMat4
