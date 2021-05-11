import numpy as np
cantObjetos = []
Presupuesto = 0



"""limite de stock del producto"""
cantidadMaxima = [2, 4, 10, 9, 20]



peso = [25, 15, 8, 7, 5]
"""ranking del producto donde el mas comprado es el menor y el mayor es el menos comprado"""
valor = [5, 4, 3, 2, 1]
guardados = [0]

def contarGanancia():
    for i in range(len(peso)):
        pesoActual = peso[i]
        gananciaActual = valor[i]
        for j in range(Presupuesto, pesoActual-1, -1):
            cantObjetos[j] = max(cantObjetos[j], cantObjetos[j-pesoActual]+gananciaActual)


def contarGananciaLimite():
    temp = [0]
    for i in range(len(peso)):
        costoActual = peso[i]
        rankingActual = valor[i]
        for x in range(cantidadMaxima[i]):
            for j in range(Presupuesto, costoActual-1, -1):
                cantObjetos[j] = max(cantObjetos[j], cantObjetos[j-costoActual]+rankingActual)                
                if j == 50 and temp[len(temp)-1] != cantObjetos[j]:
                    temp.append(cantObjetos[j])
                    guardados.append(temp[len(temp)-1] - temp[len(temp)-2])
                    

''' 5 5 2 2 2 2 '''

class main():
    global Presupuesto
    Presupuesto = 50
    for i in range(Presupuesto+1):
        cantObjetos.append(0)
    contarGanancia()
    cont = 0
    for i in cantObjetos:
        print("[{}: {}]".format(cont, i), end = " ")
        cont += 1
    print(cantObjetos[Presupuesto])

    for i in guardados:
        print("[{}]".format(i), end = " ")
    
        
