import pygame
import os
import sys
import time
import sqlite3
from menu import Start, Finish, draw_table
from random import choice

class Room:
    def __init__(self):
        self.width = 7
        self.height = 7
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 0
        self.top = 50
        self.cell_size = 100
        self.screen = pygame.Surface((700, 750))
        self.sprites = pygame.sprite.Group()

        self.sus_gr = pygame.sprite.Group()
        self.sus = pygame.sprite.Sprite()
        self.sus.image = load_image("suslik.png")
        self.sus.rect = self.sus.image.get_rect()
        self.sus.rect.x = self.coords(0, 5)[0]
        self.sus.rect.y = self.coords(0, 5)[1]
        self.sus_gr.add(self.sus)
        self.pla_gr = pygame.sprite.Group()
        self.pla = pygame.sprite.Sprite()
        self.pla.image = load_image("player.png")
        self.pla.rect = self.pla.image.get_rect()
        self.pla.rect.x = self.coords(1, 1)[0]
        self.pla.rect.y = self.coords(1, 1)[1]
        self.pla_gr.add(self.pla)
        self.cor_bord = []
        for i in range(0, 7):
            for j in range(0, 7):
                self.cor_bord.append((i, j))

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
    
    def is_near(self, i1, j1, i2, j2):
        if i1 == i2:
            return j1 == j2 + 1 or j1 == j2 - 1
        if j1 == j2:
            return i1 == i2 + 1 or i1 == i2 - 1
        return False
    
    def draw_room(self, screen):  
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                x1 = self.left + self.cell_size * i
                y1 = self.top + self.cell_size * j
                w, h = self.cell_size, self.cell_size
                pygame.draw.rect(screen, (0, 0, 0), ((x1, y1), (w, h)), 1)
        self.sprites.draw(screen)
        self.sus_gr.draw(screen)
        self.pla_gr.draw(screen)


class Hall(Room):
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
        self.busy = [(3, 0), (6, 2), (0, 3), (4, 5), (0, 6), (1, 6), (3, 6), (4, 6)]
        self.doors = {(3, 0): ((3, 5), 'corridor'), (3, 6): ((0, 0), 'finish'), (0, 3): ((5, 3), 'livingroom'), (6, 2): ((1, 2), 'store')}


class Bedroom(Room):
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
        self.busy = [(0, 0), (1, 0), (3, 3), (4, 3), (2, 4), (6, 4), (6, 5), (3, 6)]
        self.doors = {(3, 6): ((3, 1), 'corridor')}


class Corridor(Room):
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
        self.busy = [(3, 0), (5, 0), (6, 0), (0, 1), (6, 3), (0, 4), (3, 6), (6, 6)]
        self.doors = {(3, 0): ((3, 5), 'bedroom'), (3, 6): ((3, 1), 'hall'), (0, 1): ((5, 1), 'kitchen'), (6, 3): ((1, 3), 'bathroom')}


class Bathroom(Room):
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
        self.busy = [(0, 3), (1, 6), (2, 6), (3, 4), (4, 1), (4, 2), (5, 1), (5, 2), (5, 6)]
        self.doors = {(0, 3): ((5, 3), 'corridor')}


class Kitchen(Room):
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
        self.busy = [(0, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 2), (4, 0), (4, 2), (5, 0), (5, 6), (6, 0), (6, 1), (6, 6)]
        self.doors = {(6, 1): ((1, 1), 'corridor')}


class Livingroom(Room):
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
        sprite5.rect.x = self.coords(4, 0)[0]
        sprite5.rect.y = self.coords(4, 0)[1]
        self.sprites.add(sprite5)
        sprite4 = pygame.sprite.Sprite()
        sprite4.image = load_image("door.png")
        sprite4.rect = sprite3.image.get_rect()
        sprite4.rect.x = self.coords(6, 3)[0]
        sprite4.rect.y = self.coords(6, 3)[1]
        self.sprites.add(sprite4)
        self.sprites.draw(self.screen)
        self.busy = [(0, 0), (0, 6), (1, 0), (1, 6), (2, 0), (2, 2), (4, 0), (6, 3)]
        self.doors = {(6, 3): ((1, 3), 'hall')}


class Store(Room):
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
        sprite7.rect.x = self.coords(4, 0)[0]
        sprite7.rect.y = self.coords(4, 0)[1]
        self.sprites.add(sprite7)
        self.sprites.draw(self.screen)
        self.busy = [(0, 2), (2, 1), (3, 4), (4, 0), (4, 1), (4, 6), (5, 0), (5, 1), (5, 6), (6, 0), (6, 1), (6, 4)]
        self.doors = {(0, 2): ((5, 2), 'hall')} # координаты двери: (координаты появления, комната появления)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def do_base():
    connection = sqlite3.connect('top.db')
    cur = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS players
          (time TEXT, res INT)''')
    connection.commit()
    connection.close()


def draw_key(keys):
    if keys == 1:
        t = 'Под картиной вы нашли хорошо спрятанный ключик'
    if keys == 2:
        t = 'Вы открыли шкаф ключом и нашли ещё один поменьше'
    if keys == 3:
        t = 'Вы открыли холодильник ключиком и нашли чистящее средство'
    if keys == 4:
        t = 'Вы засыпали в джакузи средство и нашли на дне крепкие ножницы'
    if keys == 5:
        t = 'Вы разрезали пакет ножницами и нашли в нем отвёртку'
    if keys == 6:
        t = 'Вы разобрали телевизор и нашли внутри ещё один ключ'
    if keys == 7:
        t = 'Вы открыли шкаф и нашли огромный ключ'
    font1 = pygame.font.Font(None, 30)
    text = font1.render(t, True, (0, 0, 0))
    screen.blit(text, (10, 20))

def next_mov(sus_pos, pla_pos):
    go = choice((0, 1))
    if go == 0:
        if sus_pos[0] != pla_pos[0]:
            if sus_pos[0] > pla_pos[0]:
                sus_pos = (sus_pos[0] - 1, sus_pos[1])
            else:
                sus_pos = (sus_pos[0] + 1, sus_pos[1])
        else:
            if sus_pos[1] > pla_pos[1]:
                sus_pos = (sus_pos[0], sus_pos[1] - 1)
            else:
                sus_pos = (sus_pos[0], sus_pos[1] + 1)
    else:
        if sus_pos[1] != pla_pos[1]:
            if sus_pos[1] > pla_pos[1]:
                sus_pos = (sus_pos[0], sus_pos[1] - 1)
            else:
                sus_pos = (sus_pos[0], sus_pos[1] + 1)
        else:
            if sus_pos[0] > pla_pos[0]:
                sus_pos = (sus_pos[0] - 1, sus_pos[1])
            else:
                sus_pos = (sus_pos[0] + 1, sus_pos[1])
    return sus_pos, pla_pos
        


pygame.init()
do_base()
keys = 0
is_draw_key = 0
pygame.display.set_caption('Суслик: остаться в живых 2')
size = width, height = 7 * 100, 7 * 100 + 50
screen = pygame.display.set_mode(size)
hall, bedroom, corridor, bathroom = Hall(), Bedroom(), Corridor(), Bathroom()
kitchen, livingroom, store, start, finish = Kitchen(), Livingroom(), Store(), Start(), Finish()
rooms = [start, finish, hall, bedroom, corridor, bathroom, kitchen, livingroom, store]
get_room = {'hall': hall, 'bedroom': bedroom, 'corridor': corridor, 'bathroom': bathroom, 'kitchen': kitchen, 'livingroom':livingroom, 'store': store}
for room in rooms[2:]:
    room.set_view(0, 50, 100)
running = True
room = start
pos_mouse = 0, 0
pos_pla = 1, 1
t_sus = 0
pos_sus = 0, 5
t_sus_0 = time.time()
while running:
    if room in rooms[2:]:
        t_sus_1 = time.time()
        if t_sus_1 - t_sus_0 > 2:
            t_sus_0 = time.time()
            pos_sus, pos_pla = next_mov(pos_sus, pos_pla)
            room.sus.rect.x = room.coords(*pos_sus)[0]
            room.sus.rect.y = room.coords(*pos_sus)[1]
            screen.fill((255, 255, 255))
            room.draw_room(screen)
            if is_draw_key:
                draw_key(keys)
        if pos_sus == pos_pla:
            room = finish
            sad = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pos_mouse = event.pos
        if room == start:
            screen.fill((255, 255, 255))
            start.draw_start(screen)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 200 <= pos_mouse[0] <= 500 and 200 <= pos_mouse[1] <= 300:
                    time_1 = time.time()
                    time_2 = time.time()
                    hap, sad = 0, 0
                    room = bedroom
                    pos_pla = 1, 1
                    first_end = 1
                if 175 <= pos_mouse[0] <= 525 and 350 <= pos_mouse[1] <= 400:
                    room = 'table'
        elif room == 'table':
            draw_table(screen)
        elif room == finish:
            if first_end:
                f = 1
            else:
                f = 0
            if hap:
                screen.fill((255, 255, 255))
                finish.draw_good(screen, time_2 - time_1, f)
            else:
                screen.fill((255, 255, 255))
                finish.draw_bad(screen)
            first_end = 0
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and room.get_cell(pos_mouse):
                x_mou, y_mou = room.get_cell(pos_mouse)
                if room.is_near(x_mou, y_mou, pos_pla[0], pos_pla[1]) and (x_mou, y_mou) in room.busy:
                    if (x_mou, y_mou) not in room.doors:
                        if keys == 0 and (x_mou == 5 or x_mou == 6) and y_mou == 0 and isinstance(room, Corridor):
                            keys += 1
                            is_draw_key = 1
                            draw_key(keys)
                        if keys == 1 and (x_mou == 0 or x_mou == 1) and y_mou == 6 and isinstance(room, Hall):
                            keys += 1
                            is_draw_key = 1
                            draw_key(keys)
                        if keys == 2 and x_mou == 0 and y_mou == 0 and isinstance(room, Kitchen):
                            keys += 1
                            is_draw_key = 1
                            draw_key(keys)
                        if keys == 3 and (x_mou == 4 or x_mou == 5) and (y_mou == 1 or y_mou == 2) and isinstance(room, Bathroom):
                            keys += 1 
                            is_draw_key = 1
                            draw_key(keys)
                        if keys == 4 and x_mou == 3 and y_mou == 4 and isinstance(room, Store):
                            keys += 1
                            is_draw_key = 1
                            draw_key(keys)
                        if keys == 5 and (x_mou == 0 or x_mou == 1) and y_mou == 6 and isinstance(room, Livingroom):
                            keys += 1
                            is_draw_key = 1
                            draw_key(keys)
                        if keys == 6 and x_mou == 6 and (y_mou == 4 or y_mou == 5) and isinstance(room, Bedroom):
                            keys += 1
                            is_draw_key = 1
                            draw_key(keys)
                    else:
                        try:
                            pos_pla = room.doors[(x_mou, y_mou)][0]
                            new_x, new_y = pos_pla[0], pos_pla[1]
                            room = get_room[room.doors[(x_mou, y_mou)][1]]
                            room.pla.rect.x = room.coords(new_x, new_y)[0]
                            room.pla.rect.y = room.coords(new_x, new_y)[1]
                            is_draw_key = 0
                            pos_sus = (0, 5)
                            room.sus.rect.x = room.coords(*pos_sus)[0]
                            room.sus.rect.y = room.coords(*pos_sus)[1]
                        except KeyError:
                            room = finish
                            hap = 1
                            time_2 = time.time()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                new_x, new_y = pos_pla[0], pos_pla[1] - 1
                if (new_x, new_y) not in room.busy and (new_x, new_y) in room.cor_bord:
                    pos_pla = (new_x, new_y)
                    room.pla.rect.x = room.coords(new_x, new_y)[0]
                    room.pla.rect.y = room.coords(new_x, new_y)[1]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                new_x, new_y = pos_pla[0], pos_pla[1] + 1
                if (new_x, new_y) not in room.busy and (new_x, new_y) in room.cor_bord:
                    pos_pla = (new_x, new_y)
                    room.pla.rect.x = room.coords(new_x, new_y)[0]
                    room.pla.rect.y = room.coords(new_x, new_y)[1]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                new_x, new_y = pos_pla[0] - 1, pos_pla[1]
                if (new_x, new_y) not in room.busy and (new_x, new_y) in room.cor_bord:
                    pos_pla = (new_x, new_y)
                    room.pla.rect.x = room.coords(new_x, new_y)[0]
                    room.pla.rect.y = room.coords(new_x, new_y)[1]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                new_x, new_y = pos_pla[0] + 1, pos_pla[1]
                if (new_x, new_y) not in room.busy and (new_x, new_y) in room.cor_bord:
                    pos_pla = (new_x, new_y)
                    room.pla.rect.x = room.coords(new_x, new_y)[0]
                    room.pla.rect.y = room.coords(new_x, new_y)[1]
            try:
                screen.fill((255, 255, 255))
                room.draw_room(screen)
                if is_draw_key:
                    draw_key(keys)
            except AttributeError:
                pass
    pygame.display.flip()
