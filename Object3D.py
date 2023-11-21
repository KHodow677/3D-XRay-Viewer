import pygame as pg
from MatrixFunctions import *
from numba import njit

@njit(fastmath=True)
def ANY(array, a, b):
    return np.any((array == a) | (array == b))

class Object3D:
    def __init__(self, renderer, vertices, faces):
        self.renderer = renderer
        self.vertices = np.array(vertices)
        self.faces = faces 

        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.colorFaces = [(pg.Color('white'), face) for face in self.faces]
        self.move, self.drawVertices = True, False

    def Movement(self):
        if self.move:
            self.RotateY(pg.time.get_ticks() % 0.01)

    def Draw(self):
        self.ScreenProjection()
        self.Movement()

    def ScreenProjection(self):
        vertices = self.vertices @ self.renderer.camera.CameraMatrix()
        vertices = vertices @ self.renderer.projection.projectionMatrix

        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.renderer.projection.toScreenMatrix
        vertices = vertices[:, :2]

        for index, colorFace in enumerate(self.colorFaces):
            color, face = colorFace
            polygon = vertices[face]
            if not ANY(polygon, self.renderer.H_WIDTH, self.renderer.H_HEIGHT):
                pg.draw.polygon(self.renderer.screen, color, polygon, 1)

        if self.drawVertices:
            for vertex in vertices:
                if not ANY(vertex, self.renderer.H_WIDTH, self.renderer.H_HEIGHT):
                    pg.draw.circle(self.renderer.screen, pg.Color('white'), vertex, 2)

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

