algo = [[-3,-3, 2, -3, 3,-2, -2, 1, 2, 0, 2, 0, 1],
        [ 2, 3,'I',-1,-1, 3,  2, 0,-3,-3, 2, 2, 1],
        [ 1,-3,-3,  2, 3, 1,  3, 3, 2, 1,-2,-2, 3],
        [ 0, 0, 3,  0, 3,-3, -2,-3, 0, 2, 2, 1, 1],
        [ 2,-1,-1, -3, 3, 3,  0,-3, 1,-2, 2, 0, 1],
        [ 0, 3,-1,  1,-1,-2,  2,-2, 2,-1,-2,-3, 0],
        [ 0, 3, 2,  0, 1, 1,  2, 3,-1,-3, 0, 0,-2],
        [ 3, 3,-3, -2, 3,-3, -1,-3, 3,-2, 2,-2,-1],
        [-2,-2, 1,  0,-1, 0,  3, 0, 0,-2, 2,-3,-1],
        [-3, 3, 0, -1,-3, 1,  2,-3, 2,-3, 0, 2,-2],
        [-3,-3,-3,  3,-2, 0, -2,-3, 1, 0, 1,-1,-2],
        [-1, 0, 1,  2, 1, 0,'F', 0,-3, 3, 3,-2,-1],
        [ 1,-3, 1,  0, 1, 2,  3, 1,-2, 3, 3, 0, 3]]

#alto y ancho de la matriz
matriz_vertical = 12
matriz_horizontal = 12
#almacena arrays (1-4) con la informacion de los posibles caminos [valor, vertical, horizontal]
opciones_de_caminos = []
ruta_mas_barata = []

'''
dada una lista de posiciones validas y una posicionFinal,
va filtrando para asi tener la opcion mas barata, pero si
algun valor es string y no es el de posicionFinal, lo
elimina de posicionesValidas, si el string == posicionFinal,
hace return
'''
def camino_mas_barato(posicionesValidas, posicionFinal):
    print(f'posiciones validas: {posicionesValidas}')
    for posicion in posicionesValidas:
        print(posicion[0])
        if isinstance(posicion[0], str):
            if posicion[0] == algo[posicionFinal[0]][posicionFinal[1]]:
                print(f'llegamos al final {posicion[0]} = {posicionFinal}')
                return posicion[0]
            else:
                print(f'un string: {posicion[0]}')
                posicionesValidas.remove(posicion)

    for x in range(len(posicionesValidas) -1):
        mayor = max(posicionesValidas)
        posicionesValidas.remove(mayor)
    
    ruta_mas_barata = posicionesValidas[0]
    posicionesValidas.clear()
    return ruta_mas_barata

def todos_los_caminos(opciones):
    print('')

#me da los posibles caminos que puedo tomar basado en el "safe area" 0-12 en xy
def posibles_rutas(vertical, horizontal):
    #izquierda
    if horizontal - 1 >= 0:
        caminos.append([algo[vertical][horizontal - 1], vertical, horizontal - 1])
    #derecha
    if horizontal + 1 <= matriz_horizontal:
        caminos.append([algo[vertical][horizontal + 1], vertical, horizontal + 1])
    #arriba
    if vertical - 1 >= 0:
        caminos.append([algo[vertical - 1][horizontal], vertical - 1, horizontal])
    #abajo
    if vertical + 1 <= matriz_vertical:
        caminos.append([algo[vertical + 1][horizontal], vertical + 1, horizontal])
    print(f'posibles rutas: {caminos}')
    return opciones_de_caminos

def el_camino_asi_es(coordenadaInicial,coordenadaFinal):
    print(f'coordenadaInicial: {coordenadaInicial}')
    print(f'coordenadaFinal: {coordenadaFinal}')

    posicionActual = algo[coordenadaInicial[0]][coordenadaInicial[1]]
    posicionFinal = algo[coordenadaFinal[0]][coordenadaFinal[1]]
    
    caminoBarato = camino_mas_barato(posibles_rutas(coordenadaInicial[0],coordenadaInicial[1]), posicionFinal)
    print(f'el mas barato: {caminoBarato}')

    newVertical = caminoBarato[1]
    newHorizontal = caminoBarato[2]
    print(f'nueva posicion: {newVertical},{newHorizontal}')
   
    if posicionActual == posicionFinal:
        print('si es igual')
        return
    else:
        print('aun no')    
        return el_camino_asi_es([newVertical,newHorizontal], [coordenadaFinal[0], coordenadaFinal[1]])

#el_camino_asi_es([1,2], [11,6])
camino_mas_barato([[1,11,4],['F',11,6],[0,10,5],[2,12,5]],[11,6])
