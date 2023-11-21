import pygame as pg
from MatrixFunctions import *

class Object3D:
    def __init__(self, renderer, vertices, faces):
        self.renderer = renderer
        self.vertices = np.array(vertices)
        self.faces = faces 

        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.colorFaces = [(pg.Color('white'), face) for face in self.faces]
        self.move, self.drawVertices = True, False
        self.label = ''

    def Movement(self):
        if self.move:
            self.RotateY(pg.time.get_ticks() % 0.005)

    def Draw(self):
        self.ScreenProjection()
        self.Movement()

    def ScreenProjection(self):
        vertices = self.vertices @ self.renderer.camera.CameraMatrix()
        vertices = vertices @ self.renderer.projection.projectionMatrix

        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices = vertices @ self.renderer.projection.toScreenMatrix
        vertices = vertices[:, :2]

        for index, colorFace in enumerate(self.colorFaces):
            color, face = colorFace
            polygon = vertices[face]
            pg.draw.polygon(self.renderer.screen, color, polygon, 1)
            if self.label:
                text = self.font.render(self.label[index], True, pg.Color('white'))
                self.renderer.screen.blit(text, polygon[-1])

        if self.drawVertices:
            for vertex in vertices:
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

class Axes(Object3D):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.vertices = np.array([(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])
        self.faces = np.array([(0, 1), (0, 2), (0, 3)])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.colorFaces = [(color,face) for color, face in zip(self.colors, self.faces)]
        self.drawVertices = False
        self.label = 'XYZ'

