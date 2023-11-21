from numpy import who
import pygame as pg
import math
from MatrixFunctions import *

class Camera:
    def __init__(self, renderer, position) -> None:
        self.renderer = renderer
        self.position = np.array([*position, 1.0])

        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])
        self.hFOV = math.pi / 3
        self.vFOV = self.hFOV * (renderer.HEIGHT/ renderer.WIDTH)
        
        self.nearPlane = 0.1
        self.farPlane = 100

    def TranslationMatrix(self):
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]])

    def RotationMatrix(self):
        fx, fy, fz, w = self.forward
        rx, ry, rz, w = self.right
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]])
    
    def CameraMatrix(self):
        return self.TranslationMatrix() @ self.RotationMatrix()

