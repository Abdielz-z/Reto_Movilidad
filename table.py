import Obstaculos

class table():
    def __init__(self, Carro):
        self.Carro = Carro
        self.Obstaculo = Obstaculos.Obstaculo(600).x
        
    def regreso(self):
        vx = self.Carro.vx
        x = self.Carro.x
        if(self.Obstaculo <= (x+(vx*15))):
            ddd = self.Obstaculo
        else:
            ddd = 9999
        
        self.Carro.update(ddd)
        
        return self.Carro.Carro_corre()