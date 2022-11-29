class Sem():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.estado = 2
        self.i = 1
        
    def update(self):
        if 3000 > self.i > 2600:
            self.estado = 2
        if self.i > 3000:
            self.estado = 0
            self.i = 0    
        
        self.i = self.i + 1
       