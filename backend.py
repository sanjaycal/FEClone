import turtle
import math
import random

tilex = 0
tiley = 0


width = 16
height = 16


boxWidth = 26

halfBoxWidth = int(boxWidth/2)

def manhattanDistance(x1,x2,y1,y2):
    return abs(x1-x2)+abs(y1-y2)



class player:
    def __init__(self,name,stats,clss,color,xp,abilities):
        self.color = color
        self.name = name
        self.clss = clss
        self.stats = stats
        self.xp = xp
        self.abilities = abilities
        self.xpos = 0
        self.ypos = 0
        self.turtl = turtle.Turtle()
        self.turtl.speed(0)
        self.stats["maxHP"] = self.stats["hp"]
        

        
    def setLocation(self,x,y):
        if x != self.xpos or y != self.ypos:
            self.turtl.clear()
        self.xpos = x
        self.ypos = y

    def takeDamage(self,damage):
        self.stats["hp"] -= damage

    def AImove(self,players):
        closestPlayer = 0
        lowestDistance = 99999
        for player in players:
            if manhattanDistance(self.xpos,player.xpos,self.ypos,player.ypos)<lowestDistance:
                lowestDistance = manhattanDistance(self.xpos,player.xpos,self.ypos,player.ypos)
                closestPlayer = player
        if lowestDistance <= self.stats["attackRange"]:
            closestPlayer.takeDamage(self.stats["damage"])
        else:
            newx = self.xpos
            newy = self.ypos
            if self.xpos<closestPlayer.xpos:
                newx+=self.stats["speed"]
            elif self.xpos>closestPlayer.xpos:
                newx-=self.stats["speed"]
            if self.ypos<closestPlayer.ypos:
                newy+=self.stats["speed"]
            elif self.ypos>closestPlayer.ypos:
                newy-=self.stats["speed"]
            if newx == closestPlayer.xpos and newy == closestPlayer.ypos:
                newy -=1
            self.setLocation(newx,newy) 

    def showHealth(self):
        self.turtl.fillcolor("red")
        self.turtl.begin_fill()
        for i in range(2):
            self.turtl.fd(self.stats["hp"]*13/self.stats["maxHP"])
            self.turtl.lt(90)
            self.turtl.fd(5)
            self.turtl.lt(90)
        self.turtl.end_fill()
    
    def highlightMoves(self,playerList):
        lineSize = 5
        positions = []
        for player in playerList:
            positions.append([player.xpos,player.ypos])
        self.turtl.color(self.color)
        self.turtl.pensize(lineSize+4)
        self.turtl.speed(0)
        b= []
        for i in range(self.stats["speed"]*2+1):
            for j in range(self.stats["speed"]*2+1):
                if manhattanDistance(i-self.stats["speed"],0,j-self.stats["speed"],0)<=self.stats["speed"] and manhattanDistance(i-self.stats["speed"],0,j-self.stats["speed"],0)>1:
                    b.append([i-self.stats["speed"],j-self.stats["speed"]])
        for i in b:
            self.turtl.penup()
            self.turtl.goto(self.xpos*boxWidth+i[0]*boxWidth-boxWidth+lineSize,self.ypos*boxWidth+i[1]*boxWidth+boxWidth-lineSize)
            self.turtl.pendown()
            if not([i[0]+self.xpos,i[1]+self.ypos] in positions):
                for i in range(4):
                    self.turtl.fd(boxWidth-lineSize*2)
                    self.turtl.rt(90)
        b= []
        self.turtl.color("red")
        for i in range(self.stats["speed"]*2+1):
            for j in range(self.stats["speed"]*2+1):
                if manhattanDistance(i-self.stats["speed"],0,j-self.stats["speed"],0)<=self.stats["attackRange"]:
                    b.append([i-self.stats["speed"],j-self.stats["speed"]])
        for i in b:
            self.turtl.penup()
            self.turtl.goto(self.xpos*boxWidth+i[0]*boxWidth-boxWidth+lineSize,self.ypos*boxWidth+i[1]*boxWidth+boxWidth-lineSize)
            self.turtl.pendown()
            if not([i[0]+self.xpos,i[1]+self.ypos] in positions):
                for i in range(4):
                    self.turtl.fd(boxWidth-lineSize*2)
                    self.turtl.rt(90)
        self.turtl.pensize(1)

    def displaySelf(player):
        player.turtl.color(player.color)
        player.turtl.speed(0)
        player.turtl.penup()
        player.turtl.goto(player.xpos*boxWidth-halfBoxWidth,player.ypos*boxWidth)
        player.turtl.write(player.name)
        player.turtl.pendown()
        player.turtl.circle(halfBoxWidth)

class ability:
    def __init__(self, activation, effect):
        self.activation = activation
        self.effect = effect



def drawGrid():
    t = turtle.Turtle()
    t.speed(0)
    for i in range(height):
        t.goto(width*halfBoxWidth,i*boxWidth-height*halfBoxWidth)
        t.goto(width*halfBoxWidth,(i+1)*boxWidth-height*halfBoxWidth)
        t.goto(-width*halfBoxWidth,i*boxWidth+boxWidth-height*halfBoxWidth)
    for i in range(width):
        t.goto(i*boxWidth-width*halfBoxWidth,height*halfBoxWidth)
        t.goto((i+1)*boxWidth-width*halfBoxWidth,height*halfBoxWidth)
        t.goto(i*boxWidth+boxWidth-width*halfBoxWidth,-height*halfBoxWidth)
    t = 0


def textboxes():
    t2 = turtle.Turtle()
    t = turtle.Turtle()
    t.speed(0)
    t.fd(8*boxWidth)
    t.rt(90)
    t.color("Grey")
    t.begin_fill()
    t.fd(8*boxWidth)
    t.fd(6*boxWidth)
    t.rt(90)
    t.fd(16*boxWidth)
    t.rt(90)
    t.fd(6*boxWidth)
    t.rt(90)
    t.fd(16*boxWidth)
    t.end_fill()
    t.rt(90)
    t.fd(6*boxWidth)
    t.rt(90)
    t.fd(16*boxWidth)
    t.rt(90)
    t.fd(15)
   
   
    t.rt(90)
    t.fd(15)
    t.color("Sky Blue")
    t.ht()
    t2.fd(8*boxWidth)
    t2.rt(90)
    t2.speed(0)
    t2.color("Grey")
    t2.begin_fill()
    t2.fd(8*boxWidth)
    t2.fd(6*boxWidth)
    t2.rt(90)
    t2.fd(16*boxWidth)
    t2.rt(90)
    t2.fd(6*boxWidth)
    t2.rt(90)
    t2.fd(16*boxWidth)
    t2.rt(90)
    t2.fd(6*boxWidth)
    t2.rt(90)
    t2.fd(16*boxWidth)
    t2.rt(90)
    t2.fd(15)
    t2.rt(90)
    t2.fd(15)
    t2.color("Sky Blue")
    t2.ht()
    t2.write("To Play The Game Type Something Random If You Want To\nSee Directions Type 'R'",font=("Arial", 16, "normal"))
    a=input()
    if a=="R":
        t3 = turtle.Turtle()
        t2.clear()
        t2 = 0
        t3.speed(0)
        t3.fd(8*boxWidth)
        t3.rt(90)
        t3.color("Grey")
        t3.fd(8*boxWidth)
        t3.fd(6*boxWidth)
        t3.rt(90)
        t3.fd(16*boxWidth)
        t3.rt(90)
        t3.fd(6*boxWidth)
        t3.rt(90)
        t3.fd(16*boxWidth)
        t3.rt(90)
        t3.fd(6*boxWidth)
        t3.rt(90)
        t3.fd(16*boxWidth)
        t3.rt(90)
        t3.fd(15)
        t3.rt(90)
        t3.fd(15)
        t3.ht()
        t3.color("Sky Blue")
        t3.write("The Directions Are That",font=("Impact", 16, "normal"))
    else:
        t3 = turtle.Turtle()
        t2.clear()
        t2 = 0
        t3.speed(0)
        t3.fd(8*boxWidth)
        t3.rt(90)
        t3.color("Grey")
        t3.fd(8*boxWidth)
        t3.fd(6*boxWidth)
        t3.rt(90)
        t3.fd(16*boxWidth)
        t3.rt(90)
        t3.fd(6*boxWidth)
        t3.rt(90)
        t3.fd(16*boxWidth)
        t3.rt(90)
        t3.fd(6*boxWidth)
        t3.rt(90)
        t3.fd(16*boxWidth)
        t3.rt(90)
        t3.fd(15)
        t3.rt(90)
        t3.fd(15)
        t3.ht()
        t3.color("Sky Blue")
        t3.write("You Have Started The Game Good Luck! ",font=("Impact", 16, "normal"))


def clearScreen():
    turtle.clearscreen()

def getMouseInput():
    turtle.onscreenclick(storeMouseInput)

def storeMouseInput(x,y):
    global tilex
    global tiley
    tilex = int(math.ceil(x/boxWidth))
    tiley = int(math.floor(y/boxWidth))
    print([tilex,tiley])



