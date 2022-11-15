
'''

ES DE MI PLACER INFORMARLES QUE YA EMOS EVOLUCIONADO A LA VERSION 2.0 DE NUESTRO 
PROGRAMA. ESTA ES LA VERSION ANTERIOR, ES MAS SENCILLA DE ENTENDER PERO NO ES
CON LA QUE ESTAMOS TRABAJANDO ACTUALMENTE. EN LA NUEVA VERSION HEMOS MOVIDO
TODO EL CODIGO A UNA CLASE LLAMADA "Carro" PARA EMPEZAR A TRABAJAR CON OBJETOS.


ALV EL COPILOT TRABAJO BIEN CHIDO, HASTA ME AUTOCOMPLETO ESTE MENSAJE.



'''
import time

def aceleracion(ax, v, x, ta,vl):
    x = x + v
    ax = (vl - v)/(ta)
    v = v + ax
    return ax, v, x

def check_distance(v, ta, di, df, x, ddd, vl):
    di = ddd - x
    df = di - v
    tf = 1
    v2 = round(((v * tf) + (df - di)/tf))
    distancia = (v * ta) - (v2*ta)
    aver = v + ((vl - v)/ta)
    return distancia, v2, di, df, aver



def movimiento(x, ta, v, ax, vl, di, df, v2, start_lag, ddd, evitar):    
    distancia, v2, di, df, aver = check_distance(v, ta, di, df, x, ddd, vl)
    if distancia < ddd-x-aver and evitar == 0:
        if start_lag < 8:
            ta = ta + 16 - 2*start_lag
            start_lag += 1
        ax, v, x = aceleracion(ax, v, x, ta, vl)
        return ax, v, x, di, df, start_lag, evitar
    else:
        evitar = 1
        vl = v2
        ax, v, x = aceleracion(ax, v, x, ta, vl)
        
        return ax, v, x, di, df, start_lag, evitar

def Carro(vl, ddd):
    v = 0
    x = 0
    ta = 10
    ax = 0
    v2 = 0
    start_lag = 0 #Cuando el carro este en 0 as esto
    posiciones = []
    di = ddd
    df = ddd
    evitar = 0
    
    for i in range(0, 100):
        ax, v, x, di, df, start_lag, evitar = movimiento(x, ta, v, ax, vl, di, df, v2, start_lag, ddd, evitar)
        #print(str(i)+": "+str(round(v)))
        #print(x)
        posiciones.append([x, 5])
        #time.sleep(0.1)
    
    #return(x)
    print(x)
    return posiciones
