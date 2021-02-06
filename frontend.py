import backend
import time
import random
from playsound import playsound

playsound('Soundtrack.mp3',False)

bob = backend.player("2",{"speed":4,"hp":30,"damage":15,"attackRange":2},"","blue",0,[])
bob2 = backend.player("3",{"speed":6,"hp":30,"damage":15,"attackRange":4},"","blue",0,[])
enemy1 = backend.player("e1",{"speed":1,"hp":30,"damage":15,"attackRange":1},"","green",0,[])
enemy2 = backend.player("e1",{"speed":1,"hp":30,"damage":15,"attackRange":1},"","green",0,[])
enemy3 = backend.player("e1",{"speed":1,"hp":30,"damage":15,"attackRange":1},"","green",0,[])




players = [bob,bob2]
backend.getMouseInput()
enemy1.xpos = 5
enemy1.ypos = 5
enemy2.xpos = -5
enemy2.ypos = -5
enemy3.xpos = -5
enemy3.ypos = -5



enemies = [enemy1,enemy2,enemy3]


backend.drawGrid()
backend.textboxes()
selected = bob
a = 0
b = 0
while True:
    count = 0
    for player in range(len(players)):
        if backend.tilex == players[player].xpos and backend.tiley == players[player].ypos:
            players[players.index(selected)].turtl.clear()
            selected = players[player]
            count+=1
            players[players.index(selected)].highlightMoves(players+enemies)
            backend.tilex = 999
            backend.tiley = 999
    if count == 0:
        if backend.manhattanDistance(players[players.index(selected)].xpos,backend.tilex,players[players.index(selected)].ypos,backend.tiley)  <=  players[players.index(selected)].stats["speed"] and backend.manhattanDistance(players[players.index(selected)].xpos,backend.tilex,players[players.index(selected)].ypos,backend.tiley)>players[players.index(selected)].stats["attackRange"]:
            players[players.index(selected)].setLocation(backend.tilex,backend.tiley)
            (random.choice(enemies)).AImove(players)
            backend.tilex = 999
            backend.tiley = 999
        count2 = 0
        for enemy in enemies:
            if backend.manhattanDistance(players[players.index(selected)].xpos,backend.tilex,players[players.index(selected)].ypos,backend.tiley)<=players[players.index(selected)].stats["attackRange"] and backend.manhattanDistance(enemy.xpos,backend.tilex,enemy.ypos,backend.tiley) == 0:
                enemy.takeDamage(players[players.index(selected)].stats["damage"])
                (random.choice(enemies)).AImove(players)
                count2+=1
                time.sleep(1)
                enemy.turtl.clear()
                backend.tilex = 999
                backend.tiley = 999
        if count2==0:
            if  backend.manhattanDistance(players[players.index(selected)].xpos,backend.tilex,players[players.index(selected)].ypos,backend.tiley)<=players[players.index(selected)].stats["attackRange"]:
                players[players.index(selected)].setLocation(backend.tilex,backend.tiley)
                (random.choice(enemies)).AImove(players)
                backend.tilex = 999
                backend.tiley = 999
    for player in players:
        if player.stats["hp"]>0:
            player.displaySelf()
        if player.stats["hp"]<=0:
            player.turtl.clear()
            players.remove(player)
            if player == selected:
                selected = random.choice(players)
    for enemy in enemies:
        if  enemy.stats["hp"]>0:
            enemy.displaySelf()
            enemy.showHealth()
        if enemy.stats["hp"] <=0:
            enemy.turtl.clear()
            enemies.remove(enemy)
            playsound("Death.mp3")

