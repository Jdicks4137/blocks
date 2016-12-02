import pygame


class Brick:

    def __init__(self, brick_surface, brick_height, brick_width, brick_color):

        self.brick_surface = brick_surface
        self.brick_height = brick_height
        self.brick_width = brick_width
        self.brick_color = brick_color

    def draw(self, x, y):
        pygame.draw.rect(self.brick_surface, self.brick_color, (x, y, self.brick_width, self.brick_height), 0)