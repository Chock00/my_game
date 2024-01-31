import pygame
import os
import sys
import sqlite3
import datetime as dt


class Start:
    def __init__(self):
        pass
    
    def draw_start(self, screen):
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 255, 0), ((200, 200), (300, 100)))
        pygame.draw.rect(screen, (0, 0, 255), ((175, 350), (350, 50)))
        font1 = pygame.font.Font(None, 50)
        text1 = font1.render('Суслик: остаться в живых 2', True, (0, 0, 0))
        screen.blit(text1, (120, 50))
        font2 = pygame.font.Font(None, 100)
        text2 = font2.render('Играть', True, (0, 0, 0))
        screen.blit(text2, (225, 203))
        font3 = pygame.font.Font(None, 50)
        text3 = font3.render('Таблица лидеров', True, (0, 0, 0))
        screen.blit(text3, (195, 353))


class Finish:
    def __init__(self):
        pass

    def draw_good(self, screen, res):
        screen.fill((255, 255, 255))
        font1 = pygame.font.Font(None, 100)
        text1 = font1.render('Победа!', True, (255, 0, 0))
        screen.blit(text1, (300, 100))
        font2 = pygame.font.Font(None, 70)
        text2 = font2.render('Ваш результат: ' + str(res) + 'секунд', True, (0, 0, 0))
        screen.blit(text2, (200, 300))
        do_end(res)

    def draw_bad(self, screen):
        screen.fill((255, 255, 255))
        font1 = pygame.font.Font(None, 100)
        text1 = font1.render('Неудача!', True, (255, 0, 0))
        screen.blit(text1, (300, 100))
        font2 = pygame.font.Font(None, 70)
        text2 = font2.render('Вас поймали. Суслик оказался не таким добрым, как выглядел', True, (0, 0, 0))
        screen.blit(text2, (50, 300))


def do_end(res):
    connection = sqlite3.connect('top.db')
    cur = connection.cursor()
    al = cur.execute('''INSERT INTO players(time,res) VALUES(?,?')''', (dt.datetime.now(), res))
    connection.commit()
    connection.close()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image