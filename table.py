import Obstaculos

class table():
    def __init__(self, Carro):
        self.Carro = Carro
        self.vd = 0
        self.Obs = Obstaculos.Obstaculo(600, self.vd)
        self.Obstaculo = self.Obs.x
        self.posiciones = []
        
    def regreso(self):
        self.Obs.update(self.vd)
        self.Obstaculo = self.Obs.x
        v = self.Carro.vx 
        x = self.Carro.x
        if(self.Obstaculo <= (x+(v*15))):
            ddd = self.Obstaculo
        else:
            ddd = self.Obstaculo
        
        self.Carro.update(ddd)
        
        self.posiciones = self.Carro.Carro_corre()
        return self.posiciones
        
    def vuelta(self):
        self.Carro.update(9999)
        self.Carro.reset()
        self.Carro.turnleft()
        self.posiciones = self.Carro.Carro_corre()
        return self.posiciones
    
    def broom(self):
        self.posiciones = self.Carro.Carro_corre()
        return self.posiciones