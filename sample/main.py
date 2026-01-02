import pygame

pygame.init()

screen = pygame.display.set_mode([300,800])
running = True

while running:
    # Poll through all events.
    for event in pygame.event.get():
        # Did the player close the window?
        if event.type == pygame.QUIT:
            running = False

    # Define a light blue background.
    backgroundColor = (144,213,255)

    # Color in the background. 
    screen.fill(backgroundColor)

    # Define a black circle to represent the player.
    playerColor = (0,0,0)
    playerRadius = 25
    playerX = 250
    playerY = 250
    playerCenter = (playerX, playerY)

    # Draw the player.
    pygame.draw.circle(screen, playerColor, playerCenter, playerRadius)

    # Flip the display.
    pygame.display.flip()

pygame.quit()