cantObjetos = []
Presupuesto = 0

"""limite de stock del producto"""
cantidadMaxima = [2, 4, 10, 9, 20]

peso = [1, 2, 5, 7, 8]
"""ranking del producto donde el mas comprado es el menor y el mayor es el menos comprado"""
valor = [2, 5, 6, 10, 13]
guardados = [0]


def contarGanancia():
    for i in range(len(peso)):
        pesoActual = peso[i]
        gananciaActual = valor[i]
        for j in range(Presupuesto, pesoActual - 1, -1):
            cantObjetos[j] = max(cantObjetos[j], cantObjetos[j - pesoActual] + gananciaActual)


def contarGananciaLimite():
    temp = [0]
    for i in range(len(peso)):
        costoActual = peso[i]
        rankingActual = valor[i]
        for x in range(cantidadMaxima[i]):
            for j in range(Presupuesto, costoActual - 1, -1):
                cantObjetos[j] = max(cantObjetos[j], cantObjetos[j - costoActual] + rankingActual)
                if j == 50 and temp[len(temp) - 1] != cantObjetos[j]:
                    temp.append(cantObjetos[j])
                    guardados.append(temp[len(temp) - 1] - temp[len(temp) - 2])


''' 5 5 2 2 2 2 '''

def contar_ganancia_con_limites():
    ganancia = []
    objetos = []
    for i in range(len(peso)+1):
        nueva_lista = []
        nueva_lista_objetos = []
        ganancia.append(nueva_lista)
        objetos.append(nueva_lista_objetos)
        for j in range(Presupuesto+1):
            lista_objetos = []
            ganancia[i].append(0)
            objetos[i].append(lista_objetos)
            for k in range(len(peso)):
                objetos[i][j].append(0)

    for i in range(len(peso)):
        pesoActual = peso[i]
        gananciaActual = valor[i]
        for j in range(pesoActual):
            ganancia[i+1][j] = ganancia[i][j]
            for k in range(len(peso)):
                objetos[i + 1][j][k] = objetos[i][j][k]
        for j in range(pesoActual, Presupuesto+1):
            nueva_ganancia = gananciaActual + ganancia[i+1][j-pesoActual]
            for k in range(len(peso)):
                objetos[i + 1][j][k] = objetos[i + 1][j - pesoActual][k]
            if nueva_ganancia > ganancia[i][j]:
                ganancia[i+1][j] = gananciaActual + ganancia[i+1][j-pesoActual]
                objetos[i+1][j][i] += 1
            else:
                ganancia[i + 1][j] = ganancia[i][j]
                for k in range(len(peso)):
                    objetos[i + 1][j][k] = objetos[i][j][k]
    for i in range(len(peso)):
        print(f"{i}: {objetos[len(objetos)-1][len(objetos[0])-1][i]}")
class main():
    global Presupuesto
    Presupuesto = 10
    # for i in range(Presupuesto + 1):
    #     cantObjetos.append(0)
    # contarGananciaLimite()
    # cont = 0
    # for i in cantObjetos:
    #     print("[{}: {}]".format(cont, i), end=" ")
    #     cont += 1
    # print(cantObjetos[Presupuesto])
    #
    # for i in guardados:
    #     print("[{}]".format(i), end=" ")
    contar_ganancia_con_limites()