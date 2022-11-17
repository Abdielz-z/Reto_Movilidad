import Obstaculos

class table():
    def __init__(self, Carros, semaforos):
        self.Carros = Carros
        self.posiciones = [[],[],[]]
        self.sem = semaforos
        
    def regreso(self):
        i = 0
        for sem in self.sem:
            sem.update()
        for car in self.Carros:
            #if i == 0:
                #print("Carro 1 ", car.vx)
            if car.v != 0:
                v = car.v 
            else:
                v = 1
            
            x = car.x
            distancia = 9999

            for car2 in self.Carros:
                if car.x <= car2.x  and car2.x-10 <= distancia and car != car2:# and car2.x-car.x <= v*15: 
                    distancia = car2.x
                    print("Distancia 1 0 ", distancia)
            
            for sem in self.sem:
                if x <= sem.x and sem.x - 10 <= distancia and sem.estado == 0 and sem.x-car.x:# and sem.x-car.x <= v*100:
                    distancia = sem.x
                    #print("Distancia 2 ", distancia)
            

            if distancia - car.x <= v*15:
                ddd = 9999
            
                                
            ddd = distancia

            #print("Carro: ", i, " ddd: ", ddd, "x: ", x)
            
            car.update(ddd)
            self.posiciones[i] = car.Carro_corre()
            i += 1
        
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