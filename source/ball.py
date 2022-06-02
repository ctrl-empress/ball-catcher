import pygame as pg
from config import *


class Ball:
    ACCELERATION = 3

    def __init__(self, canvas: pg.Surface, color, position, size):
        self.canvas = canvas
        self.color = color
        self.position = position
        self.size = size
        self.rect = pg.Rect(self.position, (0,0))
        self.velocity = pg.Vector2()
        self.delete_this = False

    def get_body(self):
        return self.rect

    def update(self, time):
        self.check_position()

        if self.velocity.y < GRAVITY:
            self.velocity.y += self.ACCELERATION

        self.position.y += self.velocity.y * time
        self.rect.y = round(self.position.y)
    
    def render(self):
        self.rect = pg.draw.circle(self.canvas, 
                                   self.color, 
                                   self.position, 
                                   self.size)

    def mark_to_delete(self):
        self.delete_this = True

    def is_to_delete(self):
        return self.delete_this

    def check_position(self):
        canvas_size = pg.Vector2(self.canvas.get_size())
        if self.position.y >= canvas_size.y:
            self.mark_to_delete()