import pygame


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
        screen.blit(pygame.image.load("mega_gif.gif"), (0, 0))


class Finish:
    def __init__(self):
        pass