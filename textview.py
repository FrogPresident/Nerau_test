import pygame


class Textview:
    base_font = pygame.font.Font(None, 32)
    COLOR_INACTIVE = pygame.Color()
    COLOR_ACTIVE = pygame.Color()

    def __init__(self, x, y, height, weight, text=""):
        self.rect = pygame.Rect(x, y, height, weight)
        self.text = text
        self.text_surface = self.base_font.render(text, True, )
