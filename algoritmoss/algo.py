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


def posicion_actual(vertical, horizontal):
    #quiero saber si puedo ir a otro lugar
    return algo[vertical][horizontal]

#la utilizo para identificar si el axis vertical es valido
def vertical_valida(vertical):
    return False if vertical < 0 or vertical > 12 else True

#utilizo para saber si el axis horizontal es valido
def horizontal_valida(horizontal):
    return False if horizontal < 0 or horizontal > 12 else True

#una vez tengo los axis validos, es hora de tomar su valor y ponerlo en una lista
posiciones_validas = []
def posicion_valida(vertical, horizontal):
    if vertical_valida(vertical) == True and horizontal_valida(horizontal) == True:
        posiciones_validas.append(algo[vertical][horizontal])
    else:
        print('vertical inaccesible')

    return posiciones_validas

#una vez tengo las posiciones validas dentro de una lista, utilizo este metodo
#para reducirla al valor mas peque;o
def mas_barato(posiciones_validas):
    for x in range(len(posiciones_validas) -1):
        mayor = max(posiciones_validas)
        posiciones_validas.remove(mayor)

    return posiciones_validas[0]

for x in algo:
    print(x)
'''
a = 1
b = 2
print(f'inicio: {posicion_actual(a,b)}, izquierda: {algo[a][b-1]}, derecha: {algo[a][b+1]}, arriba: {algo[a-1][b]}, abajo: {algo[a+1][b]}')
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
