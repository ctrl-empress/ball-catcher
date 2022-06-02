import time
import pygame as pg
from config import *
from player import Player
from ball import Ball
from random import Random
from hud import HUD


class World:
    def __init__(self, canvas: pg.Surface):
        self.balls: Ball = []
        self.canvas = canvas
        self.spawn_timer = time.time()
        self.hud = HUD(canvas)
        # Create the player
        self.player = None
        self.make_player()
        self.score = 0

    def make_player(self):
        color = pg.Color(255, 0, 0)
        size = pg.Vector2(50, 15)
        canvas_size = self.get_canvas_size()
        bottom_offset = 50

        # Position the player near the bottom part of the screen
        position = pg.Vector2((canvas_size.x / 2) - (size.x / 2),
                              canvas_size.y - bottom_offset)

        self.player = Player(self.canvas, color, size, position)

    def spawn_ball(self):
        rand = Random()
        color = pg.Color(0, 0, 0)
        color.r = rand.randint(0, 255)
        color.g = rand.randint(0, 255)
        color.b = rand.randint(0, 255)
        size = rand.randint(10, 25)
        pos = pg.Vector2()
        pos.x = rand.randint(0 + size, self.get_canvas_size().x - size)
        pos.y = 0
        ball = Ball(self.canvas, color, pos, size)
        self.balls.append(ball)
        
    def get_canvas_size(self):
        return pg.Vector2(self.canvas.get_size())

    def handle_events(self):
        key = pg.key.get_pressed()
        # Move the player
        if key[pg.K_LEFT]:
            self.player.move(self.player.LEFT)
        if key[pg.K_RIGHT]:
            self.player.move(self.player.RIGHT)

    def update(self, frame_time):
        self.player.update(frame_time)

        # process the timer
        this_time = time.time()
        delta_time = this_time - self.spawn_timer

        # spawn a ball for every n second
        if delta_time >= SPAWN_TIME:
            self.spawn_ball()
            self.spawn_timer = this_time

        if len(self.balls) > 0:
            for ball in self.balls:
                ball.update(frame_time)
                self.player.catch(ball)

        self.hud.update(self.player.get_catch())
         
    def render(self):
        self.player.render()

        if len(self.balls) > 0:
            for ball in self.balls:
                ball.render()

        self.hud.render()

    def cleanup(self):
        for count, item in enumerate(self.balls):
            if item.is_to_delete():
                del self.balls[count]