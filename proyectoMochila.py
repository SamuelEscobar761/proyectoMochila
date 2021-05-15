"""Una lista que guarda las ganancias maximas para cada presupuesto hasta el presupuiesto dado"""
miniMochilas = []
"""una lista donde se guardan diccionarios para poder tener las cantidades usadas para cada producto"""
cantDiferentesPesos = []
"""limite de stock del producto"""
cantidadMaxima = []
"""El producto asociado a su peso"""
productos = {}
"""El costo de produccion para cada producto"""
costProd =  []
"""ganancia por producto, se quiere tener la mayor ganancia sin pasar el presupuesto"""
gananciasNetas = []

def contarGananciaLimite(PresupuestoActual):
    for i in range(len(costProd)):
        pesoActual = costProd[i]
        valorActual = gananciasNetas[i]
        for x in range(cantidadMaxima[i]):
            for j in range(PresupuestoActual, pesoActual-1, -1):
                if miniMochilas[j-pesoActual] + valorActual > miniMochilas[j]:
                    for k in range(len(cantDiferentesPesos[j])):
                        cantDiferentesPesos[j][costProd[k]] = cantDiferentesPesos[j-pesoActual][costProd[k]]
                    cantDiferentesPesos[j][pesoActual] = cantDiferentesPesos[j][pesoActual]+1
                    miniMochilas[j] = miniMochilas[j-pesoActual] + valorActual

def ChoiceExample(NroEjemplo):
    global cantidadMaxima
    global productos
    global costProd
    global gananciasNetas
    global miniMochilas
    global cantDiferentesPesos
    cantDiferentesPesos.clear()
    miniMochilas.clear()
    cantidadMaxima.clear()
    productos.clear()
    costProd.clear()
    gananciasNetas.clear()
    if(NroEjemplo == 1):
        print("Ejecutando ejemplo de autos...")
        cantidadMaxima = [2, 3, 2, 4, 3, 2]
        productos = {6592: "Suzuki Swift", 1360: "Suzuki Santana", 16000: "Nissan Patrol 2011", 200000: "Lamborghini URUS", 39580: "BMW X7", 15960: "Tesla Cybertruck RWD"}
        costProd = [6592, 1360, 16000, 200000, 39580, 15960]
        gananciasNetas = [9888, 2040, 24000, 300000, 59370, 23940]
        Presupuesto = 300000
        Mochila(Presupuesto)

    elif(NroEjemplo==2):
        print("Ejecutando ejemplo de zapatos...")
        cantidadMaxima = [7, 8, 5, 6, 8, 3]
        productos = {94: "Adidas Nemeziz 19", 85: "Adidas Mutator", 93: "Adidas The Predator",
                     84: "Nike Mercurial Superfly 8 Elite FG", 72: "Nike Mercurial Vapor 14 Elite FG",
                     81: "Nike Phantom GT Elite Dynamic Fit 3D FG"}
        costProd = [94, 85, 93, 84, 72, 81]
        gananciasNetas = [40, 36, 40, 36, 31, 35]
        Presupuesto = 1000
        Mochila(Presupuesto)

    elif (NroEjemplo == 3):
        print("Ejecutando ejemplo de mouses...")
        cantidadMaxima = [8, 10, 15, 5, 5, 20]
        productos = {40: "Logitech G 910", 14: "Razer Gaming Viper", 6: "Pictek Mouse",
                     21: "Razer Basilisk X", 70: "Logitech G PRO X Superlight Inalambrico",
                     4: "VEGCOO C10"}
        costProd = [40, 14, 6, 21, 70, 4]
        gananciasNetas = [55, 16, 8, 24, 85, 6]
        Presupuesto = 500
        Mochila(Presupuesto)

    elif (NroEjemplo == 4):
        print("Ejecutando ejemplo de procesadores...")
        cantidadMaxima = [10, 18, 32, 24, 38, 22]
        productos = {126: "AMD Ryzen 7 5800X", 210: "AMD Ryzen 9 5900X", 66: "Intel Core i5-9600K",
                     96: "Intel Core i7-10700K", 57: "AMD Ryzen 5 2600",
                     114: "Intel Core i9-9900K"}
        costProd = [126, 210, 66, 96, 57, 114]
        gananciasNetas = [294, 490, 154, 224, 133, 266]
        Presupuesto = 2000
        Mochila(Presupuesto)


    elif (NroEjemplo == 5):
        print("Ejecutando ejemplo de panetones...")
        cantidadMaxima = [20, 20, 46, 23, 78, 46, 12]
        productos = {30: "Panetón Gustossi", 40: "Panetón La Francesa ChocoChip", 80: "Panetón D'onfrio Chocotón",
                     120: "Panetón Anapqui Real", 20: "Panetón Todinno",
                     42: "Panetón San Gabriel", 35: "Panetón San Gabriel Deli-Choc"}
        costProd = [30, 40, 80, 120, 20, 42, 35]
        gananciasNetas = [5, 8, 10, 20, 3, 8, 11]
        Presupuesto = 2500
        Mochila(Presupuesto)


    elif (NroEjemplo == 6):
        print("Ejecutando ejemplo de consolas...")
        cantidadMaxima = [10, 16, 30, 32, 20, 25, 14, 20]
        productos = {450: "PlayStation 5", 355: "PlayStation 5 Online Edition", 480: "XBOX Series X",
                     280: "XBOX Series S", 245: "Nintendo Switch",
                     200: "Nintendo Switch Lite", 380: "PlayStation 4 Pro", 400: "XBOX One X"}
        costProd = [450, 355, 480, 280, 245, 200, 380, 400]
        gananciasNetas = [50, 45, 20, 20, 40, 20, 30, 40]
        Presupuesto = 21000
        Mochila(Presupuesto)

    elif(NroEjemplo == 0):
        cant = input("Introduce el numero de productos que tiene: ")
        while not cant.isdigit() or not (int(cant) > 0):
            cant = input(f"La entrada '{cant}' no es valida, intenta otra vez: ")
        cant = int(cant)

        for i in range(cant):
            temp = input(f"Introduce el nombre del producto {i+1}: ")
            temp2 = input(f"Introduce la cantidad maxima de '{temp}' que no sea igual a uno anterior: ")
            while not temp2.isdigit() or not (int(temp2) > 0):
                temp2 = input(f"La entrada '{temp2}' no es valida, intenta otra vez: ")
            temp2 = int(temp2)
            cantidadMaxima.append(temp2)

            temp3 = input(f"Introduce el coste de produccion de '{temp}': ")
            while not temp3.isdigit() or not (int(temp3) > 0):
                temp3 = input(f"La entrada '{temp3}' no es valida, intenta otra vez: ")
            temp3 = int(temp3)
            costProd.append(temp3)

            temp4 = input(f"Introduce la ganancia neta del producto '{temp}': ")
            while not temp4.isdigit() or not (int(temp4) > 0):
                temp4 = input(f"La entrada '{temp4}' no es valida, intenta otra vez: ")
            temp4 = int(temp4)
            gananciasNetas.append(temp4)
            productos[temp3] = temp

        Presupuesto = input("Introduce el presupuesto que tiene: ")
        while not Presupuesto.isdigit() or not (int(Presupuesto) > 0):
                Presupuesto = input(f"La entrada '{Presupuesto}' no es valida, intenta otra vez: ")
        Presupuesto = int(Presupuesto)
        print("Ejecuntando ejemplo propio...")
        Mochila(Presupuesto)
        print("============================================================================================================================================================================")






def Mochila(Presupuesto):
    for i in range(Presupuesto+1):
        miniMochilas.append(0)
        cantidades = {}
        for j in costProd:
            cantidades[j] = 0
        cantDiferentesPesos.append(cantidades)

    contarGananciaLimite(Presupuesto)

    print("Ejecutado con éxito")
    print("============================================================================================================================================================================")
    print(f"Para un presupuesto de {Presupuesto} se tiene:")
    inversion = 0
    for i in cantDiferentesPesos[Presupuesto]:
        inversion += cantDiferentesPesos[Presupuesto][i]*i

    print(f"Con una inversion de {inversion} se consigue un total de {miniMochilas[Presupuesto]+inversion} donde se tiene una ganancia maxima neta de {miniMochilas[Presupuesto]}.")

    for i in cantDiferentesPesos[Presupuesto]:
        if cantDiferentesPesos[Presupuesto][i] != 0:
            print(f"Producir {cantDiferentesPesos[Presupuesto][i]} de '{productos[i]}' con coste de {cantDiferentesPesos[Presupuesto][i]*i}.")
    print("============================================================================================================================================================================")
    Choice2 = ""
    while(Choice2 != "MENU"):
        Choice2 = input("Escriba 'MENU' para volver al menu: " )


def Menu():
    print("============================================================================================================================================================================")
    print("Escribe 'E1' para ir al ejemplo 1.")
    print("Escribe 'E2' para ir al ejemplo 2.")
    print("Escribe 'E3' para ir al ejemplo 3.")
    print("Escribe 'E4' para ir al ejemplo 4.")
    print("Escribe 'E5' para ir al ejemplo 5.")
    print("Escribe 'E6' para ir al ejemplo 6.")
    print("Escribe 'E' para generar un ejemplo nuevo.")
    print("Escribe 'FIN' para salir del programa.")
    print("============================================================================================================================================================================")

class main():
    Menu()
    Choice = input()
    while(Choice != "FIN"):
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