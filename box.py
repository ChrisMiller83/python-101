print('We will print a box.')
rows = int(input("How wide should the box be?  "))
columns = int(input("How tall should the box be?  "))

for w in range(1, rows + 1):
    for h in range(1, columns +1):
        if(w == 1 or w == rows or h == 1 or h == columns):
            print('x', end = ' ')
        else:
            print(' ', end = ' ')
    print()            