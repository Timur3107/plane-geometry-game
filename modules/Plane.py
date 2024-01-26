import pygame
from utils.constants import *
from utils.utils import *


# Класс самолета
class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = plane_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed_y = -8

    def update(self):
        # self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
