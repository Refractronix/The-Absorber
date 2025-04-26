# --- The Absorber ---
# Made By: Refractronix
# Started: 2025 April 4
# Last Updated: 2025 April 4
# Version: 1.0.0

# Import the libraries.
import random
import pygame
import time

# Pygame Setup
pygame.init()
DISPLAY = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("The Absorber")

# Pygame Colors
PINK = (255, 0, 111)
RED = (255, 0, 0)
ORANGE = (255, 77, 0)
YELLOW = (255, 242, 0)
LIME_GREEN = (51, 255, 0)
GREEN = (36, 128, 13)
DARK_GREEN = (0, 100, 0)
SKY_BLUE = (0, 132, 255)
BLUE = (0, 0, 255)
PURPLE = (107, 16, 107)
BROWN = (59, 41, 10)
BLACK = (0, 0, 0)
GRAY = (112, 112, 112)
WHITE = (255, 255, 255)

# Player starting location
player_location_y = 200
player_location_x = 200 

# Player starting size
player_length = 50
player_width = 50

# Time system and running variable
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Add this after the event loop:
    keys = pygame.key.get_pressed()

    # Movment Controls (WASD)
    if keys[pygame.K_w]:
        player_location_y -= 3
    if keys[pygame.K_s]:
        player_location_y += 3
    if keys[pygame.K_a]:
        player_location_x -= 3
    if keys[pygame.K_d]:
        player_location_x += 3

    # Movment Controls (Arrow Keys)
    if keys[pygame.K_UP]:
        player_location_y -= 3
    if keys[pygame.K_DOWN]:
        player_location_y += 3
    if keys[pygame.K_LEFT]:
        player_location_x -= 3
    if keys[pygame.K_RIGHT]:
        player_location_x += 3
        
    # Makes character bigger or smaller (I) and (O)
    # I = Increase size, O = Decrease size
    # This is a test feature and will be removed in the final version
    if keys[pygame.K_i]:
        player_length += 3
        player_width += 3
    if keys[pygame.K_o]:
        player_length -= 3
        player_width -= 3

    # Player health
    player_health = 100

    # Background color
    DISPLAY.fill(BLACK)

    # Player character (Display)
    pygame.draw.rect(DISPLAY, WHITE, [player_location_x, player_location_y, player_length, player_width])

    # Player Health bar location
    player_health_bar_location_x = 50
    player_health_bar_location_y = 20

    # Player Health bar size
    player_health_bar_length = player_health * 2
    player_health_bar_width = 20

    # Player Health bar Border (Display)
    pygame.draw.rect(DISPLAY, DARK_GREEN, [player_health_bar_location_x -5, player_health_bar_location_y -5, player_health_bar_length + 10, player_health_bar_width + 10], 2)

    # Player Health bar (Display)
    pygame.draw.rect(DISPLAY, LIME_GREEN, [player_health_bar_location_x, player_health_bar_location_y, player_health_bar_length, player_health_bar_width])

    # Other setup
    clock.tick(60)
    pygame.display.flip()

# Closes program when the window is closed (I had no idea you had to do this)
pygame.quit()