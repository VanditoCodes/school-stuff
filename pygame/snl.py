import pygame
pygame.init()


win=pygame.display.set_mode((800, 600))
pygame.display.set_caption("snakes and ladders!")
x=5
y=585
width=10
height=10
vel=10

run=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
   

    keys=pygame.key.get_pressed()
    

    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
    if keys[pygame.K_RIGHT] and x<800-width-vel:
        x+=vel
    if keys[pygame.K_UP] and y>vel:
        y-=vel
    if keys[pygame.K_DOWN] and y<600-height-vel:
        y+=vel
    

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0),(x, y, width, height))
    pygame.display.update()
    
pygame.quit()  