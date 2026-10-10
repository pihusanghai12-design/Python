import pygame, random

pygame.init()


screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

bg_colors=["Red", "Green", "Blue", "Yellow"]
sprite_colors=["Orange", "Purple", "Pink", "Lightblue"]

x,y = random.randint(0,400),random.randint(0,370)
dx, dy = 4,4
sprite_color= random.choice(sprite_colors)
bg_color= random.choice(bg_colors)

running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += dx
    y +=dy

    if x <= 0 or x >=400:
        dx = -dx
        bg_color = random.choice(bg_colors)
        sprite_color = random.choice(sprite_colors)

    if y <=0 or y >=370:
        dy = -dy
        bg_color = random.choice(bg_colors)
        sprite_color = random.choice(sprite_colors) 

    screen.fill(bg_color)  
    pygame.draw.rect(screen, sprite_color, (x,y, 40, 60))

    pygame.display.update()
    clock.tick (90)

pygame.quit()            