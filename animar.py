import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from Car import Carro
import table
import Carro


car = Carro.Carro(16.6667, 600)
tabla = table.table(car)
for i in range(1, 100):
    points = tabla.regreso()
#points = car.Carro_corre()
fig, ax = plt.subplots(1, 1)
fig.set_size_inches(15, 9)

#points = Carro(16.6667, 600)

def animate(i):
    ax.clear()
    # Get the point from the points list at index i
    point = points[i]
    # Plot that point using the x and y coordinates
    ax.plot(point[0], point[1], color='green', 
            label='original', marker='o')
    # Set the x and y axis to display a fixed range
    ax.set_xlim([0, 700])
    ax.set_ylim([0, 10])
    
ani = FuncAnimation(fig, animate, frames=len(points),
                    interval=66, repeat=False)
plt.show()