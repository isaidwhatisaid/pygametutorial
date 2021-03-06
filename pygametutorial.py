import pygame

# The pygame library needs to be initialised
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((800,600))

# Window Title
pygame.display.set_caption("Doug Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Game run loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False 
    
    screen.fill((0,100,100))
    pygame.display.update()
