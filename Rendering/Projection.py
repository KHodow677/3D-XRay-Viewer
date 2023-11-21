import math
import numpy as np

class Projection:
    def __init__(self, renderer):
        NEAR = renderer.camera.nearPlane
        FAR = renderer.camera.farPlane
        RIGHT = math.tan(renderer.camera.hFOV / 2)
        LEFT = -RIGHT
        TOP = math.tan(renderer.camera.vFOV / 2)
        BOTTOM = -TOP

        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = (FAR + NEAR) / (FAR - NEAR)
        m32 = -2 * NEAR * FAR / (FAR - NEAR)
        self.projectionMatrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

        HW, HH = renderer.H_WIDTH, renderer.H_HEIGHT
        self.toScreenMatrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])

