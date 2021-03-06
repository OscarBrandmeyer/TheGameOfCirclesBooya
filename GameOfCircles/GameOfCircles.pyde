import platform
from Bullet import Bullet 
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from raindrop import raindrop
from jigglebot import jigglebot
from screensaverbot import screensaverbot

import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(Enemy(200, 50, 2))
    
    sprites.append(player)

    

                           
def draw():
    global player, sprites
    background(255)    

    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b) 
                    
    

    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
