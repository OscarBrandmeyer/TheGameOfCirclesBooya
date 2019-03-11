from Sprite import Sprite

class raindrop(Sprite):
    
    speed = 8
    diameter = 20
    c = color(0,0,255)
    

        
    def move(self):
        self.y += self.speed
        if self.y < 0:
            self.speed *= -1
        if self.y > width:
            self.y = 0
        
