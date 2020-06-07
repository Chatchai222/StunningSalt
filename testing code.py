import pygame
import sys
from color import Color
from player import Player
from player import PlayerRed, PlayerBlu, Ball, BorderTop, BorderBottom
from screen import Screen


pygame.init()
# Player and Rect data
redplayer = PlayerRed()
bluplayer = PlayerBlu()
ball = Ball()
topborder = BorderTop()
bottomborder = BorderBottom()

# Screen data
screen = Screen()

# The game itself
game_over = False
while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        redplayer.player_movement_input(event)
        bluplayer.player_movement_input(event)

    redplayer.update_movement()
    bluplayer.update_movement()
    ball.update_movement(redplayer, bluplayer, topborder, bottomborder, screen)

    screen.update_screen(redplayer, bluplayer, ball, topborder, bottomborder)
    pygame.display.update()
