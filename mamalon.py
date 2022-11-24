import Obstaculos
import math

class table():
    def __init__(self, Carros, semaforos):
        self.Carros = Carros
        self.posiciones = [[],[],[]]
        self.sema = semaforos
        self.vuelta = 90
        self.count = 0
        
    def regreso(self):
        i = 0
        for sem in self.sema:
            sem.update()
        for car in self.Carros:
            
            if car.v != 0:
                v = car.v
            else:
                v = 1
                
            if car.superx == 1:
                powerx = 1
            else:
                powerx = -1
            if car.supery == 1:
                powery = 1
            else:
                powery = -1
            x = car.x * powerx
            y = car.y * powery

                
            card = math.sqrt((x**2) + (y**2))
            pointing = 0
            
            if car.angulo == 0 or car.angulo ==  180:
                limite = car.y
                usa = x
            else:
                limite = car.x
                usa = y
            
            
            distancia = 9999
            
            if usa >= 0:
                distancia = 9999
            else:
                distancia = 9999
            xx = 9999 * powerx
            yy = 9999 * powery
            
            
                
            
            """for car2 in self.Carros:
                x2 = car2.x
                y2 = car2.y
                
                dis = math.sqrt((x2*x2)+(y2*y2))
                
                if car.angulo == 0 or car.angulo ==  180:
                    limi = y2
                    usada = x2
                else:
                    limi = x2
                    usada = y2
                
                if usa <= usada  and dis <= distancia and car != car2 and limi - limite == 0 :# and car2.x-car.x <= v*15: 
                    pointing = 0
                    xx = x2
                    yy = y2
                    if car.v == 0:
                        distancia = dis
                    elif car.vy == 0:
                        distancia = xx
                    elif car.vx == 0:
                        distancia = yy
                    elif car.angulo == 0:
                        distancia = xx
                    elif xx-x > yy-y:
                        distancia = yy
                    else:
                        distancia = xx
                        
                if i == 0 and self.count <100:
                    print(distancia)"""
                    
            
            for sem in self.sema:
                x2 = sem.x * powerx
                y2 = sem.y * powery
                dis = math.sqrt((x2*x2)+(y2*y2))
                
                if car.angulo == 0 or car.angulo ==  180:
                    limi = sem.y
                    dis = x2
                else:
                    limi = sem.x
                    dis = y2
                    
               
                    
                    
                if usa < dis and dis <= distancia and sem.y == car.y:
                    if(sem.estado == 0):
                        pointing = 0
                        xx = x2*powerx
                        yy = y2*powery
                        if car.v == 0:
                            distancia = dis
                        elif car.vy == 0:
                            distancia = sem.x
                        elif car.vx == 0:
                            distancia = sem.y
                        elif car.angulo == 0 or car.angulo == 180:
                            distancia = sem.x
                        elif car.angulo == 90 or car.angulo == 270:
                            distancia = sem.y
                        elif xx-x > yy-y:
                            distancia = sem.y
                        else:
                            distancia = sem.x
                    else:
                        pointing = 1
                        xx = 9999 * powerx
                        yy = 9999 * powery
                        distancia = 9999

                        
            """if math.sqrt((dis - usa)**2) > v*50:
                xx = math.cos(math.radians(car.angulo)) * 9999
                yy = math.sin(math.radians(car.angulo)) * 9999 
                
                if usa >= 0:                    
                    distancia = 9999 #maybe
                else:
                    distancia = 9999 * -1 #maybe"""
                                
            self.count = self.count + 1                
            ddd = distancia
            
            car.update(ddd, xx, yy, pointing)
            self.posiciones[i] = car.Carro_corre()
            i += 1
        
        return self.posiciones
       