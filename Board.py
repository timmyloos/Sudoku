import pygame
from sudoku_generator import generate_sudoku
from sudoku_generator import SudokuGenerator
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(self.width, {'easy': 30, 'medium': 40, 'hard': 50}[self.difficulty])
        self.original_board = [row[:] for row in self.board]
        self.cells = [[Cell(row, col, self.screen, original=(self.board[row][col] != 0)) for col in range(self.width)] for row in range(self.height)]
        self.selected_cell = None

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()
        self.draw_grid()

    def draw_grid(self):
        for i in range(1, self.width // 3):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 300, 0), (i * 300, self.height * 100), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 300), (self.width * 100, i * 300), 5)

    def get_cell(self, row, col):
        return self.cells[row][col]

    def select(self, row, col):
        self.selected_cell = (row, col)
        return self.selected_cell

    def click(self, x, y):
        for row in range(self.width):
            for col in range(self.height):
                cell = self.cells[row][col]
                if (
                    col * cell.width <= x < (col + 1) * cell.width
                    and row * cell.height <= y < (row + 1) * cell.height
                ):
                    self.selected_cell = (row, col)
                    return row, col
        return None

    def click_cell(self, x, y):
        cell_width = self.cells[0][0].width
        cell_height = self.cells[0][0].height

        row = y // cell_height
        col = x // cell_width

        if 0 <= row < self.height and 0 <= col < self.width:
            return self.cells[row][col]
        else:
            return None

    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].set_cell_value(0)

    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            selected_cell = self.cells[row][col]
            if selected_cell.original:
                return
            selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            selected_cell = self.cells[row][col]
            if selected_cell.original:
                return
            selected_cell.set_cell_value(value)
            self.board[row][col] = value  # Ensure the main board array is updated
            print(f"Updated board at ({row}, {col}) to {value}")

    def reset_to_original(self):
        for row in range(self.height):
            for col in range(self.width):
                original_value = self.original_board[row][col]
                self.cells[row][col].set_cell_value(original_value)
                self.board[row][col] = original_value  # reset gameplay board as well
        print("Board reset to original configuration.")

    def is_full(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col].get_cell_value() == 0:
                    return False
        return True

    def update_board(self):
        for row in range(self.width):
            for col in range(self.height):
                cell_value = self.board[row][col]
                self.cells[row][col].set_cell_value(cell_value)


    def find_empty(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == 0:
                    return row, col
        return None

    def check_board(self):
        print("Checking board validity...")
        for row in range(self.height):
            row_values = self.get_row(row)
            print(f"Row {row}: {row_values}")
            if not self.is_valid_group(row_values):
                print(f"Row {row} is invalid.")
                return False

        for col in range(self.width):
            col_values = self.get_col(col)
            print(f"Column {col}: {col_values}")
            if not self.is_valid_group(col_values):
                print(f"Column {col} is invalid.")
                return False

        for row_start in range(0, self.height, 3):
            for col_start in range(0, self.width, 3):
                box_values = self.get_box(row_start, col_start)
                print(f"Box starting at ({row_start}, {col_start}): {box_values}")
                if not self.is_valid_group(box_values):
                    print(f"Box starting at ({row_start}, {col_start}) is invalid.")
                    return False

        print("All checks passed. Board is valid.")
        return True

    def get_row(self, row):
        return self.board[row]

    def get_col(self, col):
        return [self.board[row][col] for row in range(self.height)]

    def get_box(self, row_start, col_start):
        box_values = []
        for i in range(3):
            for j in range(3):
                box_values.append(self.board[row_start + i][col_start + j])
        return box_values

    def is_valid_group(self, group):
        seen = set()
        for value in group:
            if value == 0:
                continue
            if value in seen:
                return False
            seen.add(value)
        return True
