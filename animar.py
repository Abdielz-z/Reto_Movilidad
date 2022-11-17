import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from Car import Carro
import semaforo
import mamalon
import Carro

 
car1 = Carro.Carro(10, 9999, 0)
car2= Carro.Carro(8, 9999, 500)
car3 = Carro.Carro(10, 9999, 800)
sem = semaforo.Sem(1000)
semaforos = [sem]
car = [car1, car2, car3]
tabla = mamalon.table(car, semaforos)


for i in range(1, 325):
    points = tabla.regreso()
#for j in range(0, 18):
#    tabla.vuelta()
    
#for l in range(1, 20):
#    points =  tabla.broom()
    
#for k in range(1, 54):
#    tabla.vuelta()
    
#for l in range(1, 20):
 #   points =tabla.broom()
    
#points = car.Carro_corre()


fig, ax = plt.subplots(1, 1)
fig.set_size_inches(8, 4)

#points = Carro(16.6667, 600)

def animate(i):
    ax.clear()
    # Get the point from the points list at index i
    point = points[0][i]
    point2 = points[1][i]
    point3 = points[2][i]
    #print("Punto 1 ", point, " Punto 2 ", point2)
    # Plot that point using the x and y coordinates
    ax.plot(point[0], point[1], color='green', 
            label='original', marker='o')
    
    ax.arrow(point[0], point[1], (point[2]-point[0]-50), 0, head_width=32, head_length=50, fc='green', ec='green')
    
    ax.plot(point2[0], point2[1], color='blue', 
            label='original', marker='o')
    
    ax.arrow(point2[0], point2[1], (point2[2]-point2[0]-50), 0, head_width=32, head_length=50, fc='blue', ec='blue')
    
    ax.plot(point3[0], point3[1], color='red', 
            label='original', marker='o')
    
    ax.arrow(point3[0], point3[1], (point3[2]-point3[0]-50), 0, head_width=32, head_length=50, fc='red', ec='red')
    # Set the x and y axis to display a fixed range
    ax.set_xlim([0, 1500])
    ax.set_ylim([0, 1500])
    
ani = FuncAnimation(fig, animate, frames=len(points[0]),
                    interval=0.01, repeat=False)
plt.show()