import pygame
from math import sqrt,pow,atan,sin,cos,pi,degrees
import math
from random import randint
import pygame.gfxdraw
pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
running = True
screenWidth=screen.get_width()
screenHeight=screen.get_height()
def texturePolygon(pointList,textureName,r):
    myPic=pygame.image.load(textureName).convert()
    myTexture=pygame.transform.rotate(myPic,-degrees(r)).convert_alpha(screen)
    pygame.gfxdraw.textured_polygon(screen,pointList,myTexture,int((-myTexture.get_width()+myPic.get_width())/2)+int(screenWidth/2)-int(myPic.get_width()/2),int((-myTexture.get_height()+myPic.get_height())/2)+int(-screenHeight/2)-int(myPic.get_height()/2))
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

class renderClass():
    def __init__(self):
        self.roads=pygame.image.load("Untitled(1).png")
        self.applyTransform=False
        self.particleList=[]
    def cameraPeriodic(self,cameraX,cameraY,scale):
        self.scale=int(1000*scale)
        self.cameraX=cameraX
        self.cameraY=cameraY
        for i in range(len(self.particleList)):
            deletedParticles=0
            myList=self.particleList[i-deletedParticles]
            transparency=255-(pygame.time.get_ticks()-myList[2])/myList[3]
            if transparency<20:
                self.particleList.pop(i)
                deletedParticles+=1
            else:
                pygame.gfxdraw.filled_circle(screen,int(self.cameraX-myList[0]),int(self.cameraY-myList[1]+int(transparency/10)),myList[4],(222,184,135,transparency))
    def drawMap1(self):
        tileY=math.ceil(screen.get_height()/self.scale)+1
        tileX=math.ceil(screen.get_width()/self.scale)+1
        xOffset=self.cameraX%self.scale
        yOffset=self.cameraY%self.scale
        if self.applyTransform==False:
            self.roads=pygame.transform.scale(self.roads,(self.scale,self.scale))
            self.applyTransform=True
        for i in range(tileY):
            y=(i*self.scale)-self.scale
            for l in range(tileX):
                x=(l*self.scale)-self.scale
                screen.blit(self.roads,(x+xOffset,y+yOffset))
    def drawParticle(self,x,y,duration,size):
        startTime=pygame.time.get_ticks()
        self.particleList.append((x,y,startTime,duration,size))
def giveVector(len,ang):
    ang=math.radians(ang)
    x=-sin(ang)*len
    y=cos(ang)*len
    return (x,y)
playerX,playerY=0,0
angList=[]
render=renderClass()
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        angList.append(0)
    if keys[pygame.K_s]:
         angList.append(180)
    if keys[pygame.K_d]:
        angList.append(90)
    if keys[pygame.K_a]:
         angList.append(270)
    sum=0
    movement=(0,0)
    for i in range(len(angList)):
        sum=sum+angList[i]
    if len(angList)!=0:
        sum=sum/len(angList)
        if angList==[0,270]:
            sum=315
        angList.clear()
        movement=giveVector(10,sum)
        playerX=movement[0]+playerX
        playerY=movement[1]+playerY
    if pygame.time.get_ticks()%100==0:
        render.drawParticle(playerX,playerY,randint(10,20),randint(3,6))
    screen.fill("dark green")
    render.cameraPeriodic(playerX,playerY,0.75)
    render.drawMap1()
    #draw rect
    drawTRect(screenWidth/2,screenHeight/2,50,50,getMouseAngle(screenWidth/2,screenHeight/2),"Untitled.png")
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()