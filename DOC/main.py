import pygame
import sys

FPS = 120


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('data/gifon.gif'), (800, 600))
    screen.blit(fon, (0, 0))
    fon1 = pygame.transform.scale(load_image('data/letsplay.png'), (400, 50))
    screen.blit(fon1, (200, 400))
    fon2 = pygame.transform.scale(load_image('data/shop.png'), (200, 50))
    screen.blit(fon2, (300, 451))
    fon3 = pygame.transform.scale(load_image('data/settings.png'), (200, 50))
    screen.blit(fon3, (300, 502))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.update()
        clock.tick(FPS)


def load_image(name, colorkey=True):
    image = pygame.image.load(name)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))
pygame.display.flip()
clock = pygame.time.Clock()
x = 0
y = 0
speed = 10
start_screen()
pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
all_sprites = pygame.sprite.Group()
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
