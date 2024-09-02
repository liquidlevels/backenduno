algo = [[-3,-3,2,-3,3,-2,-2,1,2,0,2,0,1],
        [2 , 3,'I',-1,-1,3,2,0,-3,-3,2,2,1],
        [1 ,-3,-3,2,3,1,3,3,2,1,-2,-2,3],
        [0 ,0 ,3,0,3,-3,-2,-3,0,2,2,1,1],
        [2 ,-1,-1,-3,3,3,0,-3,1,-2,2,0,1],
        [0 ,3,-1,1,-1,-2,2,-2,2,-1,-2,-3,0],
        [0 ,3,2,0,1,1,2,3,-1,-3,0,0,-2],
        [3 ,3,-3,-2,3,-3,-1,-3,3,-2,2,-2,-1],
        [-2,-2,1,0,-1,0,3,0,0,-2,2,-3,-1],
        [-3,3,0,-1,-3,1,2,-3,2,-3,0,2,-2],
        [-3,-3,-3,3,-2,0,-2,-3,1,0,1,-1,-2],
        [-1,0,1,2,1,0,'F',0,-3,3,3,-2,-1],
        [1 ,-3,1,0,1,2,3,1,-2,3,3,0,3]]

#alto y ancho de la matriz
matrizVertical = 0
matrizHorizontal = 0
#almacena arrays (1-4) con la informacion de los posibles caminos [valor, vertical, horizontal]
caminos = []

def camino_mas_barato(posicionesValidas, posicionFinal):
    print(posicionesValidas)
    for y in range(len(posicionesValidas) -1):
        print('entre al for')
        if isinstance(posicionesValidas[y][0], str) and posicionesValidas[y][0] == algo[posicionFinal[0]][posicionFinal[1]]:
            print(f'llegamos al final {posicionesValidas[y][0]} = {posicionFinal}')
            return
        elif isinstance(posicionesValidas[y][0], str):
            print(f'adios, {posicionesValidas[y][0]}')
            print(f'posicionesValidas[y]?? {posicionesValidas[y]}')
            posicionesValidas.remove(posicionesValidas[y])
            print(f'posiciones validas despues: {posicionesValidas}')
        else:
            print('ninguna de las anteriores')
    
    print(f'posiciones validas antes del segundo for: {posicionesValidas}')
    for x in range(len(posicionesValidas) -1):
        print('entre al segundo for?')
        mayor = max(posicionesValidas)
        posicionesValidas.remove(mayor)
        print(f'segundo for: {posicionesValidas}')

    print(len(posicionesValidas))
    if(len(posicionesValidas) > 1):
        print(f'varios casos, elige el mejor: {posicionesValidas}')
        return posicionesValidas
    
    print('llegue al final?')
    return posicionesValidas[0]

#me da los posibles caminos que puedo tomar basado en el "safe area" 0-12 en xy
def posibles_rutas(vertical, horizontal):
    #izquierda
    if horizontal - 1 >= 0:
        caminos.append([algo[vertical][horizontal - 1], vertical, horizontal - 1])
    #derecha
    if horizontal + 1 <= 12:
        caminos.append([algo[vertical][horizontal + 1], vertical, horizontal + 1])
    #arriba
    if vertical - 1 >= 0:
        caminos.append([algo[vertical - 1][horizontal], vertical - 1, horizontal])
    #abajo
    if vertical + 1 <= 12:
        caminos.append([algo[vertical + 1][horizontal], vertical + 1, horizontal])

    return caminos

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

#camino_mas_barato([[-3, 2, 2], [-3, 2, 1], [2, 2, 3], ['I', 1, 2], [3, 3, 2]],[11,6])

camino_mas_barato([[1,11,4],['F',11,6],[0,10,5],[2,12,5]],[11,6])

#el_camino_asi_es([1,2], [11,6])
