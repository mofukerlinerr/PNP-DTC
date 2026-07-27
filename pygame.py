import pygame
import sys

# ----------------------------
# Startup area
# ----------------------------
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Starter Game")

clock = pygame.time.Clock()
running = True

# ----------------------------
# Main game loop
# ----------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Draw everything
    screen.fill((0, 0, 0))  # clear screen

    pygame.display.flip()
    clock.tick(60)

# ----------------------------
# Shutdown area
# ----------------------------
pygame.quit()
sys.exit()