import numpy as np
"""Una lista que guarda las ganancias maximas para cada presupuesto hasta el presupuiesto dado"""
cantObjetos = []
"""una lista donde se guardan diccionarios para poder tener las cantidades usadas para cada producto"""
cantDiferentesPesos = []
"""limite de stock del producto"""
cantidadMaxima = []
"""El producto asociado a su peso"""
productos = {}
"""El costo de produccion para cada producto"""
costProd =  []
"""ganancia por producto, se quiere tener la mayor ganancia sin pasar el presupuesto"""
ganancias = []

def contarGananciaLimite(PresupuestoActual):
    for i in range(len(costProd)):
        pesoActual = costProd[i]
        valorActual = ganancias[i]
        for x in range(cantidadMaxima[i]):
            for j in range(PresupuestoActual, pesoActual-1, -1):
                if cantObjetos[j-pesoActual]+ valorActual > cantObjetos[j]:
                    for k in range(len(cantDiferentesPesos[j])):
                        cantDiferentesPesos[j][costProd[k]] = cantDiferentesPesos[j-pesoActual][costProd[k]]
                    cantDiferentesPesos[j][pesoActual] = cantDiferentesPesos[j][pesoActual]+1                    
                    cantObjetos[j] = cantObjetos[j-pesoActual]+ valorActual
                
def ChoiceExample(NroEjemplo):
    global cantidadMaxima
    global productos
    global costProd
    global ganancias
    global cantObjetos
    global cantDiferentesPesos
    cantDiferentesPesos.clear()
    cantObjetos.clear()
    cantidadMaxima.clear()
    productos.clear()
    costProd.clear()
    ganancias.clear()
    if(NroEjemplo == 1):
        cantidadMaxima = [7, 3, 2, 5, 6, 10]
        productos = {1:"Suzuki Swift", 2:"Santana", 4:"Nissan Patrol 2011", 5:"Lamborghini", 7:"BMW", 8:"Tesla Cybertruck"}
        costProd =  [1, 2, 4, 5, 7, 8]
        ganancias = [2, 5, 6, 10, 13, 16]
        Presupuesto = 100
        Mochila(Presupuesto)
    
    elif(NroEjemplo == 0):
        cant = input("Introduce el numero de productos que tiene: ")        
        while not cant.isdigit() or not (int(cant) > 0):
            cant = input(f"La entrada '{cant}' no es valida, intenta otra vez: ")
        cant = int(cant)

        for i in range(cant):
            temp = input(f"Introduce el nombre del producto {i+1}: ")
            temp2 = input(f"Introduce la cantidad maxima de '{temp}': ")
            while not temp2.isdigit() or not (int(temp2) > 0):
                temp2 = input(f"La entrada '{temp2}' no es valida, intenta otra vez: ")
            temp2 = int(temp2)
            cantidadMaxima.append(temp2)

            temp3 = input(f"Introduce el coste de produccion de '{temp}': ")
            while not temp3.isdigit() or not (int(temp3) > 0):
                temp3 = input(f"La entrada '{temp3}' no es valida, intenta otra vez: ")
            temp3 = int(temp3)
            costProd.append(temp3)

            temp4 = input(f"Introduce la ganancia generada del producto '{temp}': ")
            while not temp4.isdigit() or not (int(temp4) > 0):
                temp4 = input(f"La entrada '{temp4}' no es valida, intenta otra vez: ")
            temp4 = int(temp4)
            ganancias.append(temp4)
            productos[temp3] = temp
        
        Presupuesto = input("Introduce el presupuesto que tiene: ")
        while not Presupuesto.isdigit() or not (int(Presupuesto) > 0):
                Presupuesto = input(f"La entrada '{Presupuesto}' no es valida, intenta otra vez: ")
        Presupuesto = int(Presupuesto)
        print()
        Mochila(Presupuesto)
            

    



def Mochila(Presupuesto):
    for i in range(Presupuesto+1):
        cantObjetos.append(0)
        cantidades = {}
        for j in costProd:
            cantidades[j] = 0
        cantDiferentesPesos.append(cantidades)

    contarGananciaLimite(Presupuesto)    
    print(f"Para presupuesto de {Presupuesto} se tiene:")
    print("Ganancia Maxima", cantObjetos[Presupuesto])

    for i in cantDiferentesPesos[Presupuesto]:
        if cantDiferentesPesos[Presupuesto][i] != 0:
            print(f"Producir {cantDiferentesPesos[Presupuesto][i]} de {productos[i]} con coste de {cantDiferentesPesos[Presupuesto][i]*i}")
    print("============================================================================================================================================================================") 
    Choice2 = ""
    while(Choice2 != "MENU"):
        Choice2 = input("Escriba 'MENU' para volver al menu: " )
    print()

    
def Menu():
    print("============================================================================================================================================================================")
    print("Escribe 'E1' para ir al ejemplo 1.")
    print("Escribe 'E2' para ir al ejemplo 2.")
    print("Escribe 'E3' para ir al ejemplo 3.")
    print("Escribe 'E4' para ir al ejemplo 4.")
    print("Escribe 'E5' para ir al ejemplo 5.")
    print("Escribe 'E6' para ir al ejemplo 6.")
    print("Escribe 'E' para generar un ejemplo nuevo.")
    print("Escribe 'EXIT' para salir del programa.")
    print("============================================================================================================================================================================")

class main():
    Menu()
    Choice = input()
    while(Choice != "EXIT"):
        if(Choice == "E1"):
            ChoiceExample(1)
        elif(Choice == "E2"):
            ChoiceExample(2)
        elif(Choice == "E3"):
            ChoiceExample(3)
        elif(Choice == "E4"):
            ChoiceExample(4)
        elif(Choice == "E5"):
            ChoiceExample(5)
        elif(Choice == "E6"):
            ChoiceExample(6)
        elif(Choice == "E"):
            ChoiceExample(0)
        else:
            print(f"Comando no valido {Choice}")
        Menu()
        Choice = input()