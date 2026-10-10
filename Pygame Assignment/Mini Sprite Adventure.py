import pygame
def main():
    pygame.init()
    Screen_width, Screen_height = 500,500

    screen= pygame.display.set_mode((Screen_width, Screen_height))
    pygame.display.set_caption("MINI SPRITE ADVENTURE")

    x= 50
    y=50
    sprite_width, sprite_height = 64,64
    speed = 5

    BLACK= (0,0,0)
    WHITE= (255,255,255)
    YELLOW= (255,255,0)
    GREEN= (0,255,0)
    PINK= (255,0,255)
    BROWN= (139,69,19)
    RED= (255,0,0)

    current_color= WHITE

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Pressed_keys = pygame.key.get_pressed()

        if Pressed_keys[pygame.K_LEFT]:
            x -= speed
  

        if Pressed_keys[pygame.K_RIGHT]:
            x += speed


        if Pressed_keys[pygame.K_UP]:
            y -= speed


        if Pressed_keys[pygame.K_DOWN]:
           y += speed
  

        x = min(max(x,0), Screen_width - sprite_width)
        y= min(max(y,0), Screen_height - sprite_height) 

        if x==0:
            current_color= GREEN
        elif x == Screen_width- sprite_width:
            current_color= PINK
        elif y == 0 :
            current_color= BROWN
        elif y == Screen_height- sprite_height:
            current_color= YELLOW
        else:
            current_color= WHITE
 
        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, (400,500), 50)
        pygame.draw.circle(screen, YELLOW, (80, 120), 50, 8)

        sprite_rect = pygame.Rect(x, y, sprite_width, sprite_height)
        pygame.draw.rect(screen, current_color, sprite_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


