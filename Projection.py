import math
import numpy as np

class Projection:
    def __init__(self, renderer):
        near = renderer.camera.nearPlane
        far = renderer.camera.farPlane
        right = math.tan(renderer.camera.hFOV / 2)
        left = -right
        top = math.tan(renderer.camera.vFOV / 2)
        bottom = -top

        m00 = 2 / (right - left)
        m11 = 2 / (top - bottom)
        m22 = (far + near) / (far - near)
        m32 = -2 * near * far / (far - near)
        self.projectionMatrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]])

        hWidth, hHeight = renderer.H_WIDTH, renderer.H_HEIGHT
        self.toScreenMatrix = np.array([
            [hWidth, 0, 0, 0],
            [0, -hHeight, 0, 0],
            [0, 0, 1, 0],
            [hWidth, hHeight, 0, 1]])

