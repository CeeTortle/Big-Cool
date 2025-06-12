import pygame
import math
from math import sin,cos,tan,pi,atan2
pygame.init()
screen = pygame.display.set_mode((1280, 720),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
scrW=screen.get_width()
scrH=screen.get_height()
scrS=min(scrW,scrH)
def drawElipse(x,y,max,e,pr,segments):
    #MIX(MINORAXIS) MAX(MAJORAXIS)
    mix=max*math.sqrt(1-e**2)
    fociOffset=math.sqrt(max**2-mix**2)
    step=(2*pi)/segments
    pointList=[]
    for i in range(segments):
        r=max*((1-e**2)/(1+e*cos(step*i)))
        pointList.append((sin(step*i+pr)*r+x+sin(pr)*2*fociOffset,cos(step*i+pr)*r+y+cos(pr)*2*fociOffset))
    pygame.draw.lines(screen,"cyan",True,pointList,1)
def orbitalCoord(x,y,max,e,pr,time):
    r=max*((1-e**2)/(1+e*cos(time)))
    mix=max*math.sqrt(1-e**2)
    fociOffset=math.sqrt(max**2-mix**2)
    return (sin(time+pr)*r+x+sin(pr)*2*fociOffset,cos(time+pr)*r+y+cos(pr)*2*fociOffset)
def orbitParamCalulator(mass,objSpeed,objCoordFromBod):
    angFromBod=atan2(objCoordFromBod[1],objCoordFromBod[0])
    totalSpeed=math.sqrt(objSpeed[0]**2+objSpeed[1]**2)
    speedAng=atan2(objSpeed[1],objSpeed[0])
    pass
x=0
while running:
    x=x+1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            scrW=screen.get_width()
            scrH=screen.get_height()
            scrS=min(scrW,scrH)
    screen.fill("black")
    drawElipse(scrW/2,scrH/2,scrS/2,0.5,pi/2,150)
    pygame.draw.circle(screen,"red",orbitalCoord(scrW/2,scrH/2,scrS/2,0.5,pi/2,x/200),4)    
    pygame.draw.circle(screen,"blue",(scrW/2,scrH/2),scrS/8)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()