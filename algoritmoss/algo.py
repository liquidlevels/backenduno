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

#la utilizo para tener el valor y la posicion dividida en x & y
def posicion_actual(vertical, horizontal):
    #print(f'valor: {algo[vertical][horizontal]}, vertical: {vertical}, horizontal {horizontal}')
    return [algo[vertical][horizontal], vertical, horizontal]

def mas_barato(posiciones_validas):
    for x in range(len(posiciones_validas) -1):
        mayor = max(posiciones_validas)
        posiciones_validas.remove(mayor)

    return posiciones_validas[0]

#me da los posibles caminos que puedo tomar basado en el "safe area" 0-12 en xy
caminos = []
def caminos_viables(vertical, horizontal):
    #izquierda
    if posicion_actual(vertical, horizontal - 1)[2] < 0:
        print('mevalevergacompa')
        pass
    else:
        caminos.append([algo[vertical][horizontal - 1], vertical, horizontal - 1])
    #derecha
    if posicion_actual(vertical, horizontal + 1)[2] > 12:
        print('mevalevergacompa')
        pass
    else:
        caminos.append([algo[vertical][horizontal], vertical, horizontal + 1])
    #arriba
    if posicion_actual(vertical - 1, horizontal)[1] < 0:
        print('mevalevergacompa')
        pass
    else:
        caminos.append([algo[vertical - 1][horizontal], vertical - 1, horizontal])
    #abajo
    if posicion_actual(vertical + 1, horizontal)[1] > 12:
        print('mevalevergacompa')
        pass
    else:
        caminos.append([algo[vertical + 1][horizontal], vertical + 1, horizontal])

    return caminos

def prueba():
    print(f'don baraton: {mas_barato(caminos_viables(2,1))}')
    print(caminos_viables(2,1))

prueba()
