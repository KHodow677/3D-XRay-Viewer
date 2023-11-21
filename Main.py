from Object3D import *
import pygame as pg
from Camera import *
from Projection import *

class SoftwareRenderer:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1280, 720
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self. HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.CreateObject()
    
    def CreateObject(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.Translate([0.2, 0.4, 0.2])
        self.object.RotateY(math.pi / 6)

    def Draw(self):
        self.screen.fill(pg.Color('black'))
        self.object.Draw()

    def Run(self):
        while True:
            self.Draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = SoftwareRenderer()
    app.Run()

