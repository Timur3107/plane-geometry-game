import pygame
import random
import sys
import sqlite3

from utils.constants import *

# Импорт модулей
from modules.Plane import Plane
from modules.Platform import Platform
from modules.Coin import Coin

# Импорт функций
from utils.show_start_screen import show_start_screen
from utils.show_game_over_screen import show_game_over_screen
from utils.save_record import save_record

# Работа с базой данных sqlite3
conn = sqlite3.connect('records.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score INTEGER
    )
''')

# инициализация Pygame
pygame.init()

# создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flying Plane Game")

# грпуппы спрайтов
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Создание игровых объектов
plane = Plane()
all_sprites.add(plane)

# Создание платформ и монет
for i in range(5):
    platform = Platform()
    all_sprites.add(platform)
    platforms.add(platform)

    coin = Coin()
    all_sprites.add(coin)
    coins.add(coin)

# показываем стартовый экран
show_start_screen()

# Основной цикл игры
clock = pygame.time.Clock()
score = 0
distance = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка клавиш
    keys = pygame.key.get_pressed()
    # Ускорение движения платформ
    if keys[pygame.K_w]:
        for platform in platforms:
            platform.speed_y = 4
        for coin in coins:
            coin.speed_y = 4
    # Замедление движения платформ
    elif keys[pygame.K_s]:
        for platform in platforms:
            platform.speed_y = 2
        for coin in coins:
            coin.speed_y = 2
    else:
        # Вернуть обычную скорость платформ и монет
        for platform in platforms:
            platform.speed_y = 3
        for coin in coins:
            coin.speed_y = 3

    # управление самолетом влево и впрво
    if keys[pygame.K_a]:
        plane.rect.x -= 5
        plane.rect.x = max(0, plane.rect.x)
    if keys[pygame.K_d]:
        plane.rect.x += 5
        plane.rect.x = min(SCREEN_WIDTH - plane.rect.width, plane.rect.x)

    # Обновление платформ и монет
    for platform in platforms:
        platform.update()

    for coin in coins:
        coin.update()

    distance += 1

    # каждые 300 метров обновляем спавн платформ
    if distance % 300 == 0:
        for i in range(5):
            platform = Platform()

            # проверка коллизий с другими платформами, пока платформа не найдет свободное место
            while pygame.sprite.spritecollide(platform, platforms, False):
                platform.rect.x = random.randint(0, SCREEN_WIDTH - platform.rect.width)
                platform.rect.y = random.randint(-500, -200)
            platforms.add(platform)
            all_sprites.add(platform)

            # platforms.add(platform)

    all_sprites.update()

    # Обработка коллизий
    hits_platform = pygame.sprite.spritecollide(plane, platforms, False)
    if hits_platform:
        # Сохраняем рекорд
        save_record(score)

        show_game_over_screen(score, distance)

        # Сбросим текущие игровые объекты
        all_sprites.empty()
        platforms.empty()
        coins.empty()

        # Создание новых платформ и монет
        for i in range(5):
            platform = Platform()
            all_sprites.add(platform)
            platforms.add(platform)

            coin = Coin()
            all_sprites.add(coin)
            coins.add(coin)

        # Сбросим счет и расстояние
        score = 0
        distance = 0

        # Переместим самолет в стартовую позицию
        plane.rect.centerx = SCREEN_WIDTH // 2
        plane.rect.bottom = SCREEN_HEIGHT - 20

        # Добавим самолет в группу спрайтов
        all_sprites.add(plane)

    hits_coin = pygame.sprite.spritecollide(plane, coins, True)
    for hit in hits_coin:
        score += 1
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    # Отрисовка
    screen.fill(FONT_COLOR)
    all_sprites.draw(screen)

    # Отображение счета и пройденного расстояния
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, INITIAL_COLOR)
    distance_text = font.render(f"Distance: {distance}", True, INITIAL_COLOR)
    screen.blit(score_text, (10, 10))
    screen.blit(distance_text, (10, 50))

    pygame.display.flip()

    clock.tick(30)

# Завершение игры
conn.commit()
conn.close()

pygame.quit()
sys.exit()
