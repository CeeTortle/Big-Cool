import pygame
from math import sqrt,pow,atan,sin,cos,pi,degrees

import pygame.gfxdraw
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
screenWidth=screen.get_width()
screenHeight=screen.get_height()
def texturePolygon(pointList,textureName,r):
    myPic=pygame.image.load(textureName).convert()
    myTexture=pygame.transform.rotate(myPic,-degrees(r)).convert_alpha(screen)
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
def drawTRect(x,y,w,h,r,textureName):
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
    texturePolygon(pointList,textureName,r)
def getMouseAngle(x,y):
    mousePos=pygame.mouse.get_pos()
    if mousePos[0]-x==0:
        x=x+1
    if mousePos[0]-x>0:
        return atan((mousePos[1]-y)/(mousePos[0]-x))
    else:
        return atan((mousePos[1]-y)/(mousePos[0]-x))+pi

class map1():
    def __init__(self):
        self.roads=pygame.image.load("Untitled(1).png")
    def draw(self,cameraX,cameraY):
        xOffset=cameraX%1000
        yOffset=cameraY%1000
        for i in range(3):
            y=(i*1000)-1000
            for l in range(3):
                x=(l*1000)-1000
                screen.blit(self.roads,(x+xOffset,y+yOffset))
x=0
angList=[]
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_w:
            angList.append(0)
        if event.type == pygame.K_s:
            angList.append(180)
        if event.type == pygame.K_d:
            angList.append(90)
        if event.type == pygame.K_a:
            angList.append(270)
    sum=0
    for i in range(len(angList)):
        sum=sum+angList[i]
    if len(angList)!=0:
        sum/len(angList)
        angList.clear()
        print(sum)

    screen.fill("dark green")
    map1().draw(0,0)
    #draw rect
    x=x+5
    drawTRect(screenWidth/2,screenHeight/2,100,100,getMouseAngle(screenWidth/2,screenHeight/2)+pi/2,"Untitled.webp")
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()