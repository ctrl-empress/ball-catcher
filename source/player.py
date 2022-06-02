import pygame as pg
from config import *

class Player:
    LEFT = pg.Vector2(-1, 0)
    RIGHT = pg.Vector2(1, 0)
    direction = pg.Vector2()
    
    def __init__(self, canvas, color, size, position):
        self.canvas = canvas
        self.color = color
        self.size = size
        self.position = position
        self.rect = pg.Rect(self.position, self.size)
        self.catched = 0

    def catch(self, ball):
        if self.rect.colliderect(ball.get_body()):
            ball.mark_to_delete()
            self.catched += 1

    def get_catch(self):
        return self.catched

    def move(self, direction):
        self.direction = direction

    def update(self, time):
        cur_pos = self.position
        canvas_size = pg.Vector2(self.canvas.get_size())

        self.position.x += PLAYER_SPEED * self.direction.x * time
        self.rect.x = round(self.position.x)

        # Restrict movement
        self.rect.clamp_ip(pg.Rect((0,0), canvas_size))

        # Reset the movement
        self.direction = pg.Vector2()

    def render(self):
        pg.draw.rect(self.canvas, self.color, self.rect)