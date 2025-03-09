import pygame

FONT_BIG = None
FONT_SMALL = None

def initialize_fonts():
    global FONT_BIG, FONT_SMALL
    FONT_BIG = pygame.font.Font(None, 36)
    FONT_SMALL = pygame.font.Font(None, 25)

class Cell:
    def __init__(self, row, col, screen, original=False):
        self.row = row
        self.col = col
        self.screen = screen
        self.width = 100
        self.height = 100
        self.value = 0
        self.sketched_value = ""
        self.clicked = False
        self.original = original

    def set_cell_value(self, value):
            self.value = value

    def get_cell_value(self):
        return self.value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * self.width
        y = self.row * self.height

        # ensure fonts are initialized
        if FONT_BIG is None or FONT_SMALL is None:
            initialize_fonts()

        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x, y, self.width, self.height), 2)

        if self.value != 0:
            text = FONT_BIG.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + self.width // 2, y + self.height // 2))
            self.screen.blit(text, text_rect)

        if self.sketched_value:
            sketched_text = FONT_SMALL.render(str(self.sketched_value), True, (175, 175, 175))
            self.screen.blit(sketched_text, (x + 5, y + 5))

        if self.clicked:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(x, y, self.width, self.height), 4) 
