import pygame
import random

screen= pygame.display.set_mode((400,500))
pygame.display.set_caption("Sprite Collision")

pygame.init()

RED = ("Red")
GREEN = ("Green")

player= pygame.Rect(random.randint(0,200), random.randint(0,200),30,40)
target= pygame.Rect(random.randint(0,200), random.randint(0,200),20,50)

font= pygame.font.SysFont("Arial",30)

running= True
win= False

while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running= False

    if not win:
        keys= pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= 3
        if keys[pygame.K_RIGHT]:
            player.x += 3
        if keys[pygame.K_UP]:
            player.y -=3 
        if keys[pygame.K_DOWN]:
            player.y +=3 

        if player.colliderect(target):
            win = True 

    screen.fill("Yellow")   

    pygame.draw.rect(screen, RED, player)

    if not win:
        pygame.draw.rect(screen, GREEN, target)
    else:
        text= font.render("You Won!", True, "Black")
        screen.blit(text, (250, 100))    

    pygame.display.update()

pygame.quit()            
