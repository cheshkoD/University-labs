
w = int(input('Enter w : '))
h = int(input('Enter h : '))

for i in range(h):
    if i == 0 or i == h - 1:
        for j in range(w):
            print('*', end=' ')
    else:
        print('*', end=' ')
        for j in range(1, w - 1):
            print(' ', end=' ')
        print('*', end=' ')
    print('')

