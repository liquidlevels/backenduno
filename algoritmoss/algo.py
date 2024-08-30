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
        pass
    else:
        caminos.append([algo[vertical][horizontal - 1], vertical, horizontal - 1])
    #derecha
    if posicion_actual(vertical, horizontal + 1)[2] > 12:
        pass
    else:
        caminos.append([algo[vertical][horizontal], vertical, horizontal + 1])
    #arriba
    if posicion_actual(vertical - 1, horizontal)[1] < 0:
        pass
    else:
        caminos.append([algo[vertical - 1][horizontal], vertical - 1, horizontal])
    #abajo
    if posicion_actual(vertical + 1, horizontal)[1] > 12:
        pass
    else:
        caminos.append([algo[vertical + 1][horizontal], vertical + 1, horizontal])

    return caminos

#pruebas
print(f'caminos: {caminos_viables(0,0)}')
posi = posicion_actual(0,0)
print(posi[0])
print(posicion_actual(0,0)[0])
a = 1
b = 2
print(f'inicio: {algo[a][b]}, izquierda: {algo[a][b-1]}, derecha: {algo[a][b+1]}, arriba: {algo[a-1][b]}, abajo: {algo[a+1][b]}')
'''
micamino = []
a = 0
b = 0
precio = 0
while True:
    for x in algo:
        if isinstance(algo[a][b],str):
            print(f'string: {posicion_actual(a,b)} en index: {a},{b}')
            pass
        
        if isinstance(algo[a][b], int):
            if algo[a][b] >= 0:
                precio += algo[a][b]
            else:
                precio -= (-algo[a][b])

        if b == 12:
            b = 0
            a+=1
            continue
        
        b+=1

    if a == 13:
        break
print("caminito: ", micamino)
'''
