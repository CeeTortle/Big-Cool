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
#draws a texture in a set of points
def texturePolygon(x,y,pointList,textureName,r):
    myPic=pygame.image.load(textureName).convert()
    myTexture=pygame.transform.rotate(myPic,-degrees(r)).convert_alpha(screen)
    #all the math is used to work around how livbrary handles the .textured_polygon
    pygame.gfxdraw.textured_polygon(screen,pointList,myTexture,int((-myTexture.get_width()+myPic.get_width())/2)+int(x)-int(myPic.get_width()/2),int((-myTexture.get_height()+myPic.get_height())/2)+int(-y)-int(myPic.get_height()/2))
#used to draw a rotatable rectangle
def drawRect(x,y,w,h,r,color):
    w=w/2
    h=h/2
    distance=sqrt(pow(w,2)+pow(h,2))
    pointList=[[-w,-h],[w,-h],[w,h],[-w,h]]
    #calculate rotation by calculating the angle from center for every point
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
    pygame.draw.polygon(screen,color,pointList)
    return pointList
#used to draw a rotatable rectangle with a texture
def drawTRect(x,y,w,h,r,textureName):
    w=w/2
    h=h/2
    distance=sqrt(pow(w,2)+pow(h,2))
    pointList=[[-w,-h],[w,-h],[w,h],[-w,h]]
    #calculate rotation by calculating the angle from center for every point
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
    #Call another function to draw an image inside the set of points(only works for quadrilaterals)
    texturePolygon(x,y,pointList,textureName,r)
    return pointList
def drawPoly(pointlist,color):
    pygame.gfxdraw.filled_polygon(screen,pointlist,color)
    '''textureName=pygame.image.load(textureName)
    myArray=pygame.PixelArray(textureName)
    print(myArray)
    myArray.close()
    screen.blit(myArray.surface,(100,100))'''
def getMouseAngle(x,y):
    mousePos=pygame.mouse.get_pos()
    #prevent division by 0
    if mousePos[0]-x==0:
        x=x+1
    #trig to find mouse angle
    if mousePos[0]-x>0:
        return atan((mousePos[1]-y)/(mousePos[0]-x))
    else:
        return atan((mousePos[1]-y)/(mousePos[0]-x))+pi

class renderClass():
    def __init__(self):
        self.roads=pygame.image.load("Untitled(1).png")
        self.applyTransform=False
        self.particleList=[]
        self.buildingList=[]
    def cameraPeriodic(self,cameraX,cameraY,scale):
        self.scale=int(1000*scale)
        self.cameraX=cameraX
        self.cameraY=cameraY
    def drawMap1(self):
        tileY=math.ceil(screen.get_height()/self.scale)+1
        tileX=math.ceil(screen.get_width()/self.scale)+1
        xOffset=self.cameraX%self.scale
        yOffset=self.cameraY%self.scale
        #Infinitlet draw roads
        self.buildingList.clear()
        if self.applyTransform==False:
            self.roads=pygame.transform.scale(self.roads,(self.scale,self.scale))
            self.applyTransform=True
        for i in range(tileY):
            y=(i*self.scale)-self.scale
            for l in range(tileX):
                x=(l*self.scale)-self.scale
                screen.blit(self.roads,(x+xOffset,y+yOffset))
                tileCenter=((-self.cameraX+xOffset)+x,(-self.cameraY+yOffset)+y)
                tileId=(tileCenter[0]/750,+tileCenter[1])
                #tileId[0] counts by 1's
                #tileId[1] counts by 750's
                if tileId[0]%3==0 and tileId[1]%1500==0:
                    self.drawBuilding(tileCenter[0],tileCenter[1],400,400,1.5)
                elif tileId[0]%4==0 and tileId[1]%2250==0:
                    self.drawBuilding(tileCenter[0]+200,tileCenter[1],200,500,1.1)
                    self.drawBuilding(tileCenter[0]-75,tileCenter[1]+190,300,125,1.1)
                    self.drawBuilding(tileCenter[0]-75,tileCenter[1]-190,300,125,1.1)
                else:
                    self.drawBuilding(tileCenter[0]-150,tileCenter[1]-150,250,250,1.1)
                    self.drawBuilding(tileCenter[0]-150,tileCenter[1]+150,250,250,1.1)
                    self.drawBuilding(tileCenter[0]+150,tileCenter[1]-150,250,250,1.1)
                    self.drawBuilding(tileCenter[0]+150,tileCenter[1]+150,250,250,1.1)
    def renderPeriodic(self):
        #Draw all dust paricles
        self.deletedParticles=0
        for i in range(len(self.particleList)):
            myList=self.particleList[i-self.deletedParticles]
            transparency=255-(pygame.time.get_ticks()-myList[2])/myList[3]
            if transparency<20: #uses transparency to kill the particle when it exceeds its duration
                self.particleList.pop(i-self.deletedParticles)
                self.deletedParticles+=1
            else:
                pygame.gfxdraw.filled_circle(screen,int(self.cameraX-myList[0]),int(self.cameraY-myList[1]+int(transparency/10)),myList[4],(222,184,135,transparency))
        #Draw all buildings
        for i in range(len(self.buildingList)):
            x,y,w,h,height=self.buildingList[i]
            bottomPoints=drawRect(x+self.cameraX,y+self.cameraY,w,h,0,"darkgrey")
            topPoints=drawRect((x+self.cameraX-screenWidth/2)*height+screenWidth/2,(y+self.cameraY-screenHeight/2)*height+screenHeight/2,w,h,0,"grey")
            for i in range(4):
                i=i-1
                drawPoly((bottomPoints[i],bottomPoints[i+1],topPoints[i+1],topPoints[i]),(50*(i+1),50*(i+1),50*(i+1)))
            drawRect((x+self.cameraX-screenWidth/2)*height+screenWidth/2,(y+self.cameraY-screenHeight/2)*height+screenHeight/2,w,h,0,"grey")
    def drawDustParticle(self,x,y,duration,size):
        startTime=pygame.time.get_ticks()
        self.particleList.append((x,y,startTime,duration,size))
    def drawBuilding(self,x,y,w,h,height):
        self.buildingList.append((x,y,w,h,height))
def giveVector(len,ang):
    ang=math.radians(ang)
    x=-sin(ang)*len
    y=cos(ang)*len
    return (x,y)
playerX,playerY=0,0
angList=[]
render=renderClass()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Turn key inputs into movement
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
        render.drawDustParticle(playerX-screenWidth/2,playerY-screenHeight/2,randint(2,5),randint(3,6))#draw particles when player is moving
    screen.fill("dark green")
    render.cameraPeriodic(playerX,playerY,0.75)
    render.drawMap1()
    render.renderPeriodic()
    #draw the player character
    drawTRect(screenWidth/2,screenHeight/2+25,50,50,getMouseAngle(screenWidth/2,screenHeight/2),"Untitled.png")
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()