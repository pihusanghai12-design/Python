import pygame
pygame.init()

screen= pygame.display.set_mode((500,600))
done= False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, "Red", pygame.Rect(100, 100, 200, 200))        

    pygame.display.flip()