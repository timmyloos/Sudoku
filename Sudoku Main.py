import pygame
import sys
from Board import Board
from sudoku_generator import SudokuGenerator


def game_start():
    font_title = pygame.font.Font(None, 100)
    font_button = pygame.font.Font(None, 40)

    easy_rect = pygame.Rect(100, 750, 125, 50)
    medium_rect = pygame.Rect(387.5, 750, 125, 50)
    hard_rect = pygame.Rect(675, 750, 125, 50)

    while True:

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    return('easy')
                if medium_rect.collidepoint(event.pos):
                    return('medium')
                if hard_rect.collidepoint(event.pos):
                    return('hard')

        title_surface = font_title.render("Welcome to Sudoku", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(450, 250))
        screen.blit(title_surface, title_rect)

        easy_button_surface = font_button.render('Easy', True, (255, 255, 255))
        easy_button_rect = easy_button_surface.get_rect(center=easy_rect.center)
        pygame.draw.rect(screen, (255, 255, 255), easy_rect, 2)  # Draw button outline
        screen.blit(easy_button_surface, easy_button_rect)

        medium_button_surface = font_button.render('Medium', True, (255, 255, 255))
        medium_button_rect = medium_button_surface.get_rect(center=medium_rect.center)
        pygame.draw.rect(screen, (255, 255, 255), medium_rect, 2)  # Draw button outline
        screen.blit(medium_button_surface, medium_button_rect)

        hard_button_surface = font_button.render('Hard', True, (255, 255, 255))
        hard_button_rect = easy_button_surface.get_rect(center=hard_rect.center)
        pygame.draw.rect(screen, (255, 255, 255), hard_rect, 2)  # Draw button outline
        screen.blit(hard_button_surface, hard_button_rect)

        pygame.display.flip()


def game_win():
    font_title = pygame.font.Font(None, 100)
    font_button = pygame.font.Font(None, 40)

    rect = pygame.Rect(387.5, 750, 125, 50)

    while True:

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()

        title_surface = font_title.render("Game Won!", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(450, 250))
        screen.blit(title_surface, title_rect)

        button_surface = font_button.render('Exit', True, (255, 255, 255))
        button_rect = button_surface.get_rect(center=rect.center)
        pygame.draw.rect(screen, (255, 255, 255), rect, 2)  # Draw button outline
        screen.blit(button_surface, button_rect)

        pygame.display.flip()


def game_lost():
    board.reset_to_original()
    board.draw()
    pygame.display.flip()

    font_title = pygame.font.Font(None, 100)
    font_button = pygame.font.Font(None, 40)

    restart_rect = pygame.Rect(300, 750, 200, 50)
    exit_rect = pygame.Rect(550, 750, 200, 50)

    def draw_button(rect, text, active=False):
        color = (255, 200, 200) if active else (255, 255, 255)
        pygame.draw.rect(screen, color, rect, 0)  # Solid fill
        pygame.draw.rect(screen, (255, 255, 255), rect, 2)  # White border
        button_surface = font_button.render(text, True, (0, 0, 0))
        button_rect = button_surface.get_rect(center=rect.center)
        screen.blit(button_surface, button_rect)

    def restart_game():
        pygame.init()
        screen = pygame.display.set_mode((900, 1000))
        pygame.display.set_caption("Sudoku Game")

        difficulty = game_start()
        board = Board(9, 9, screen, difficulty)
        game = None
        selected_cell = None
        selected_value = None
        prev_click = None
        board.update_board()

    while True:
        screen.fill((0, 0, 0))

        title_surface = font_title.render("Game Over", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(450, 250))
        screen.blit(title_surface, title_rect)

        mx, my = pygame.mouse.get_pos()
        draw_button(restart_rect, 'Restart', restart_rect.collidepoint((mx, my)))
        draw_button(exit_rect, 'Exit', exit_rect.collidepoint((mx, my)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rect.collidepoint(event.pos):
                    board.reset_to_original()
                    board.draw()
                    pygame.display.flip()
                    continue
                elif restart_rect.collidepoint(event.pos):
                    restart_game()
                    return True

                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((900, 1000))
    pygame.display.set_caption("Sudoku Game")

    difficulty = game_start()
    board = Board(9, 9, screen, difficulty)
    game = None
    selected_cell = None
    selected_value = None
    prev_click = None
    board.update_board()

    while True:

        while True:

                screen.fill((255, 255, 255))

                board.draw()

                font_button = pygame.font.Font(None, 40)

                reset_rect = pygame.Rect(100, 925, 125, 50)
                restart_rect = pygame.Rect(387.5, 925, 125, 50)
                quit_rect = pygame.Rect(675, 925, 125, 50)

                reset_button_surface = font_button.render('Reset', True, (0, 0, 0))
                reset_button_rect = reset_button_surface.get_rect(center=reset_rect.center)
                pygame.draw.rect(screen, (0, 0, 0), reset_rect, 2)  # Draw button outline
                screen.blit(reset_button_surface, reset_button_rect)

                restart_button_surface = font_button.render('Restart', True, (0, 0, 0))
                restart_button_rect = restart_button_surface.get_rect(center=restart_rect.center)
                pygame.draw.rect(screen, (0, 0, 0), restart_rect, 2)  # Draw button outline
                screen.blit(restart_button_surface, restart_button_rect)

                quit_button_surface = font_button.render('Quit', True, (0, 0, 0))
                quit_button_rect = quit_button_surface.get_rect(center=quit_rect.center)
                pygame.draw.rect(screen, (0, 0, 0), quit_rect, 2)  # Draw button outline
                screen.blit(quit_button_surface, quit_button_rect)

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        clicked_cell = board.click_cell(pos[0], pos[1])
                        click_position = board.click(pos[0], pos[1])

                        if click_position:
                            selected_cell = board.select(click_position[0], click_position[1])

                        if clicked_cell:
                            clicked_cell.clicked = not clicked_cell.clicked
                            if prev_click:
                                prev_click.clicked = False
                            prev_click = clicked_cell

                        if reset_rect.collidepoint(event.pos):
                            board.reset_to_original()
                            board.draw()
                            pygame.display.flip()
                            continue

                        elif restart_rect.collidepoint(event.pos):
                                pygame.init()
                                screen = pygame.display.set_mode((900, 1000))
                                pygame.display.set_caption("Sudoku Game")

                                difficulty = game_start()
                                board = Board(9, 9, screen, difficulty)
                                game = None
                                selected_cell = None
                                selected_value = None
                                prev_click = None
                                board.update_board()

                        elif quit_rect.collidepoint(event.pos):
                            pygame.quit()

                    elif event.type == pygame.KEYDOWN:
                        if selected_cell:
                            if event.key == pygame.K_RETURN:
                                board.place_number(selected_value)
                                board.sketch("")
                            elif event.key == pygame.K_BACKSPACE:
                                board.clear()
                            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                               pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                                selected_value = int(event.unicode)
                                board.sketch(int(event.unicode))

                if board.is_full():
                    if board.check_board():
                        game_win()
                        break
                    else:
                        game_lost()
                        break
