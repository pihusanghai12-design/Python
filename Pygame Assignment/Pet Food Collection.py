import pygame
import random

screen= pygame.display.set_mode((400,500))
pygame.display.set_caption("Pet Food Collection")

pygame.init()

Snake = pygame.transform.scale(
    pygame.image.load("Snake.jpg").convert_alpha(), (50, 50)
   
) 
Food = pygame.transform.scale(
    pygame.image.load("Food.jpg").convert_alpha(), (35, 35)
    
)

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

        player.clamp_ip(screen.get_rect())    

    screen.fill("Yellow")

    screen.blit(Snake, player)

    if not win:
        screen.blit(Food, target)
    else:
        text = font.render("You Won!", True, "Black")
        screen.blit(text, (120, 100))

    pygame.display.update()

pygame.quit()            
