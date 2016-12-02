# josh dickey 11/30/16
# this project creates a pyramid of different colored blocks

import pygame, sys, brick
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("pyramid")

main_surface.fill((255, 255, 255))

number_bricks = 9
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
colors = [BLUE, RED, GREEN, YELLOW, ORANGE]
SPACE = 5
# this formula determines brick width by number of bricks, spaces, and screen size
BRICK_WIDTH = (main_surface.get_width() - (number_bricks + 1) * SPACE) / number_bricks
BRICK_HEIGHT = 20
x_pos = SPACE
y_pos = (main_surface.get_height() - BRICK_HEIGHT) # first row of bricks is on the bottom of the screen

for y in range (5):
    x_pos = (SPACE * y) + (BRICK_WIDTH * y) # this creates indent for each row
    for x in range (number_bricks):
        # creates different color rows of bricks
        my_brick = brick.Brick(main_surface, BRICK_HEIGHT, BRICK_WIDTH, colors[y])
        my_brick.draw(x_pos, y_pos)
        x_pos = x_pos + BRICK_WIDTH + SPACE # this moves brick position
    y_pos = y_pos - (SPACE + BRICK_HEIGHT) # moves brick position to next row
    number_bricks = number_bricks - 2 # number of bricks in next row





pygame.display.update()



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
