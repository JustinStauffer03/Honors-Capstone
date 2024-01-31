import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_POS = [WIDTH/2, HEIGHT-2*PLAYER_SIZE]
ENEMY_SIZE = 50
ENEMY_POS = [random.randint(0, WIDTH-ENEMY_SIZE), 0]
ENEMY_LIST = [ENEMY_POS]
SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH-ENEMY_SIZE)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE))

def update_enemy_positions(enemy_list):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + PLAYER_SIZE)) or (p_x >= e_x and p_x < (e_x + ENEMY_SIZE)):
        if (e_y >= p_y and e_y < (p_y + PLAYER_SIZE)) or (p_y >= e_y and p_y < (e_y + ENEMY_SIZE)):
            return True
    return False

# Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = PLAYER_POS[0]
            y = PLAYER_POS[1]

            if event.key == pygame.K_LEFT:
                x -= PLAYER_SIZE
            elif event.key == pygame.K_RIGHT:
                x += PLAYER_SIZE

            PLAYER_POS = [x, y]

    screen.fill(WHITE)

    drop_enemies(ENEMY_LIST)
    update_enemy_positions(ENEMY_LIST)

    if collision_check(ENEMY_LIST, PLAYER_POS):
        game_over = True

    draw_enemies(ENEMY_LIST)

    pygame.draw.rect(screen, BLUE, (PLAYER_POS[0], PLAYER_POS[1], PLAYER_SIZE, PLAYER_SIZE))

    clock.tick(30)

    pygame.display.update()
