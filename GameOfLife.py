import pygame
from random import randint
from copy import deepcopy

class Cell:

    def __init__(self, TILE, WIDTH, HEIGHT):
        self.TILE = TILE
        self.W = WIDTH // self.TILE
        self.H = HEIGHT // self.TILE

    def check_cell(self, current_field, x, y):
        count = 0
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if (j >= 0 and j < self.H) and (i >= 0 and i < self.W):
                    if current_field[j][i]:
                        count += 1

        if current_field[y][x]:
            count -= 1
            if count == 2 or count == 3:
                return 1
            return 0
        else:
            if count == 3:
                return 1
            return 0

    pass

class Surface:

    def __init__(self, WIDTH, HEIGHT, FPS):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.FPS = FPS
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

    def draw_grid(self, TILE):
        [pygame.draw.line(self.surface, pygame.Color('dimgray'), (x, 0), (x, self.HEIGHT)) for x in range(0, self.WIDTH, TILE)]
        [pygame.draw.line(self.surface, pygame.Color('dimgray'), (0, y), (self.WIDTH, y)) for y in range(0, self.HEIGHT, TILE)]

    pass

class Game:

    pygame.init()

    def __init__(self, WIDTH, HEIGHT, FPS, TILE, current_field):
        self.surface = Surface(WIDTH, HEIGHT, FPS)
        self.cell = Cell(TILE, self.surface.WIDTH,  self.surface.HEIGHT)
        self.next_field = [[0 for i in range(self.cell.W)] for j in range(self.cell.H)]
        self.current_field = current_field

    def run(self):
        while True:
            self.surface.surface.fill(pygame.Color('black'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit

            # self.surface.surface.draw_grid(TILE)      
  
            # draw life
            for x in range(self.cell.W):
                for y in range(self.cell.H):
                    if self.current_field[y][x]:
                        pygame.draw.rect(self.surface.surface, pygame.Color('forestgreen'), (x * self.cell.TILE + 2, y * self.cell.TILE + 2, self.cell.TILE - 2, self.cell.TILE - 2))
                    self.next_field[y][x] = self.cell.check_cell(self.current_field, x, y)

            self.current_field = deepcopy(self.next_field)

            pygame.display.flip()
            self.surface.clock.tick(self.surface.FPS)

    pass

WIDTH = 1600
HEIGHT = 900
FPS = 10
TILE = 20

game = Game(WIDTH, HEIGHT, FPS, TILE, [[randint(0, 1) for i in range (WIDTH // TILE)] for j in range(HEIGHT // TILE)])

game.run()