import random
import pygame
import sys
from enum import Enum

# ----------------------------
# Startup area
# ----------------------------
pygame.init()

# ----------------------------
# Definition area
# ----------------------------
font = pygame.font.Font(None, 36)

playingarea = 0
spawnX = playingarea - 10
spawnY = playingarea - 10

difficulty = "Normal"
difficulty_select = True
map_open = False
running = True
camera_x = 0
camera_y = 0
Fuel = 0
time = 0
tick = 0
genX = 0
genY = 0

map_scale = playingarea / 2000
gen = 1000

screen_width = 800
screen_height = 600

control = True
player_speed = 5
playerX = 0
playerY = 0
player_moving = False
player_direction = "down"
playerhealth = 100
collection_area = 50
origin_area = 250

Fuel_worth = 5
Fuel_count = playingarea // 100


# ----------------------------
# list setup area
# ----------------------------
rects = []

for i in range(Fuel_count):
    rects.append(pygame.Rect(random.randint(-spawnX, spawnX), random.randint(-spawnY, spawnY), 20, 20))

# ----------------------------
# pygame variables
# ----------------------------
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DTC Game")
clock = pygame.time.Clock()

while difficulty_select:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            difficulty_select = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = event.pos

            button_easy = pygame.Rect(100, 50, 200, 40)
            button_normal = pygame.Rect(100, 100, 200, 40)
            button_hard = pygame.Rect(100, 150, 200, 40)
            
            if button_easy.collidepoint(click_pos):
                difficulty = "Easy"
                difficulty_select = False
                playingarea = 500
            elif button_normal.collidepoint(click_pos):
                difficulty = "Normal"
                difficulty_select = False
                playingarea = 1000
            elif button_hard.collidepoint(click_pos):
                difficulty = "Hard"
                difficulty_select = False
                playingarea = 2000
    
    screen.fill((0, 0, 0))
    difficulty_text = font.render(f"Difficulty: {difficulty}", True, (255, 255, 255))
    screen.blit(difficulty_text, (100, 10))

    button_easy = pygame.Rect(100, 50, 200, 40)
    button_normal = pygame.Rect(100, 100, 200, 40)
    button_hard = pygame.Rect(100, 150, 200, 40)

    pygame.draw.rect(screen, (0, 255, 0), button_easy)
    pygame.draw.rect(screen, (255, 255, 0), button_normal)
    pygame.draw.rect(screen, (255, 0, 0), button_hard)

    easy_text = font.render("Easy", True, (0, 0, 0))
    normal_text = font.render("Normal", True, (0, 0, 0))
    hard_text = font.render("Hard", True, (0, 0, 0))

    screen.blit(easy_text, (button_easy.x + 10, button_easy.y + 5))
    screen.blit(normal_text, (button_normal.x + 10, button_normal.y + 5))
    screen.blit(hard_text, (button_hard.x + 10, button_hard.y + 5))

    pygame.display.flip()
    clock.tick(50)

# ----------------------------
# Main game loop
# ----------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if control:

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
            map_open = True

        if keys[pygame.K_r] and Fuel > 0:
            if player_direction == "up":
                playerY -= player_speed * 2
            elif player_direction == "down":
                playerY += player_speed * 2
            elif player_direction == "left":
                playerX -= player_speed * 2
            elif player_direction == "right":
                playerX += player_speed * 2

            Fuel -= 1


    # ----------------------------
    # map area
    # ----------------------------
    if map_open:
        screen.fill((50, 50, 50))


        pygame.draw.rect(screen, (0, 0, 255), (screen_width // 2 - 10 // 2, screen_height // 2 - 10 // 2, 10, 10))

        map_center_x = screen_width // 2
        map_center_y = screen_height // 2

        for r in rects:
            draw_x = map_center_x + int((r.x - playerX) * map_scale)
            draw_y = map_center_y + int((r.y - playerY) * map_scale)
            
            draw_w = max(2, int(r.width * map_scale))
            draw_h = max(2, int(r.height * map_scale))
            pygame.draw.rect(screen, (255, 0, 0), (draw_x - draw_w // 2, draw_y - draw_h // 2, draw_w, draw_h))

        pygame.display.flip()

        gen -= 0.1
        map_open = False

        clock.tick(50)
        continue

    camera_x = playerX - screen_width // 2
    camera_y = playerY - screen_height // 2


    # ----------------------------
    # Area Limit
    # ----------------------------
    if playerY > playingarea:
        playerY -= player_speed

    if playerY < -playingarea:
        playerY += player_speed

    if playerX > playingarea:
        playerX -= player_speed

    if playerX < -playingarea:
        playerX += player_speed


    # ----------------------------
    # Generator Area
    # ----------------------------
    if gen >= 1:
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

    print(f'Player: {playerX}, {playerY} | Fuel: {Fuel} | Gen: {gen:.0f} | Time: {time:.2f}| Difficulty: {difficulty}| Player Direction: {player_direction}')
    screen.fill((100, 100, 100))

# ----------------------------
# active variables area
# ----------------------------
    player_rect = pygame.Rect(playerX - camera_x - 20, playerY - camera_y - 20, 40, 40)
    origin_screen_x = 0 - camera_x
    origin_screen_y = 0 - camera_y
    origin_radius = 20
    origin_screen_x = max(origin_radius, min(screen_width - origin_radius, origin_screen_x))
    origin_screen_y = max(origin_radius, min(screen_height - origin_radius, origin_screen_y))
    gen_charge = font.render(f"{gen:.0f}", True, (255, 255, 255))
    text_rect = gen_charge.get_rect(center=(origin_screen_x, origin_screen_y))
    fuel_count = font.render(f"Fuel: {Fuel}", True, (0, 0, 0))


    for rect in rects:
        pygame.draw.rect(screen, (255, 0, 0), (rect.x - camera_x, rect.y - camera_y, rect.width, rect.height))

    pygame.draw.circle(screen, (0, 0, 255), player_rect.center, 20)
    
    screen.blit(fuel_count, (0, 0))
    
    pygame.draw.circle(screen, (0, 0, 0), (int(origin_screen_x), int(origin_screen_y)), origin_radius)
    screen.blit(gen_charge, text_rect)


# ----------------------------
# End Game area
# ----------------------------
    if gen <= 0:
        screen.fill((0, 0, 0))
        timelasted = font.render(f"You lasted {time:.0f} seconds.", True, (255, 255, 255))
        game_over = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over, (0, 0))
        screen.blit(timelasted, (0, 50))
        control = False

    pygame.display.flip()
    clock.tick(50)


# ----------------------------
# Shutdown area
# ----------------------------
pygame.quit()
sys.exit()