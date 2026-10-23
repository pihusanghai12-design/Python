import pygame, random , math
pygame.init()

screen= pygame.display.set_mode((800,500))
pygame.display.set_caption("Sapce Invaders")

rocket= pygame.image.load("Rocket.png")
bullet= pygame.image.load("Bullet.png")
enemy= pygame.image.load("Enemy.png")
bg_image= pygame.image.load("Space.jpg")

rocket = pygame.transform.scale(rocket, (64, 64))

enemy = pygame.transform.scale(enemy, (64, 64))

bullet = pygame.transform.scale(bullet, (16, 32))

bg_image = pygame.transform.scale(bg_image, (800, 500))

player_x, player_y = 370, 380
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
    screen.blit(bg_image, (0,0))

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

    player_x += change_x
    player_x = max(0,min(player_x, 600))

    enemy_x += enemy_speed 
    if enemy_x <=0 or enemy_x >= 600:
        enemy_speed *= -1
        enemy_y += 40

    if bullet_state == "Fire":
        screen.blit(bullet, (bullet_x +16, bullet_y ))
        bullet_y -= 10

    if bullet_y <= 0:
        bullet_y = 380
        bullet_state= "ready"

    if collision(enemy_x, enemy_y, bullet_x, bullet_y):
        score +=1
        bullet_y = 380
        bullet_state= "ready"    
        enemy_x = random.randint(0,750)
        enemy_y = 100

    screen.blit(rocket, (player_x, player_y))  
    screen.blit(enemy, (enemy_x, enemy_y))

    text= font.render("Score= " + str(score), True, "White")
    screen.blit(text, (10,10) )

    pygame.display.update()  