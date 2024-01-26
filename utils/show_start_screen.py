import pygame
from utils.utils import *
from utils.constants import *


#функция отображения стартового экрана
def show_start_screen():
    screen.fill(FONT_COLOR)
    font = pygame.font.Font(None, 30)
    title_font = pygame.font.Font(None, 36)
    title_text = title_font.render("Plane Geometry Game", True, INITIAL_COLOR)
    instruction_text = font.render("Нажимайте A и D, чтобы перемещаться,", True, INITIAL_COLOR)
    second_instruction_text = font.render("W и S, чтобы контролировать скорость", True, INITIAL_COLOR)

    start_text = font.render("Нажмите SPACE, чтобы играть", True, INITIAL_COLOR)

    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8))
    instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    second_instruction = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.8))
    start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4))

    screen.blit(title_text, title_rect)
    screen.blit(instruction_text, instruction_rect)
    screen.blit(second_instruction_text, second_instruction)
    screen.blit(start_text, start_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
