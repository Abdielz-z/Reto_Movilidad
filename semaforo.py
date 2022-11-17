class Sem():
    def __init__(self, x):
        self.x = x
        self.estado = 0
        self.i = 0
        
    def update(self):
        if self.i > 250:
            self.estado = 1
        self.i = self.i + 1
       