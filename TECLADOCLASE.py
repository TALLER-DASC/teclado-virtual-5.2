rows = 0
cols = 0
teclado = []

# LEER EL ARCHIVO
fil = open('filasc.txt','r')

if fil.mode == 'r':
    # obtener el contenido
    lines = fil.readlines()
    c = 1
    l = 0
    # recorrer los renglones
    for line in lines:

        # encontrar el primer renglón
        if c == 1:
            row_col = line.split(' ')
            print(row_col[0], ' - ', row_col[1])
            rows = int(row_col[0])
            cols = int(row_col[1])

        # encontrar las letras del teclado
        if c > 1 and c <= (rows + 1):
            letters = list(line)
            letters.pop()
            teclado.append(letters)
        if c == (rows + 2 ):
            palabra = list(line)
            enter = list("*")
            palabra = palabra + enter





        c += 1
posx = 0
posy = 0
cantmovi = 0
cantsentido = []

print("Palabra a buscar: \n",palabra)
pos=1
cantidad = []
for letra in range(len(palabra)):
    for fila in range(rows):
        for columna in range(cols):
            if (teclado[fila][columna]) == palabra[letra]:
                if teclado[fila][columna] == palabra[pos]:
                    pos += 1
                else:
                     if posx < fila:
                        cantmovi = fila - posx
                        posx = fila
                        cantidad.append(cantmovi)
                        cantsentido.append(cantmovi)
                        cantsentido.append('Hacia abajo, seleccionar')
                     elif posx > fila:
                         cantmovi = posx - fila
                         posx = fila
                         cantidad.append(cantmovi)
                         cantsentido.append(cantmovi)
                         cantsentido.append('Hacia arriba, seleccionar')
                     if posy < columna:
                        cantmovi = columna - posy
                        posy = columna
                        cantidad.append(cantmovi)
                        cantsentido.append(cantmovi)
                        cantsentido.append('Hacia derecha, seleccionar')
                     elif posy > columna:
                          cantmovi = posy - columna
                          posy = columna
                          cantidad.append(cantmovi)
                          cantsentido.append(cantmovi)
                          cantsentido.append('Hacia izquierda, seleccionar')

cantsentido.pop()
cantsentido.pop()

cantidad2 = 0
cantidad.pop()
for i in range(len(cantidad)):
    cantidad2 = cantidad2 + int(cantidad[i])

cantidad2 = cantidad2 + len(palabra)
print("Cantidad de movimientos: ",cantidad2)