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

a = 0
b = 0
precio = 0
'''
def camino(inicio, fin):
    c = inicio
    d = fin
    print(inicio,fin)

camino(algo[1][2],algo[11][6])
'''
for x in algo:
    print(x)

micamino = []

a = 1
b = 2
print(f'inicio: {algo[a][b]}, izquierda: {algo[a][b-1]}, derecha: {algo[a][b+1]}, arriba: {algo[a-1][b]}, abajo: {algo[a+1][b]}')

'''
while True:
    for x in algo:
        if isinstance(algo[a][b],str):
            print(f'string: {algo[a][b]} en index: {a},{b}')
            pass
        
        if isinstance(algo[a][b], int):
            if algo[a][b] >= 0:
                precio += algo[a][b]
            else:
                precio -= (-algo[a][b])

            micamino.append(f'[{a},{b}]')
        
        if b == 12:
            b = 0
            a+=1
            continue
        
        b+=1

    if a == 13:
        break
'''
print("caminito: ", micamino)
