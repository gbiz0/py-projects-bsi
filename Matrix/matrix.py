line = 0
column = 0
mat =[[0]*3, [0]*3, [0]*3]

for line in range(0,3):
    for column in range (0,3):
        mat[line][column] = int (input(f"Inform the number for position [{line},{column}]: "))
   

for line in range(0,3):
    for column in range(0,3):
        print(f'[{mat[line][column]}]', end=' ')
    print('')
