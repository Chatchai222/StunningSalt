import pygame
from color import Color
import random


class Player(pygame.Rect):
    def __init__(self, x, y, xsize=25, ysize=100, color=Color.GREY, speed=3, score=0, go_up=False, go_down=False):
        super().__init__(x, y, xsize, ysize)
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.speed = speed
        self.score = score
        self.color = color
        self.go_up = go_up
        self.go_down = go_down
        self.rect = [self.x, self.y, self.xsize, self.ysize]

    # Old way of drawing
    def _draw(self, screen):
        self.rect = [self.x, self.y, self.xsize, self.ysize]
        pygame.draw.rect(screen, self.color, self.rect)

    # The draw method in the last column for 'self' has the attribute for a rect (so its ok)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)

# The redplayer on the left handside of the screen
class PlayerRed(Player):
    def __init__(self, x=100, y=300, xsize=25, ysize=100, speed=5, score=0, color=Color.RED, go_up=False, go_down=False):
        super().__init__(x, y, xsize, ysize, color, speed, score, go_up, go_down)

    # Takes input from event to state if player is moving up or down
    def player_movement_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.go_up = True

            if event.key == pygame.K_s:
                self.go_down = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.go_up = False

            if event.key == pygame.K_s:
                self.go_down = False

    # Update the x and y position based on if they are currently going up or down
    def update_movement(self):
        if self.go_up:
            self.y -= self.speed
        if self.go_down:
            self.y += self.speed

# The blu player on the right handside of the screen
class PlayerBlu(Player):
    def __init__(self, x=875, y=100, xsize=25, ysize=100, speed=5, score=0, color=Color.BLUE, go_up=False, go_down=False):
        super().__init__(x, y, xsize, ysize, color, speed, score, go_up, go_down)

    def player_movement_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.go_up = True

            if event.key == pygame.K_DOWN:
                self.go_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.go_up = False

            if event.key == pygame.K_DOWN:
                self.go_down = False

    def update_movement(self):
        if self.go_up:
            self.y -= self.speed
        if self.go_down:
            self.y += self.speed


class Border(pygame.Rect):
    def __init__(self, x, y, xsize, ysize, color=Color.GREY):
        super().__init__(x, y, xsize, ysize)
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)

class BorderTop(Border):
    def __init__(self, x=0, y=0, xsize=1000, ysize=50, color=Color.GREY):
        super().__init__(x, y, xsize, ysize, color)

class BorderBottom(Border):
    def __init__(self, x=0, y=450, xsize=1000, ysize=50, color=Color.GREY):
        super().__init__(x, y, xsize, ysize, color)


class Ball(pygame.Rect):
    def __init__(self, x=490, y=240, xsize=20, ysize=20, speed=4, yvel=5, collision=0, color=Color.WHITE):
        super().__init__(x, y, xsize, ysize)
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.speed = speed
        self.yvel = yvel
        self.color = color
        self.collision = collision
        self.xvel = self.speed + self.collision

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)

    # Just to note I don't know how to reflect a ball (as collision between Rect have no direction, you just know it
    # collide but don't know the direction it collided)

    # So I just hard coded it for each individual thing to reflect
    def collide_red_player(self, redplayer):
        if self.colliderect(redplayer):
            self.collision += 1
            self.x += abs(self.xvel) + 3
            self.xvel = abs(self.speed + self.collision)
            self.yvel = random.randint(-5, 5)

    def collide_blu_player(self, bluplayer):
        if self.colliderect(bluplayer):
            self.collision += 1
            self.x -= abs(self.xvel) + 3
            self.xvel = -abs(self.speed + self.collision)
            self.yvel = random.randint(-5, 5)

    def collide_border_top(self, border):
        if self.colliderect(border):
            self.y += abs(self.yvel) + 3
            self.yvel = abs(self.yvel)

    def collide_border_bottom(self, border):
        if self.colliderect(border):
            self.y -= abs(self.yvel) + 3
            self.yvel = -abs(self.yvel)

    # Update the position of the ball according to the veloctiy
    def moving_ball(self):
        self.x += self.xvel
        self.y += self.yvel

    # This will give points to the player and reset the ball speed and collision and send it to middle of screen
    def give_point_to_player(self, redplayer, bluplayer, screen):
        # Red player gets a point
        if self.x > screen.width:
            redplayer.score += 1
            self.collision = 0
            self.xvel = 3
            self.x = screen.width/2

        # Blu player gets a point
        if self.x < 0:
            bluplayer.score += 1
            self.collision = 0
            self.xvel = -3
            self.x = screen.width/2

    # Putting all the functions together
    def update_movement(self, redplayer, bluplayer, topborder, bottomborder, screen):
        self.collide_red_player(redplayer)
        self.collide_blu_player(bluplayer)
        self.collide_border_top(topborder)
        self.collide_border_bottom(bottomborder)
        self.give_point_to_player(redplayer, bluplayer, screen)
        self.moving_ball()













