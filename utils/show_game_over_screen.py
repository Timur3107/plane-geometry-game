import pygame
import sqlite3
from utils.utils import *
from utils.constants import *

# получение лучшего рекорда
def get_best_score():
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.execute('SELECT MAX(score) FROM records')
    best_score = cursor.fetchone()[0]

    conn.close()
    if best_score is not None:
        return best_score
    else:
        return 0

# Функция отображения финального экрана
def show_game_over_screen(score, distance):
    screen.fill(FONT_COLOR)
    title_font = pygame.font.Font(None, 36)
    score_font = pygame.font.Font(None, 30)
    font = pygame.font.Font(None, 20)
    game_over_text = title_font.render("Game Over", True, INITIAL_COLOR)
    score_text = score_font.render(f"Очки: {score}", True, INITIAL_COLOR)
    distance_text = score_font.render(f"Дистанция: {distance}", True, INITIAL_COLOR)
    record_text = score_font.render(f"РЕКОРД: {get_best_score()}", True, (255, 0, 0))
    restart_text = font.render("Нажмите SPACE, чтобы перезапустить игру", True, INITIAL_COLOR)

    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    distance_rect = distance_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))
    record_rect = distance_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.8))
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 7 // 8))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(distance_text, distance_rect)
    screen.blit(record_text, record_rect)
    screen.blit(restart_text, restart_rect)

    pygame.display.flip()

    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting_for_restart = False


