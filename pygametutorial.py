import pygame
import random

# The pygame library needs to be initialised
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((800,600))

# Window Title
pygame.display.set_caption("Doug Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('player.png')
player_x = 368
player_y = 480
player_x_change = player_y_change = 0
# Player function that draws the player in the right position
def player(x, y):
    screen.blit(player_img, (x, y))

# Grunt Enemy
grunt_img = pygame.image.load('enemy_grunt.png')
grunt_x = random.randint(10, 780)
grunt_y = random.randint(10, 580)
grunt_x_change = grunt_y_change = 0.1

# Player function that draws the player in the right position
def grunt(x, y):
    screen.blit(grunt_img, (x, y))


# Game run loop
running = True
while running:
    
    # Fill the screen background colour
    screen.fill((52,210,235))
    
    for event in pygame.event.get():

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.1
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.1
            if event.key == pygame.K_UP:
                player_y_change = -0.1
            if event.key == pygame.K_DOWN:
                player_y_change = 0.1
        # Stop movement if key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0

        # Quit program condition
        if event.type == pygame.QUIT:
           running = False 

    # Move the player based on key inputs so that the player icon can be redrawn using the player function at the new location
    player_x += player_x_change
    player_y += player_y_change
    # Stop player from moving beyond the borders
    if player_x <= 0:
        player_x = 0
    if player_x >= 736:
        player_x = 736
    if player_y <= 0:
        player_y = 0
    if player_y >= 536:
        player_y = 536

    # Move the grunt enemy type by bouncing them around the screen
    grunt_x += grunt_x_change
    grunt_y += grunt_y_change
    # Stop grunts from moving beyond the borders
    if grunt_x <= 0:
        grunt_x_change = 0.1
    if grunt_x >= 768:
        grunt_x_change = -0.1
    if grunt_y <= 0:
        grunt_y_change = 0.1
    if grunt_y >= 568:
        grunt_y_change = -0.1
    
    # Call the player function
    player(player_x, player_y)

    # Call the enemy functions
    grunt(grunt_x, grunt_y)
    
    
    # Update the screen with everything that's happened each loop
    pygame.display.update()
