import pygame, random , math
pygame.init()

screen= pygame.display.set_mode((800,500))
pygame.display.set_caption("Sapce Invaders")

rocket= pygame.image.load("Rocket.png")
bullet= pygame.image.load("Bullet.png")
enemy= pygame.image.load("Enemy.png")
bg_image= pygame.image.load("Space.jpg")

player_x, player_y = 370, 300
change_x= 0

enemy_x= random.randint(0,750)
enemy_y= 100
enemy_speed= 4

bullet_x, bullet_y= 0, 380
bullet_state="ready"

score= 0 
font= pygame.font.SysFont("Arial",30)

def collision(ex,ey, bx, by):
    return math.sqrt((ex- bx)**2 +(ey- by)**2) <27

running= True

while running:
    screen.blit(bg_image (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = -5
            if event.key == pygame. K_RIGHT:
                change_x = 5 
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x 
                bullet_state= "Fire"

        if event.type == pygame.KEYUP:
            change_x = 0          


