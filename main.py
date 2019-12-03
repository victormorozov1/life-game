import pygame
from board import *
from constants import *
import copy


class Life(Game):
    def __init__(self, birth=(3, 4), live=(2, 4), sleep_time=1, margin=1):
        super().__init__(n, n, sz, sz, [(255, 255, 255), (0, 0, 0)], sleep_time=sleep_time, margin=margin)
        self.birth = birth
        self.live = live
        print(self.live, self.birth)

    def handle_event(self, ev):
        if ev.type == pygame.MOUSEBUTTONDOWN:
            self.board.cells[ev.pos[0] // self.board.sz][ev.pos[1] // self.board.sz].click()
        elif ev.type == pygame.KEYDOWN:
            print('space pressed')
            if ev.key == pygame.K_SPACE:
                self.pause = (self.pause + 1) % 2

    def number_of_living_around(self, x, y):
        ret = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i != 0 or j != 0:
                    ret += self.board2[(x + i + self.board.n) % self.board.n][(y + j + self.board.m) % self.board.m]
        return ret

    def game_iteration(self):
        self.board2 = self.board.get_arr()

        for i in range(len(self.board.cells)):
            for j in range(len(self.board.cells[i])):
                nola = self.number_of_living_around(i, j)
                if self.board.cells[i][j].clicked % 2:  # alive
                    if nola not in range(*self.live):
                        self.board.cells[i][j].click()
                else:
                    if nola in range(*self.birth):
                        self.board.cells[i][j].click()


if __name__ == '__main__':
    game = Life(sleep_time=0, margin=0)
    game.run()
