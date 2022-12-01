import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from Car import Carro
import semaforo
import contSem
import mamalon
import Carro
import time
import json


#vl, ddd, x, vueltaa, y, angulo)

car1 = Carro.Carro(10, 80, 1, 0, 90, 0)
car2= Carro.Carro(10, 75, 2, 170, 270, 1)
car3 = Carro.Carro(10, 0, 0, 110, 0, 2)
sem = semaforo.Sem(80, 40,0)
sem2 = semaforo.Sem(75, 35,1)
sem3 = semaforo.Sem(75, 40,2)
sem4 = semaforo.Sem(80, 35,3)



semaforos = [sem, sem2, sem3, sem4]
sema0 = contSem.ContSem(0, "que te", semaforos)

sem = semaforo.Sem(80, 115, 10)
sem2 = semaforo.Sem(75, 110, 11)
sem3 = semaforo.Sem(75, 115, 12)
sem4 = semaforo.Sem(80, 110, 13)


semaforos = [sem, sem2, sem3, sem4]
sema1 = contSem.ContSem(1, "que te", semaforos)



sem = semaforo.Sem(175, 115, 20)
sem2 = semaforo.Sem(170, 110, 21)
sem3 = semaforo.Sem(170, 115, 22)
sem4 = semaforo.Sem(175, 110, 23)


semaforos = [sem, sem2, sem3, sem4]
sema2 = contSem.ContSem(2, "que te", semaforos)



semM = [sema0, sema1, sema2]

car = [car1, car2, car3]
tabla = mamalon.table(car, semM)

for i in range(1, 20):
    tabla.regreso()
    
points = tabla.imprime()

x = {
    "porfa":
        {
        "carros": points[0],
         "semaforos": points[1]
}
}

jsonStr = json.dumps(x)
print(jsonStr)

'''
fig, ax = plt.subplots(1, 1)
fig.set_size_inches(14, 7)


#print((points))



def animate(i):
        ax.clear()
        point = points[0][i]
        point2 = points[1][i]
        point3 = points[2][i]
        
        pp1 = point[2] - point[0]
        ppp1 = point[3] - point[1]
        pp2 = point2[2] - point2[0]
        ppp2 = point2[3] - point2[1]
        pp3 = point3[2] - point3[0]
        ppp3 = point3[3] - point3[1]    
        
        """ if(pp1 < 0):
            pp1 = 0
        if(pp2 < 0):
            pp2 = 0
        if(pp3 < 0):
            pp3 = 0
        if(ppp1 < 0):
            ppp1 = 0
        if(ppp2 < 0):
            ppp2 = 0
        if(ppp3 < 0):
            ppp3 = 0"""
        
        
        ax.plot(point[0], point[1], color='green', label='original', marker='o')

        ax.arrow(point[0], point[1], pp1, ppp1, head_width=32, head_length=50, fc='green', ec='green')
        ax.plot(point2[0], point2[1], color='blue', label='original', marker='o')
        ax.arrow(point2[0], point2[1], pp2, ppp2, head_width=32, head_length=50, fc='blue', ec='blue')
        ax.plot(point3[0], point3[1], color='red', label='original', marker='o')    
        ax.arrow(point3[0], point3[1], pp3, ppp3, head_width=32, head_length=50, fc='red', ec='red')
        
        ax.set_xlim([0, 300])
        ax.set_ylim([0, 300])
  
 


ani = FuncAnimation(fig, animate, frames=len(points[0]), interval=0.01, repeat=False)
inicio = time.time()
plt.show()
fin = time.time()
print(fin-inicio)'''