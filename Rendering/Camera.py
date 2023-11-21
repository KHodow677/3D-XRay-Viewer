from numpy import who
import pygame as pg
import math
from Rendering.MatrixFunctions import *

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

        self.anglePitch = 0
        self.angleYaw = 0
        self.angleRoll = 0

        self.movementSpeed = 0.2
        self.rotationSpeed = 0.05

    def Control(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.position -= self.right * self.movementSpeed
        if key[pg.K_d]:
            self.position += self.right * self.movementSpeed
        if key[pg.K_w]:
            self.position += self.forward * self.movementSpeed
        if key[pg.K_s]:
            self.position -= self.forward * self.movementSpeed
        if key[pg.K_q]:
            self.position += self.up * self.movementSpeed
        if key[pg.K_e]:
            self.position -= self.up * self.movementSpeed

        if key[pg.K_LEFT]:
            self.CameraYaw(-self.rotationSpeed)
        if key[pg.K_RIGHT]:
            self.CameraYaw(self.rotationSpeed)
        if key[pg.K_UP]:
            self.CameraPitch(-self.rotationSpeed)
        if key[pg.K_DOWN]:
            self.CameraPitch(self.rotationSpeed)

    def CameraYaw(self, angle):
        self.angleYaw += angle

    def CameraPitch(self, angle):
        self.anglePitch += angle

    def AxesIdentity(self):
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])

    def UpdateCameraAxes(self):
        rotate = RotateX(self.anglePitch) @ RotateY(self.angleYaw)
        self.AxesIdentity()
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

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
        self.UpdateCameraAxes()
        return self.TranslationMatrix() @ self.RotationMatrix()

