import pygame
from constants import *
import copy


class Board:
    def __init__(self, n, m, sz, cell, win, cell_colors, margin=1, grid_color=(255, 255, 255)):
        self.n = n
        self.m = m
        self.sz = sz
        self.margin = margin
        self.grid_color = grid_color
        self.Cell = cell
        self.cells = [[self.Cell(cell_colors) for i in range(m)] for j in range(n)]
        self.win = win
        self.cell_colors = cell_colors
        self.cell = cell

    def show(self):
        for i in range(self.n):
            for j in range(self.m):
                pygame.draw.rect(self.win, self.grid_color,
                                 (i * self.sz, j * self.sz, self.sz, self.sz))
                self.cells[i][j].draw(self.win,
                                      (i * self.sz + self.margin, j * self.sz + self.margin,
                                       self.sz - 2 * self.margin, self.sz - 2 * self.margin))
        pygame.display.update()

    def get_arr(self):
        ret = []
        for i in self.cells:
            ret.append([])
            for j in i:
                ret[-1].append(j.clicked % 2)
        return ret

    def __str__(self):
        ret = ''
        for i in self.cells:
            for j in i:
                ret += str(j.clicked % 2)
            ret += '\n'
        return ret


class Cell:
    def __init__(self, colors):
        self.clicked = 0
        self.colors = colors
        self.color = self.colors[self.clicked]

    def click(self):
        self.clicked += 1
        self.color = self.colors[self.clicked % len(self.colors)]

    def draw(self, win, tpl):
        pygame.draw.rect(win, self.color, tpl)

    def copy(self):
        ret = Cell(self.colors)
        ret.clicked = self.clicked
        ret.color = ret.colors[self.clicked]
        return ret


class Game:
    def __init__(self, nx, ny, szx, szy, cell_colors, cell=Cell, sleep_time=1, margin=0):
        pygame.init()
        self.win = pygame.display.set_mode((nx * szx, ny * szy))
        self.board = Board(nx, ny, szx, cell, self.win, cell_colors, margin=margin, grid_color=(188, 188, 188))
        self.sleep_time = sleep_time
        self.pause = 1

    def handle_event(self, ev):
        if ev.type == pygame.MOUSEBUTTONDOWN:
            self.board.cells[ev.pos[0] // self.board.sz][ev.pos[1] // self.board.sz].click()

    def handle_events(self):
        for i in pygame.event.get():
            self.handle_event(i)
            self.event_quit(i)

    def event_quit(self, ev):
        if ev.type == pygame.QUIT:
            exit()

    def game_iteration(self):
        pass

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            if not self.pause:
                # print('game iteration')
                self.game_iteration()
            self.board.show()
            pygame.time.wait(self.sleep_time)
