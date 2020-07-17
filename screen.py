from color import Color
import pygame
from player import Player, PlayerBlu, PlayerRed

# This is class for the screen of pygame project pong
class Screen:
    def __init__(self, width=1000, height=500, background_color=Color.BLACK, font_type="monospace", font_size=35, clock_tick=30):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width,height))
        self.font = pygame.font.SysFont(font_type, font_size)
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick

    def refresh_background(self):
        self.screen.fill(self.background_color)

    def draw_player(self, player):
        player.draw(self.screen)

    def draw_ball(self, ball):
        ball.draw(self.screen)

    def draw_border(self, border):
        border.draw(self.screen)

    # The score_label the '1' in the second argument is orientation of text
    def draw_score_label(self, redplayer, bluplayer, color=Color.YELLOW):
        score_text = str(redplayer.score) + ':' + str(bluplayer.score)
        score_label = self.font.render(score_text, 1, color)
        self.screen.blit(score_label, (self.width/2 - 20, self.height/20 - 20))

    def player_wins(self, redplayer, bluplayer, goal=3):
        if redplayer.score >= goal or bluplayer.score >= goal:
            return True

    def tell_who_wins(self, redplayer, bluplayer):
        # The setting of go up and down is to prevent the bug of not receiving command to start game fresh
        if redplayer.score > bluplayer.score:
            redplayer.score = 0
            bluplayer.score = 0
            redplayer.go_up = False
            redplayer.go_down = False
            bluplayer.go_up = False
            bluplayer.go_down = False
            return 'Red'
        if bluplayer.score > redplayer.score:
            redplayer.score = 0
            bluplayer.score = 0
            redplayer.go_up = False
            redplayer.go_down = False
            bluplayer.go_up = False
            bluplayer.go_down = False
            return 'Blue'

    # This updates the screen with all the rect, score and the clock
    def update_screen(self, redplayer, bluplayer, ball, topborder, bottomborder):
        self.refresh_background()
        self.draw_player(redplayer)
        self.draw_player(bluplayer)
        self.draw_ball(ball)
        self.draw_border(topborder)
        self.draw_border(bottomborder)
        self.draw_score_label(redplayer, bluplayer, color=Color.YELLOW)

        self.clock.tick(self.clock_tick)
        pygame.display.update()












