import pygame as pg
from config import *

class HUD:
    FONT_SIZE = 25
    PADDING = 5
    HEADER_HEIGHT = 40

    def __init__(self, canvas: pg.Surface):
        self.canvas = canvas
        self.elements = []

        self.font = pg.font.SysFont(FONT, self.FONT_SIZE)
        
        # score
        self.score: pg.Surface = None
        self.score_rect = pg.Rect(0, 0, 0, 0)

        # header
        self.header_color = pg.Color(153, 204, 255)
        self.header = pg.Rect(0, 0, WIDTH, self.HEADER_HEIGHT)

    def update(self, score):
        # update score
        self.score = self.font.render(str(score), True, COLORS['black'])

        self.score_rect.centerx = WIDTH / 2

    def render(self):
        pg.draw.rect(self.canvas, self.header_color, self.header)
        
        if self.score is not None:
            self.canvas.blit(self.score, self.score_rect)