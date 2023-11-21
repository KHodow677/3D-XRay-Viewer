import pygame as pg
from MatrixFunctions import *

class Object3D:
    def __init__(self, renderer):
        self.renderer = renderer
        self.vertices = np.array([
            (0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
            (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])

        self.faces = np.array([
            (0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 6, 7, 3),
            (0, 4, 3, 7), (1, 5, 6, 2)])

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


