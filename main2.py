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
def gameloop():
    game_over = False
    while not game_over:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            redplayer.player_movement_input(event)
            bluplayer.player_movement_input(event)
            
        if screen.player_wins(redplayer, bluplayer, 3):
            winning_menu(screen.tell_who_wins(redplayer, bluplayer))
        redplayer.update_movement(topborder, bottomborder)
        bluplayer.update_movement(topborder, bottomborder)
        ball.update_movement(redplayer, bluplayer, topborder, bottomborder, screen)

        screen.update_screen(redplayer, bluplayer, ball, topborder, bottomborder)



def main_menu():

    class theButton():
        def __init__(self, color, x, y, width, height, text=''):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text

        def draw(self, win, outline=None):
            # Call this method to draw the button on the screen
            if outline:
                pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pygame.font.SysFont('comicsans', 60)
                text = font.render(self.text, 1, (0, 0, 0))
                win.blit(text, (
                self.x + (int(self.width / 2) - int(text.get_width() / 2)), self.y + (int(self.height / 2) - int(text.get_height() / 2))))

        def isOver(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True

            return False

    titlescreen = theButton(Color.GREY, 400, 0, 200, 100, 'PONG!')
    playbutton = theButton(Color.RED, 450, 200, 100, 50, 'Play')
    quitbutton = theButton(Color.RED, 450, 300, 100, 50, 'Quit')
    menuscreen = pygame.display.set_mode((1000,500))
    running = True
    while running:

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton.isOver(pos):
                    print('Clicked a button')
                    gameloop()
                if quitbutton.isOver(pos):
                    print('Quit the game')
                    sys.exit()

        titlescreen.draw(menuscreen)
        playbutton.draw(menuscreen)
        quitbutton.draw(menuscreen)
        pygame.display.update()


def winning_menu(whowins='Showplayerwhowins'):

    class theButton():
        def __init__(self, color, x, y, width, height, text=''):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text

        def draw(self, win, outline=None):
            # Call this method to draw the button on the screen
            if outline:
                pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pygame.font.SysFont('comicsans', 60)
                text = font.render(self.text, 1, (0, 0, 0))
                win.blit(text, (
                self.x + (int(self.width / 2) - int(text.get_width() / 2)), self.y + (int(self.height / 2) - int(text.get_height() / 2))))

        def isOver(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True

            return False

    winningscreen = pygame.display.set_mode((1000,500))
    playerthatwins = theButton(Color.GREY, 400, 0, 200, 50, whowins + str(' Wins!'))
    playagainbutton = theButton(Color.RED, 370, 200, 250, 50, 'Play again')
    quitbutton = theButton(Color.RED, 450, 300, 100, 50, 'Quit')
    running = True
    while running:

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playagainbutton.isOver(pos):
                    gameloop()
                if quitbutton.isOver(pos):
                    sys.exit()

        playagainbutton.draw(winningscreen)
        quitbutton.draw(winningscreen)
        playerthatwins.draw(winningscreen)
        pygame.display.update()

main_menu()





