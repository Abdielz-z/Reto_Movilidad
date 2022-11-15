import math

class Carro():
    def __init__(self, vl, ddd):
        self.v = 0
        self.vx = 0
        self.vy = 0
        self.vl = vl
        self.x = 0
        self.y = 250
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
        self.tiempo_control = 1
        self.angulo = 0
        self.ddd_pas = ddd
        
    def aceleracion(self, vl, ta):
        self.x = self.x + self.vx*self.tiempo_control
        self.y = self.y + self.vy*self.tiempo_control
        self.ax = (vl - self.v)/(ta)
        self.v = self.v + self.ax*self.tiempo_control
        self.vx = math.cos(math.radians(self.angulo)) * self.v
        self.vy = math.sin(math.radians(self.angulo)) * self.v
        
    
    def check_distance(self):
        self.di = self.ddd_pas - self.x + self.vx 
        self.df = self.ddd - self.x 
        self.v2 = round(((self.vx) + (self.df - self.di)))
        self.distancia = (self.vx * self.ta) - (self.v2*self.ta)
        print(self.distancia)

        self.aver = self.vx + ((self.vl - self.vx)/self.ta)

 
    def movimiento(self):
        self.check_distance()
        ta = self.ta
        if self.evitar == 999 or self.distancia < self.ddd-self.x-self.aver and self.evitar == 0:
            if self.start_lag < 7:
                ta = self.ta + 14 - 2*self.start_lag
                self.start_lag += 1
            self.aceleracion(self.vl, ta)
        else:
            self.evitar = 0
            vl = self.v2
            self.aceleracion(vl, ta)
        
    
    def reset(self):
        self.evitar = 999
    
    def turnleft(self):
        self.angulo = self.angulo + 5
        print(self.angulo)
    
    def update(self, ddd):
        if(self.ddd_pas == 9999):
            self.ddd_pas = ddd
        else:   
            self.ddd_pas = self.ddd
        self.ddd = ddd
        print(self.ddd, self.ddd_pas)
        
            
    def Carro_corre(self):
        self.movimiento()
        self.posiciones.append([self.x, self.y])
        print(self.x, self.vx)
        #print(self.ddd, self.ddd_pas ,self.di, self.df)
        #print(self.di, self.distancia, self.x, self.v2)
        return self.posiciones