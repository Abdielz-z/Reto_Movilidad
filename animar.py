import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from Car import Carro
import semaforo
import mamalon
import Carro
import math
import time



car1 = Carro.Carro(12, 9999, 100,0, 100, 0)
car2= Carro.Carro(8, 9999, 500, 0, 0, 0)
car3 = Carro.Carro(12, -9999, 1000, 3, 500, 180)
sem = semaforo.Sem(600, 100)
sem2 = semaforo.Sem(400, 500)
semaforos = [sem, sem2]
car = [car1, car2, car3]
tabla = mamalon.table(car, semaforos)

for i in range(1, 2500):
    points = tabla.regreso()

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(14, 7)



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
        
        ax.set_xlim([0, 1000])
        ax.set_ylim([0, 1000])
  
 

#print(points[0][25])
#print(points[2][27])
#print(points[2][25])


ani = FuncAnimation(fig, animate, frames=len(points[0]), interval=0.01, repeat=False)
inicio = time.time()
plt.show()
fin = time.time()
print(fin-inicio)