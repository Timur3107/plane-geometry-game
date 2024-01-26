import pygame
from utils.constants import *

# Загрузка спрайтов и их масштабирование

plane_img = pygame.transform.scale(pygame.image.load("images/plane.png"), (40, 40))
platform_img = pygame.transform.scale(pygame.image.load("images/platform.png"), (70, 20))
coin_img = pygame.transform.scale(pygame.image.load("images/coin.png"), (30, 30))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
