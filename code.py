import pygame
import os
import sys

class Board:
    def __init__(self):
        self.width = 7
        self.height = 7
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 50
        self.cell_size = 100

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    
    def render(self, screen):
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                x1 = self.left + self.cell_size * i
                y1 = self.top + self.cell_size * j
                w, h = self.cell_size, self.cell_size
                pygame.draw.rect(screen, (255, 255, 255), ((x1, y1), (w, h)), 1)
    
    def get_cell(self, mouse_pos):
        if (self.left <= mouse_pos[0] <= self.left + self.width * self.cell_size and
            self.top <= mouse_pos[1] <= self.top + self.height * self.cell_size):
                x = (mouse_pos[0] - self.left) // self.cell_size
                y = (mouse_pos[1] - self.top) // self.cell_size
                return (x, y)
    
    def on_click(self, cell_coords):
        if cell_coords:
            x, y = cell_coords
            self.board[y][x] = (self.board[y][x] + 1) % 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
    


class Hall(Board):
    def __init__(self):
        super().__init__()
        
    
    def open_cell(self, i, j):
        if self.board[j][i] == -1:
            self.board[j][i] = self.vecinos(j, i)[1]
            if self.board[j][i] == 0:
                for cord in self.vecinos(j, i)[0]:
                    self.open_cell(cord[1], cord[0])
    
    def vecinos(self, i, j):
        al_vars = [(i + 1, j), (i + 1, j + 1), (i + 1, j - 1), (i, j + 1),
                   (i, j - 1), (i - 1, j + 1), (i - 1, j), (i - 1, j - 1)]
        res = []
        num = 0
        for var in al_vars:
            if 0 <= var[0] < len(self.board) and 0 <= var[1] < len(self.board[0]):
                res.append((var[0], var[1]))
                if self.board[var[0]][var[1]] == 10:
                    num += 1
        return res, num


class Bedroom(Board):
    def __init__(self):
        super().__init__()
    
    def render():
        pass


class Corridor(Board):
    def __init__(self):
        super().__init__()
    
    def render():
        pass


class Bathroom(Board):
    def __init__(self):
        super().__init__()
    
    def render():
        pass


class Kitchen(Board):
    def __init__(self):
        super().__init__()
    
    def render():
        pass


class Livingroom(Board):
    def __init__(self):
        super().__init__()
    
    def render():
        pass


class Store(Board):
    def __init__(self):
        super().__init__()
    
    def render():
        pass


class Start:
    def __init__(self):
        font = pygame.font.Font(None, w - 5)
        text = font.render(str(self.board[j][i]), True, (0, 255, 0))
        screen.blit(text, (x1 + 3, y1 + 3))


class Finish:
    def __init__(self):
        pass


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


pygame.init()
pygame.display.set_caption('Суслик: остаться в живых 2')
size = width, height = 7 * 100, 7 * 100 + 50
screen = pygame.display.set_mode(size)
hall, bedroom, corridor, bathroom = Hall(), Bedroom(), Corridor(), Bathroom()
kitchen, livingroom, store, start, finish = Kitchen(), Livingroom(), Store(), Start(), Finish()
rooms = [start, finish, hall, bedroom, corridor, bathroom, kitchen, livingroom, store]
for room in rooms[2:]:
    room.set_view(0, 50, 100)
running = True
play = False
room = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            try:
                x, y = board_life.get_cell(event.pos)
                board_life.open_cell(x, y)
            except Exception:
                pass
    screen.fill((255, 255, 255))
    board_life.render(screen)
    pygame.display.flip()