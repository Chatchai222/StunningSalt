# This code is for the game of pong
import pygame
import random
import sys

pygame.init()

HEIGHT = 500
WIDTH = 1000


# Color in RGB
RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
GREY = (192,192,192)
BLACK = (0,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

# The players data
redplayer_pos = [100, 300]
redplayer_change_in_y = 0
redplayer_size = [25,100]
redplayer_score = 0
rp_go_up = False
rp_go_down = False



bluplayer_pos = [875,100]
bluplayer_change_in_y = 0
bluplayer_size = [25,100]
bluplayer_score = 0
bp_go_up = False
bp_go_down = False

player_speed = 10



# The ball data
ball_pos = [490, 240]
ball_change_in_pos = [-3,3]
ball_size = [20,20]
ball_collision = 0


# Border data
topborder_pos = [0,0]
topborder_size = [1000,50]

bottomborder_pos = [0,450]
bottomborder_size = [1000,50]


# Screen data
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
game_over = False




while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Control the red player rate of change in y pos
            if event.key == pygame.K_s:
                rp_go_down = True
            if event.key == pygame.K_w:
                rp_go_up = True

            # Control the blu player rate of change in y pos
            if event.key == pygame.K_UP:
                bp_go_up = True
            if event.key == pygame.K_DOWN:
                bp_go_down = True


        # Stop player from moving after releasing button
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                rp_go_up = False

            if event.key == pygame.K_s:
                rp_go_down = False

            if event.key == pygame.K_UP:
                bp_go_up = False

            if event.key == pygame.K_DOWN:
                bp_go_down = False

    # Updating the variable (I dont know why stuff dont update when I change its dependent variable?)
    score_font = pygame.font.SysFont("monospace", 35)
    score_text = str(redplayer_score) + ':' + str(bluplayer_score)
    score_label = score_font.render(score_text, 1, YELLOW)
    score_pos = [470, 0]

    ball_speed = ball_collision + 3
    # Defining the rectangle of each object

    redplayer_rec = pygame.Rect(redplayer_pos[0], redplayer_pos[1], redplayer_size[0], redplayer_size[1])
    bluplayer_rec = pygame.Rect(bluplayer_pos[0], bluplayer_pos[1], bluplayer_size[0], bluplayer_size[1])
    ball_rec = pygame.Rect(ball_pos[0], ball_pos[1], ball_size[0], ball_size[1])
    topborder_rec = pygame.Rect(topborder_pos[0], topborder_pos[1], topborder_size[0], topborder_size[1])
    bottomborder_rec = pygame.Rect(bottomborder_pos[0], bottomborder_pos[1], bottomborder_size[0], bottomborder_size[1])





    # Update positon for the player red and blu
    if rp_go_up:
        redplayer_pos[1] -= player_speed
    if rp_go_down:
        redplayer_pos[1] += player_speed
    if bp_go_up:
        bluplayer_pos[1] -= player_speed
    if bp_go_down:
        bluplayer_pos[1] += player_speed
        # For preventing player moving into border
    if redplayer_rec.colliderect(topborder_rec):
        redplayer_pos[1] += player_speed
    if redplayer_rec.colliderect(bottomborder_rec):
        redplayer_pos[1] -= player_speed
    if bluplayer_rec.colliderect(topborder_rec):
        bluplayer_pos[1] += player_speed
    if bluplayer_rec.colliderect(bottomborder_rec):
        bluplayer_pos[1] -= player_speed



    # Logic for ball collision
    if ball_rec.colliderect(redplayer_rec):
        ball_collision += 1
        ball_pos[0] += abs(ball_speed) + 3
        ball_change_in_pos[0] = abs(ball_speed)

    if ball_rec.colliderect(bluplayer_rec):
        ball_collision += 1
        ball_pos[0] -= abs(ball_speed) + 3
        ball_change_in_pos[0] = -abs(ball_speed)

    if ball_rec.colliderect(topborder_rec):
        ball_pos[1] += 5
        ball_change_in_pos[1] = ball_change_in_pos[1] * -1

    if ball_rec.colliderect(bottomborder_rec):
        ball_pos[1] -= 5
        ball_change_in_pos[1] = ball_change_in_pos[1] * -1

    # Logic for getting points
    # It also reset the ball collision and speed and update the change in pos
    if ball_pos[0] < 0:  # Blu get a point
        ball_collision = 0
        ball_speed = 0
        ball_change_in_pos[0] = -3
        bluplayer_score += 1
        ball_pos[0] = 500

    if ball_pos[0] > WIDTH:  # Red get a point
        ball_collision = 0
        ball_speed = 0
        ball_change_in_pos[0] = 3
        redplayer_score += 1
        ball_pos[0] = 500

    # Update position of the ball
    ball_pos[0] += ball_change_in_pos[0]
    ball_pos[1] += ball_change_in_pos[1]







    # Drawing the stuff on the screen
    screen.fill(BLACK)


    pygame.draw.rect(screen, GREY, bottomborder_rec)
    pygame.draw.rect(screen, GREY, topborder_rec)
    pygame.draw.rect(screen, WHITE, ball_rec)
    pygame.draw.rect(screen, RED, redplayer_rec)
    pygame.draw.rect(screen, BLUE, bluplayer_rec)
    screen.blit(score_label, score_pos)

    clock.tick(30)
    pygame.display.update()

