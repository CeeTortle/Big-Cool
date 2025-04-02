import pygame
from math import sqrt,pow,atan,sin,cos,pi,degrees

import pygame.gfxdraw
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
screenWidth=screen.get_width()
screenHeight=screen.get_height()
def texturePolygon(pointList):
    myPic=pygame.image.load("Untitled.webp").convert()
    myTexture=pygame.transform.rotate(myPic,-degrees(x)).convert_alpha(screen)
    screen.blit(myTexture,(int((-myTexture.get_width()+myPic.get_width())/2),int((-myTexture.get_height()+myPic.get_height())/2)))
    print(myPic.get_width(),myPic.get_height())
    pygame.gfxdraw.textured_polygon(screen,pointList,myTexture,int((-myTexture.get_width()+myPic.get_width())/2)+int(screenWidth/2)-int(193/2),int((-myTexture.get_height()+myPic.get_height())/2)+int(-screenHeight/2)-int(112/2))
#Custom fucntion to draw a rotatable rectangle
def drawRect(x,y,w,h,r):
    w=w/2
    h=h/2
    distance=sqrt(pow(w,2)+pow(h,2))
    pointList=[[-w,-h],[w,-h],[w,h],[-w,h]]
    #calculate rotation
    for i in pointList:
        angle=atan(h/w)
        if i[0]<0 and i[1]<0:
            angle=pi+angle
        elif i[1]<0:
            angle=2*pi-angle
        elif i[0]<0:
            angle=pi-angle
        i[0]=cos(angle+r)*distance+x
        i[1]=sin(angle+r)*distance+y
    pygame.draw.polygon(screen,"red",pointList)
    texturePolygon(pointList)
def drawTRect()
class map1():
    pass
x=0
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    pygame.draw.circle(screen,"blue",[100,100],100)
    #draw rect
    drawRect(screenWidth/2,screenHeight/2,300,100,x)
    x=x+0.01
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()