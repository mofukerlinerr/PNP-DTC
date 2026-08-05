from tkinter import font
import random
import pygame
import sys

# ----------------------------
# Startup area
# ----------------------------
pygame.init()

font = pygame.font.Font(None, 36)

gen = 10000

control = True

player_speed = 5
playerX = 0
playerY = 0
player_moving = False
player_direction = "down"
collection_area = 50
origin_area = 10

menu_open = False
Fuel = 0

time = 0
tick = 0

spawnX = 100
spawnY = 100

Fuel_worth = 5
Fuel_count = 100

rects = []

for i in range(Fuel_count):
    rects.append(pygame.Rect(random.randint(-spawnX, spawnX), random.randint(-spawnY, spawnY), 20, 20))



screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("")

clock = pygame.time.Clock()

camera_x = 0
camera_y = 0

running = True

# ----------------------------
# Main game loop
# ----------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if control == True:

        keys = pygame.key.get_pressed()
        player_moving = False

        if keys[pygame.K_w]:
            playerY -= player_speed
            player_moving = True
            player_direction = "up"

        if keys[pygame.K_a]:
            playerX -= player_speed
            player_moving = True
            player_direction = "left"

        if keys[pygame.K_s]:
            playerY += player_speed
            player_moving = True
            player_direction = "down"

        if keys[pygame.K_d]:
            playerX += player_speed
            player_moving = True
            player_direction = "right"

        if keys[pygame.K_e]:
            menu_open = True

# ----------------------------
# menu area
# ----------------------------

    if menu_open == True:
        screen.fill((50, 50, 50))
        pygame.draw.rect(screen, (0, 0, 255), (screen_width// 2, screen_height// 2, 10, 10))

        map_rects = []

        for i in range(Fuel_count):
            map_rects.append(pygame.Rect(rects[i].x - camera_x // 10, rects[i].y - camera_y // 10 , 10, 10))

        for rect in map_rects:
            pygame.draw.rect(screen, (255, 0, 0), (rect.x // 10, rect.y // 10, rect.width, rect.height))

        pygame.display.flip()

        gen -= 0.04

        if keys[pygame.K_e]:
            menu_open = False

        clock.tick(50)
        continue

    camera_x = playerX - screen_width // 2
    camera_y = playerY - screen_height // 2

    tick += 1
    time = tick/50

    if time >= 10:
        gen -= 0.02

    if abs(playerX) <= origin_area and abs(playerY) <= origin_area and Fuel > 0:
        Fuel -= 1
        gen += Fuel_worth

    for rect in rects:
        nearest_x = max(rect.left, min(playerX, rect.right))
        nearest_y = max(rect.top, min(playerY, rect.bottom))
        dx = playerX - nearest_x
        dy = playerY - nearest_y

        if dx * dx + dy * dy <= collection_area * collection_area:
            rect.x = random.randint(-spawnX, spawnX)
            rect.y = random.randint(-spawnY, spawnY)
            Fuel += 1

    print(f'Player: {playerX}, {playerY} | Fuel: {Fuel} | Gen: {gen:.0f} | Time: {time:.2f}')


    screen.fill((100, 100, 100))

    for rect in rects:
        pygame.draw.rect(screen, (255, 0, 0), (rect.x - camera_x, rect.y - camera_y, rect.width, rect.height))

    pygame.draw.circle(screen, (0, 0, 255), (playerX - camera_x, playerY - camera_y), 20)
    fuel_count = font.render(f"Fuel: {Fuel}", True, (0, 0, 0))
    screen.blit(fuel_count, (0, 0))


    pygame.draw.circle(screen, (0, 0, 0), (0 - camera_x, 0 - camera_y), 20)

    gen_charge = font.render(f"{gen:.0f}", True, (255, 255, 255))
    text_rect = gen_charge.get_rect(center=(screen_width * 0.50 - playerX, screen_height * 0.50 - playerY))
    screen.blit(gen_charge, text_rect)

    if gen <= 0:
        screen.fill((0, 0, 0))
        game_over = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over, (0, 0))

    pygame.display.flip()
    clock.tick(50)
# ----------------------------
# Shutdown area
# ----------------------------
pygame.quit()
sys.exit()