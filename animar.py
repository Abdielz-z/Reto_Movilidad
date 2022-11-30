import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from Car import Carro
import semaforo
import contSem
import mamalon
import Carro
import time


#vl, ddd, x, vueltaa, y, angulo)
car1 = Carro.Carro(12, 100, 1, 100, 0, 0)
car2= Carro.Carro(6, 500, 2, 1000, 270, 1)
car3 = Carro.Carro(10, 1000, 0, 500, 180, 2)
sem = semaforo.Sem(600, 100,0)
sem2 = semaforo.Sem(400, 500,1)
sem3 = semaforo.Sem(500, 300,2)
sem4 = semaforo.Sem(608, 800,3)

semaforos = [sem, sem2, sem3, sem4]

sem = contSem.ContSem(0, "que te", semaforos)

semM = [sem]

car = [car1, car2, car3]
tabla = mamalon.table(car, semM)

for i in range(1, 1000):
    tabla.regreso()
    
points = tabla.imprime()

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(14, 7)


print((points[1][0][0]))


'''def animate(i):
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
  
 

print(points[0][33])
print(points[2][33])
print(points[2][33])


ani = FuncAnimation(fig, animate, frames=len(points[0]), interval=0.01, repeat=False)
inicio = time.time()
plt.show()
fin = time.time()
print(fin-inicio)'''