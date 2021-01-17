print('We will print a triangle.')
rows = int(input("How many rows should the triangle be?  "))
x = (2 * rows) - 2
for i in range(0, rows):
    for j in range(0, x):
        print(end = ' ')
    x = x - 1
    for j in range(0, i + 1):
        print("* ", end = ' ')    
    print(" ")           