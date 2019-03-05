import SpriteManager
from Sprite import Sprite
from Bullet import Bullet
from Player import Player
mark = 0
wait = 1000
go = True

class Enemy(Sprite):
    
    speed = 8
    diameter = 50
    c = color(0, 0, 255)

    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
        
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)

    def aim(self, target):
        # solve unit vector problem too
        xcomp = target.x - self.x
        ycomp = target.y - self.y
        xVec = xcomp / 2 * .1
        yVec = ycomp / 2 * .1
        return PVector(xVec, yVec)
         
        d = ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** .5
    
        return PVector(0, 10)
        
    def fire(self, vector):
        
        
        global go, mark, wait
        if(millis() - mark > wait):
            go = not go
            mark = millis()
        if(go): 
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
        
