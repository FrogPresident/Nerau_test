import pygame
import button

# initializing the constructor
pygame.init()
# screen width & height
screen_width = 800
screen_height = 600

# screen resolution
res = (screen_width, screen_height)

# open up a window
screen = pygame.display.set_mode(res)
background = pygame.image.load('white_background.jpg')
pygame.display.set_caption('NeRaU')

# game mode textview
target_sum_font = pygame.font.Font(None, 54)
target_sum_text = "Target Sum"
target_speed_font = pygame.font.Font(None, 54)
target_speed_text = "Target Speed"


# button image
start_img = pygame.image.load('image/start_btn.png').convert_alpha()
quit_img = pygame.image.load('image/exit_btn.png').convert_alpha()


class GameMode:
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        start_button = button.Button(screen_width / 2 - 130, screen_height / 2 - 150, start_img, 1)
        quit_button = button.Button(screen_width / 2 - 110, screen_height / 2, quit_img, 1)
        screen.blit(background, (0, 0))
        if start_button.draw(screen):
            self.state = 'set_mode'

        if quit_button.draw(screen):
            pygame.quit()

        pygame.display.flip()

    def set_mode(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        sum_surface = target_sum_font.render(target_sum_text, True, (255, 255, 255))
        speed_surface = target_speed_font.render(target_speed_text, True, (255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(sum_surface, (screen_width / 2 - 250, screen_height / 2 - 150))
        screen.blit(speed_surface, (screen_width / 2 - 250, screen_height / 2))
        pygame.display.flip()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(background, (0, 0))
        pygame.display.flip()

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "set_mode":
            self.set_mode()
        if self.state == "main_game":
            self.main_game()


# the menu page switch
game_mode = GameMode()

while True:
    game_mode.state_manager()
    pygame.display.update()
