cantObjetos = []
cantPesos = []
cantDiferentesPesos = []
Presupuesto = 0

"""limite de stock del producto"""
cantidadMaxima = [7, 3, 2, 5, 6, 10]

modeloAuto = {1: "Suzuki Swift", 2: "Santana", 4: "Nissan Patrol 2011", 5: "Lamborghini", 7: "BMW",
              8: "Tesla Cybertruck"}
costProd = [1, 2, 4, 5, 7, 8]

"""ranking del producto donde el mas comprado es el menor y el mayor es el menos comprado"""
gananciaAnual = {1: 2, 2: 5, 4: 6, 5: 10, 7: 13, 8: 16}


def contarGananciaLimite():
    for i in range(len(cantPesos)):
        if (cantPesos[i] != 0):
            pesoActual = i
            valorActual = gananciaAnual[i]
            for x in range(cantPesos[i]):
                for j in range(Presupuesto, pesoActual - 1, -1):
                    if cantObjetos[j - pesoActual] + valorActual > cantObjetos[j]:

                        for k in range(len(cantDiferentesPesos[j])):
                            cantDiferentesPesos[j][costProd[k]] = cantDiferentesPesos[j - pesoActual][costProd[k]]
                        cantDiferentesPesos[j][pesoActual] = cantDiferentesPesos[j][pesoActual] + 1
                        cantObjetos[j] = cantObjetos[j - pesoActual] + valorActual


class main():
    global Presupuesto
    Presupuesto = 100
    for i in range(Presupuesto + 1):
        cantObjetos.append(0)
        cantPesos.append(0)
        cantidades = {}
        for j in costProd:
            cantidades[j] = 0
        cantDiferentesPesos.append(cantidades)

    for i in range(len(costProd)):
        cantPesos[costProd[i]] = cantidadMaxima[i]

    contarGananciaLimite()

    print(cantDiferentesPesos[Presupuesto])
    cont = 0
    for i in cantObjetos:
        print("[{}: {}]".format(cont, i), end=" ")
        cont += 1
    print()
    print("Ganancia Maxima", cantObjetos[Presupuesto])

    for i in cantDiferentesPesos[Presupuesto]:
        if cantDiferentesPesos[Presupuesto][i] != 0:
            print(f"Producir {cantDiferentesPesos[Presupuesto][i]} de {modeloAuto[i]}")

