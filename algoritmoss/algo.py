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

c = 0
d = 0

'''
for x in algo:
    print('estas en x numero: ', c)
    c+=1
    for y in algo:
        print('estas en y numero: ', d)
        d+=1
        if b > 12:
            break
        else:
            print('index: ',a,b)
            if algo[a][b] >= 0:
                precio += algo[a][b]
            if algo[a][b] < 0:
                precio -= (-algo[a][b])
            print('presio: ',precio)
            print(algo[a][b])
            if b == 12:
                a+=1
            b+=1
'''

for x in algo:
    print('index: ',a,b)
    if algo[a][b] >= 0:
        precio += algo[a][b]
    if algo[a][b] < 0:
        precio -= (-algo[a][b])
    print('presio: ',precio)
    print(algo[a][b])
    if b == 12:
        a+=1
    b+=1


