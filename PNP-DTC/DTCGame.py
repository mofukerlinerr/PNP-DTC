from tkinter import font
import pygame
import sys

# ----------------------------
# Startup area
# ----------------------------
pygame.init()

font = pygame.font.Font(None, 36)

gen = 100

player_speed = 5

playerX = 0
playerY = 50

time = 0
tick = 0

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("")

clock = pygame.time.Clock()
running = True

# ----------------------------
# Main game loop
# ----------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        playerY -= player_speed
        player_moving = True

    if keys[pygame.K_a]:
        playerX -= player_speed
        player_moving = True

    if keys[pygame.K_s]:
        playerY += player_speed
        player_moving = True

    if keys[pygame.K_d]:
        playerX += player_speed
        player_moving = True

    tick += 1
    time = tick/50

    for i in range(5):
        animation_frame = i

    player_an = pygame.image.load(f"playerstill{animation_frame}.png").convert_alpha()

    if player_moving == True:
        player_an = pygame.image.load(f"playermoving{animation_frame}.png").convert_alpha()

        

    

    if time >= 10:
        gen -= 0.02

    if gen <= 0:
        gen = 0
    
    screen.fill((255, 255, 255))

    screen.blit(player_an, (playerX, playerY, 50, 50))

    text_surface = font.render(f"{gen:.0f}", True, (0, 0, 0))
    screen.blit(text_surface, (400, 300))

    pygame.display.flip()
    clock.tick(50)

# ----------------------------
# Shutdown area
# ----------------------------
pygame.quit()
sys.exit()