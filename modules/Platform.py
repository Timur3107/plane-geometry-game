import pygame
import random
from utils.constants import *
from utils.utils import *

platforms = pygame.sprite.Group()
# Класс платформ
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = platform_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-500, -100)
        self.speed_y = 3

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT or pygame.sprite.spritecollide(self, platforms, False):
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-500, -200)