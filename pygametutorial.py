import pygame
import random
import math

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
player_width = 64
player_x = 368
player_y = 480
player_x_change = player_y_change = 0
# Player function that draws the player in the right position
def player(x, y):
    screen.blit(player_img, (x, y))

# Grunt Enemy
grunt_img = pygame.image.load('enemy_grunt.png')
grunt_width = 32
grunt_x = random.randint(10, 780)
grunt_y = random.randint(10, 580)
grunt_x_change = grunt_y_change = 0.1
# Grunt function that draws the grunt enemy type in the right position
def grunt(x, y):
    screen.blit(grunt_img, (x, y))

# Bullet
bullet_img = pygame.image.load('bullet.png')
bullet_width = 16
bullet_x = player_x + 24
bullet_y = player_y
bullet_y_change = -0.5
# Ready state - can't see the bullet yet
bullet_state = 'ready'
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_img, (x, y))

# Collision Detection Function
score = 0
def is_collision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game run loop
running = True
while running:
    
    # Fill the screen background colour
    screen.fill((52,100,235))
    
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
            # Fire bullet when space is pressed, so long as no other bullet is on the screen
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_x = player_x + 24
                    bullet_y = player_y
                    fire_bullet(bullet_x, bullet_y)
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
    
    # Bullet firing
    if bullet_y <= -20:
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y += bullet_y_change
    
    # Collision action
    collision = is_collision((grunt_x + grunt_width/2), (grunt_y + grunt_width/2), (bullet_x + bullet_width/2), (bullet_y + bullet_width/2))
    if collision:
        bullet_x = player_x + 24
        bullet_y = player_y
        bullet_state = 'ready'
        score += 1
        print(score)

    
    # Call the player function
    player(player_x, player_y)

    # Call the enemy functions
    grunt(grunt_x, grunt_y)
    
    
    # Update the screen with everything that's happened each loop
    pygame.display.update()
