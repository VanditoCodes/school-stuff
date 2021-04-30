import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Here we go!") 

x = 0
y = 500

width = 10
height = 10
vel = 50

screenwidth = 500
screenheight = 500

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.draw.rect(win,(255,245,4), (x, y, width, height))
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>vel :
         x -= vel
    if keys[pygame.K_RIGHT]and x<screenwidth-width-vel:
        x += vel
    if keys[pygame.K_UP] and y>vel :
        y -= vel
    if keys[pygame.K_DOWN] and y<screenheight-height-vel:
        y += vel

    win.fill((0,0,0))
        
pygame.quit()
                                
        
