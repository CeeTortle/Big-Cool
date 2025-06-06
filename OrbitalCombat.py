import pygame,math
from math import pi
pygame.init()
screen=pygame.display.set_mode((1280,720),pygame.RESIZABLE)
clock=pygame.time.Clock()
running=True
scrW=screen.get_width()
scrH=screen.get_height()
x=0
def rectMaker(x,y,w,h):
    pointList=[]
    for i in range(4):
        xCor=w/2
        yCor=h/2
        if i==1 or i==3:
            xCor=(-xCor)
        if i==2 or i==3:
            yCor=(-yCor)
        pointList.append([x+xCor,y+yCor])
    return pointList
if scrW<scrH:
    scwL=scrW
else:
    scrL=scrH
while running:
    x+=0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            scrW=screen.get_width()
            scrH=screen.get_height()
            if scrW<scrH:
                scwL=scrW
            else:
                scrL=scrH
    rectMaker(100,100,100,100)
    screen.fill("black")
    arcW=scrL/3
    arcH=scrL/2
    pygame.draw.arc(screen, "black", [210, 75, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen,"lightgreen",[scrW/2-arcW,scrH/2-arcH,arcW*2,arcH*2],0,90,2)
    pygame.draw.circle(screen,"red",(math.sin(x)*scrL/3+scrW/2,math.cos(x)*scrL/3+scrH/2),10)
    #pygame.draw.circle(screen,"blue",(scrW/2,scrH/2),scrL/4)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()