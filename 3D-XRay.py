from Rendering.Object3D import *
import pygame as pg
import math
from Rendering.Camera import *
from Rendering.Projection import *

class SoftwareRenderer:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 1280, 720
        self.hWidth, self.hHeight = self.width // 2, self.height // 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self.CreateObject()
    
    def CreateObject(self):
        self.camera = Camera(self, [0, 2, -10])
        self.projection = Projection(self)
        self.object = self.LoadObjectFromFile('wood-house.obj')
        self.object.RotateY(math.pi / 2)

    def LoadObjectFromFile(self, filename):
        vertices, faces = [], []
        with open(filename) as file:
            for line in file:
                if line.startswith('v '):
                    vertices.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    fileFaces = line.split()[1:]
                    faces.append([int(face.split('/')[0]) - 1 for face in fileFaces])
        return Object3D(self, vertices, faces)

    def Draw(self):
        self.screen.fill(pg.Color('black'))
        self.object.Draw()

    def Run(self):
        while True:
            self.Draw()
            self.camera.Control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    app = SoftwareRenderer()
    app.Run()

