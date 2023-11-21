import pygame as pg
from MatrixFunctions import *

class Object3D:
    def __init__(self, renderer):
        self.renderer = renderer
        self.vertices = np.array([
            (0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
            (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])

        self.faces = np.array([
            (0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 3, 7, 6),
            (1, 2, 6, 5), (0, 3, 7, 4)])

    def Draw(self):
        self.ScreenProjection()

    def ScreenProjection(self):
        vertices = self.vertices @ self.renderer.camera.CameraMatrix()
        vertices = vertices @ self.renderer.projection.projectionMatrix

        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 1) | (vertices < -1)] = 0
        vertices = vertices @ self.renderer.projection.toScreenMatrix
        vertices = vertices[:, :2]

        print(vertices)

        for face in self.faces:
            polygon = vertices[face]
            if not np.any((polygon == self.renderer.H_WIDTH) | (polygon == self.renderer.H_HEIGHT)):
                pg.draw.polygon(self.renderer.screen, pg.Color('white'), polygon, 3)

        for vertex in vertices:
            if not np.any((vertex == self.renderer.H_WIDTH) | (polygon == self.renderer.H_HEIGHT)):
                pg.draw.circle(self.renderer.screen, pg.Color('white'), vertex, 6)

    def Translate(self, pos):
        self.vertices = self.vertices @ Translate(pos)
    
    def Scale(self, scaleTo):
        self.vertices = self.vertices @ Scale(scaleTo)

    def RotateX(self, angle):
        self.vertices = self.vertices @ RotateX(angle)

    def RotateY(self, angle):
        self.vertices = self.vertices @ RotateY(angle)

    def RotateZ(self, angle):
        self.vertices = self.vertices @ RotateZ(angle)


