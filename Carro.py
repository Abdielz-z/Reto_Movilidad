class Carro():
    def __init__(self, vl, ddd):
        self.vx = 0
        self.vl = vl
        self.x = 0
        self.ta = 10
        self.ax = 0
        self.v2 = 0
        self.start_lag = 0 #Cuando el carro este en 0 as esto
        self.posiciones = []
        self.ddd = ddd
        self.di = ddd
        self.df = ddd
        self.evitar = 0
        self.aver = 0
        self.distancia = 0
        
    def aceleracion(self, vl, ta):
        self.x = self.x + self.vx
        self.ax = (vl - self.vx)/(ta)
        self.vx = self.vx + self.ax
    
    def check_distance(self):
        self.di = self.ddd - self.x
        self.df = self.di - self.vx
        self.v2 = round(((self.vx) + (self.df - self.di)))
        self.distancia = (self.vx * self.ta) - (self.v2*self.ta)
        self.aver = self.vx + ((self.vl - self.vx)/self.ta)
 
    def movimiento(self):
        self.check_distance()
        ta = self.ta
        if self.distancia < self.ddd-self.x-self.aver and self.evitar == 0:
            if self.start_lag < 7:
                ta = self.ta + 14 - 2*self.start_lag
                self.start_lag += 1
            self.aceleracion(self.vl, ta)
        else:
            self.evitar = 1
            vl = self.v2
            self.aceleracion(vl, ta)
    
    def update(self, ddd):
        self.ddd = ddd
            
    def Carro_corre(self):
        self.movimiento()
        self.posiciones.append([self.x, 5])
        return self.posiciones