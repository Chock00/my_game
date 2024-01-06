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
        self.screen = pygame.Surface((700, 750))
        self.sprites = pygame.sprite.Group()

        self.sus = pygame.sprite.Group()
        sprite01 = pygame.sprite.Sprite()
        sprite01.image = load_image("suslik.png")
        sprite01.rect = sprite01.image.get_rect()
        sprite01.rect.x = self.coords(0, 6)[0]
        sprite01.rect.y = self.coords(0, 6)[1]
        self.sus.add(sprite01)
        self.pla = pygame.sprite.Group()
        sprite02 = pygame.sprite.Sprite()
        sprite02.image = load_image("player.png")
        sprite02.rect = sprite02.image.get_rect()
        sprite02.rect.x = self.coords(0, 6)[0]
        sprite02.rect.y = self.coords(0, 6)[1]
        self.pla.add(sprite02)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    
    def get_cell(self, mouse_pos):
        if (self.left <= mouse_pos[0] <= self.left + self.width * self.cell_size and
            self.top <= mouse_pos[1] <= self.top + self.height * self.cell_size):
                x = (mouse_pos[0] - self.left) // self.cell_size
                y = (mouse_pos[1] - self.top) // self.cell_size
                return (x, y)  
    
    def coords(self, i, j):
        return i * 100, 50 + j * 100


class Hall(Board):
    def __init__(self):
        super().__init__()
        sprite1 = pygame.sprite.Sprite()
        sprite1.image = load_image("dirt_hall.png")
        sprite1.rect = sprite1.image.get_rect()
        sprite1.rect.x = self.coords(4, 5)[0]
        sprite1.rect.y = self.coords(4, 5)[1]
        self.sprites.add(sprite1)
        sprite2 = pygame.sprite.Sprite()
        sprite2.image = load_image("shoes_hall.jpg")
        sprite2.rect = sprite2.image.get_rect()
        sprite2.rect.x = self.coords(4, 6)[0]
        sprite2.rect.y = self.coords(4, 6)[1]
        self.sprites.add(sprite2)
        sprite3 = pygame.sprite.Sprite()
        sprite3.image = load_image("wordr_hall.jpg")
        sprite3.rect = sprite3.image.get_rect()
        sprite3.rect.x = self.coords(0, 6)[0]
        sprite3.rect.y = self.coords(0, 6)[1]
        self.sprites.add(sprite3)
        sprite4 = pygame.sprite.Sprite()
        sprite4.image = load_image("door.png")
        sprite4.rect = sprite4.image.get_rect()
        sprite4.rect.x = self.coords(3, 6)[0]
        sprite4.rect.y = self.coords(3, 6)[1]
        self.sprites.add(sprite4)
        sprite5 = pygame.sprite.Sprite()
        sprite5.image = load_image("door.png")
        sprite5.rect = sprite5.image.get_rect()
        sprite5.rect.x = self.coords(3, 0)[0]
        sprite5.rect.y = self.coords(3, 0)[1]
        self.sprites.add(sprite5)
        sprite6 = pygame.sprite.Sprite()
        sprite6.image = load_image("door.png")
        sprite6.rect = sprite6.image.get_rect()
        sprite6.rect.x = self.coords(0, 3)[0]
        sprite6.rect.y = self.coords(0, 3)[1]
        self.sprites.add(sprite6)
        sprite7 = pygame.sprite.Sprite()
        sprite7.image = load_image("door.png")
        sprite7.rect = sprite7.image.get_rect()
        sprite7.rect.x = self.coords(6, 2)[0]
        sprite7.rect.y = self.coords(6, 2)[1]
        self.sprites.add(sprite7)
        self.sprites.draw(self.screen)

        
    def open_cell(self, i, j):
        pass


class Bedroom(Board):
    def __init__(self):
        super().__init__()
        sprite1 = pygame.sprite.Sprite()
        sprite1.image = load_image("bed_bed.jpg")
        sprite1.rect = sprite1.image.get_rect()
        sprite1.rect.x = self.coords(0, 0)[0]
        sprite1.rect.y = self.coords(0, 0)[1]
        self.sprites.add(sprite1)
        sprite2 = pygame.sprite.Sprite()
        sprite2.image = load_image("mesa_bed.jpg")
        sprite2.rect = sprite2.image.get_rect()
        sprite2.rect.x = self.coords(3, 3)[0]
        sprite2.rect.y = self.coords(3, 3)[1]
        self.sprites.add(sprite2)
        sprite3 = pygame.sprite.Sprite()
        sprite3.image = load_image("sil_bed.jpg")
        sprite3.rect = sprite3.image.get_rect()
        sprite3.rect.x = self.coords(2, 4)[0]
        sprite3.rect.y = self.coords(2, 4)[1]
        self.sprites.add(sprite3)
        sprite5 = pygame.sprite.Sprite()
        sprite5.image = load_image("wordr_bed.png")
        sprite5.rect = sprite5.image.get_rect()
        sprite5.rect.x = self.coords(6, 4)[0]
        sprite5.rect.y = self.coords(6, 4)[1]
        self.sprites.add(sprite5)
        sprite4 = pygame.sprite.Sprite()
        sprite4.image = load_image("door.png")
        sprite4.rect = sprite4.image.get_rect()
        sprite4.rect.x = self.coords(3, 6)[0]
        sprite4.rect.y = self.coords(3, 6)[1]
        self.sprites.add(sprite4)
        self.sprites.draw(self.screen)
    
    def render():
        pass


class Corridor(Board):
    def __init__(self):
        super().__init__()
        sprite1 = pygame.sprite.Sprite()
        sprite1.image = load_image("flow_cor.png")
        sprite1.rect = sprite1.image.get_rect()
        sprite1.rect.x = self.coords(0, 4)[0]
        sprite1.rect.y = self.coords(0, 4)[1]
        self.sprites.add(sprite1)
        sprite2 = pygame.sprite.Sprite()
        sprite2.image = load_image("pict_cor.png")
        sprite2.rect = sprite2.image.get_rect()
        sprite2.rect.x = self.coords(5, 0)[0]
        sprite2.rect.y = self.coords(5, 0)[1]
        self.sprites.add(sprite2)
        sprite3 = pygame.sprite.Sprite()
        sprite3.image = load_image("tumba_cor.png")
        sprite3.rect = sprite3.image.get_rect()
        sprite3.rect.x = self.coords(6, 6)[0]
        sprite3.rect.y = self.coords(6, 6)[1]
        self.sprites.add(sprite3)
        sprite4 = pygame.sprite.Sprite()
        sprite4.image = load_image("door.png")
        sprite4.rect = sprite4.image.get_rect()
        sprite4.rect.x = self.coords(0, 1)[0]
        sprite4.rect.y = self.coords(0, 1)[1]
        self.sprites.add(sprite4)
        sprite5 = pygame.sprite.Sprite()
        sprite5.image = load_image("door.png")
        sprite5.rect = sprite5.image.get_rect()
        sprite5.rect.x = self.coords(3, 0)[0]
        sprite5.rect.y = self.coords(3, 0)[1]
        self.sprites.add(sprite5)
        sprite6 = pygame.sprite.Sprite()
        sprite6.image = load_image("door.png")
        sprite6.rect = sprite6.image.get_rect()
        sprite6.rect.x = self.coords(6, 3)[0]
        sprite6.rect.y = self.coords(6, 3)[1]
        self.sprites.add(sprite6)
        sprite7 = pygame.sprite.Sprite()
        sprite7.image = load_image("door.png")
        sprite7.rect = sprite7.image.get_rect()
        sprite7.rect.x = self.coords(3, 6)[0]
        sprite7.rect.y = self.coords(3, 6)[1]
        self.sprites.add(sprite7)
        self.sprites.draw(self.screen)
    
    def render():
        pass


class Bathroom(Board):
    def __init__(self):
        super().__init__()
        sprite1 = pygame.sprite.Sprite()
        sprite1.image = load_image("bath_bath.jpg")
        sprite1.rect = sprite1.image.get_rect()
        sprite1.rect.x = self.coords(4, 1)[0]
        sprite1.rect.y = self.coords(4, 1)[1]
        self.sprites.add(sprite1)
        sprite2 = pygame.sprite.Sprite()
        sprite2.image = load_image("sink_bath.jpg")
        sprite2.rect = sprite2.image.get_rect()
        sprite2.rect.x = self.coords(5, 6)[0]
        sprite2.rect.y = self.coords(5, 6)[1]
        self.sprites.add(sprite2)
        sprite3 = pygame.sprite.Sprite()
        sprite3.image = load_image("water_bath.jpg")
        sprite3.rect = sprite3.image.get_rect()
        sprite3.rect.x = self.coords(3, 4)[0]
        sprite3.rect.y = self.coords(3, 4)[1]
        self.sprites.add(sprite3)
        sprite5 = pygame.sprite.Sprite()
        sprite5.image = load_image("wordr_bath.jpg")
        sprite5.rect = sprite5.image.get_rect()
        sprite5.rect.x = self.coords(1, 6)[0]
        sprite5.rect.y = self.coords(1, 6)[1]
        self.sprites.add(sprite5)
        sprite4 = pygame.sprite.Sprite()
        sprite4.image = load_image("door.png")
        sprite4.rect = sprite3.image.get_rect()
        sprite4.rect.x = self.coords(0, 3)[0]
        sprite4.rect.y = self.coords(0, 3)[1]
        self.sprites.add(sprite4)
        self.sprites.draw(self.screen)
    
    def render():
        pass


class Kitchen(Board):
    def __init__(self):
        super().__init__()
        sprite1 = pygame.sprite.Sprite()
        sprite1.image = load_image("fridge_kitchen.png")
        sprite1.rect = sprite1.image.get_rect()
        sprite1.rect.x = self.coords(0, 0)[0]
        sprite1.rect.y = self.coords(0, 0)[1]
        self.sprites.add(sprite1)
        sprite2 = pygame.sprite.Sprite()
        sprite2.image = load_image("kitchen_kitchen.png")
        sprite2.rect = sprite2.image.get_rect()
        sprite2.rect.x = self.coords(2, 0)[0]
        sprite2.rect.y = self.coords(2, 0)[1]
        self.sprites.add(sprite2)
        sprite3 = pygame.sprite.Sprite()
        sprite3.image = load_image("mesa_kitchen.jpg")
        sprite3.rect = sprite3.image.get_rect()
        sprite3.rect.x = self.coords(1, 2)[0]
        sprite3.rect.y = self.coords(1, 2)[1]
        self.sprites.add(sprite3)
        sprite5 = pygame.sprite.Sprite()
        sprite5.image = load_image("sil_kitchen.jpg")
        sprite5.rect = sprite5.image.get_rect()
        sprite5.rect.x = self.coords(2, 4)[0]
        sprite5.rect.y = self.coords(2, 4)[1]
        self.sprites.add(sprite5)
        sprite6 = pygame.sprite.Sprite()
        sprite6.image = load_image("wordr_kitchen.jpg")
        sprite6.rect = sprite6.image.get_rect()
        sprite6.rect.x = self.coords(5, 6)[0]
        sprite6.rect.y = self.coords(5, 6)[1]
        self.sprites.add(sprite6)
        sprite4 = pygame.sprite.Sprite()
        sprite4.image = load_image("door.png")
        sprite4.rect = sprite3.image.get_rect()
        sprite4.rect.x = self.coords(6, 1)[0]
        sprite4.rect.y = self.coords(6, 1)[1]
        self.sprites.add(sprite4)
        self.sprites.draw(self.screen)
    
    def render():
        pass


class Livingroom(Board):
    def __init__(self):
        super().__init__()
        sprite1 = pygame.sprite.Sprite()
        sprite1.image = load_image("mesa_liv.jpg")
        sprite1.rect = sprite1.image.get_rect()
        sprite1.rect.x = self.coords(2, 2)[0]
        sprite1.rect.y = self.coords(2, 2)[1]
        self.sprites.add(sprite1)
        sprite2 = pygame.sprite.Sprite()
        sprite2.image = load_image("sofa_liv.png")
        sprite2.rect = sprite2.image.get_rect()
        sprite2.rect.x = self.coords(0, 0)[0]
        sprite2.rect.y = self.coords(0, 0)[1]
        self.sprites.add(sprite2)
        sprite3 = pygame.sprite.Sprite()
        sprite3.image = load_image("tel_liv.jpg")
        sprite3.rect = sprite3.image.get_rect()
        sprite3.rect.x = self.coords(0, 6)[0]
        sprite3.rect.y = self.coords(0, 6)[1]
        self.sprites.add(sprite3)
        sprite5 = pygame.sprite.Sprite()
        sprite5.image = load_image("tumba_liv.jpg")
        sprite5.rect = sprite5.image.get_rect()
        sprite5.rect.x = self.coords(0, 4)[0]
        sprite5.rect.y = self.coords(0, 4)[1]
        self.sprites.add(sprite5)
        sprite4 = pygame.sprite.Sprite()
        sprite4.image = load_image("door.png")
        sprite4.rect = sprite3.image.get_rect()
        sprite4.rect.x = self.coords(6, 3)[0]
        sprite4.rect.y = self.coords(6, 3)[1]
        self.sprites.add(sprite4)
        self.sprites.draw(self.screen)
    
    def render():
        pass


class Store(Board):
    def __init__(self):
        super().__init__()
        sprite1 = pygame.sprite.Sprite()
        sprite1.image = load_image("bag_store.png")
        sprite1.rect = sprite1.image.get_rect()
        sprite1.rect.x = self.coords(4, 6)[0]
        sprite1.rect.y = self.coords(4, 6)[1]
        self.sprites.add(sprite1)
        sprite2 = pygame.sprite.Sprite()
        sprite2.image = load_image("case_store.png")
        sprite2.rect = sprite2.image.get_rect()
        sprite2.rect.x = self.coords(5, 6)[0]
        sprite2.rect.y = self.coords(5, 6)[1]
        self.sprites.add(sprite2)
        sprite3 = pygame.sprite.Sprite()
        sprite3.image = load_image("clothes_store.png")
        sprite3.rect = sprite3.image.get_rect()
        sprite3.rect.x = self.coords(2, 1)[0]
        sprite3.rect.y = self.coords(2, 1)[1]
        self.sprites.add(sprite3)
        sprite4 = pygame.sprite.Sprite()
        sprite4.image = load_image("door.png")
        sprite4.rect = sprite3.image.get_rect()
        sprite4.rect.x = self.coords(0, 2)[0]
        sprite4.rect.y = self.coords(0, 2)[1]
        self.sprites.add(sprite4)
        sprite5 = pygame.sprite.Sprite()
        sprite5.image = load_image("rub_store.png")
        sprite5.rect = sprite5.image.get_rect()
        sprite5.rect.x = self.coords(3, 4)[0]
        sprite5.rect.y = self.coords(3, 4)[1]
        self.sprites.add(sprite5)
        sprite6 = pygame.sprite.Sprite()
        sprite6.image = load_image("trap_store.jpg")
        sprite6.rect = sprite6.image.get_rect()
        sprite6.rect.x = self.coords(6, 4)[0]
        sprite6.rect.y = self.coords(6, 4)[1]
        self.sprites.add(sprite6)
        sprite7 = pygame.sprite.Sprite()
        sprite7.image = load_image("wordr_store.JPG")
        sprite7.rect = sprite7.image.get_rect()
        sprite7.rect.x = self.coords(5, 0)[0]
        sprite7.rect.y = self.coords(5, 0)[1]
        self.sprites.add(sprite7)
        self.sprites.draw(self.screen)
    
    def render():
        pass


class Start:
    def __init__(self):
        self.screen = pygame.Surface((750, 750))
        font = pygame.font.Font(None, 15)
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
room = start
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
    screen.blit(room.screen)
    pygame.display.flip()
