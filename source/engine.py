import sys, time
import pygame as pg
from config import *
from world import World


class Engine:
    def __init__(self):
        self.running = False
        self.canvas = None
        self.world = None
        self.clock = None

        pg.init()

    def stop(self):
        pg.quit()
        sys.exit()

    def start(self):
        # Set up the window
        self.setup()

        # It's now running!
        self.running = True

        # Create the world
        self.world = World(self.canvas)

        # Set the clock
        self.clock = pg.time.Clock()

        last_time = time.time()

        # Game loop
        while self.running:
            dt = time.time() - last_time
            last_time = time.time()

            self.handle_events()
            self.update(dt)
            self.render()
            self.cleanup()

            dt = self.clock.tick(FPS)

        self.stop()

    def setup(self):
        self.canvas = pg.display.set_mode((WIDTH, HEIGHT))
        self.canvas.fill(COLORS['white'])

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        self.world.handle_events()

    def update(self, time):
        self.world.update(time)
        
    def render(self):
        self.canvas.fill(COLORS['white'])
        self.world.render()
        pg.display.update()

    def cleanup(self):
        self.world.cleanup()

if __name__ == "__main__":
    engine = Engine()
    engine.start()