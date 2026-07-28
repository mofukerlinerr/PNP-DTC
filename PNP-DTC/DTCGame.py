import pygame
import sys

# ----------------------------
# Startup area
# ----------------------------
pygame.init()

player_speed = 5

playerX = 50
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

    if keys[pygame.K_a]:
        playerX -= player_speed

    if keys[pygame.K_s]:
        playerY += player_speed

    if keys[pygame.K_d]:
        playerX += player_speed

    pygame.display.set_caption("Pygame Text Example")

    tick += 1

    time = tick/60
    
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), (playerX, playerY, 50, 50))

    pygame.display.flip()
    clock.tick(60)

# ----------------------------
# Shutdown area
# ----------------------------
pygame.quit()
sys.exit()