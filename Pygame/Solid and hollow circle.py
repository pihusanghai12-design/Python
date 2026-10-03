import pygame

pygame.init()

screen= pygame.display.set_mode((500,500))
screen.fill((255,150,155))
done= False

color1= ("Yellow")
color2= ("Blue")

pygame.draw.circle(screen, color1, (200,300), 50)
pygame.draw.circle(screen, color2, (200,300), 50, 10)

pygame.display.update()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            running = False

pygame.quit()        

