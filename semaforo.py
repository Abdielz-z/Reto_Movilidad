class Sem():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.estado = 0
        self.i = 1
        
    def update(self):
        if self.i > 2600:
            self.estado = 1
            
        
        self.i = self.i + 1
       