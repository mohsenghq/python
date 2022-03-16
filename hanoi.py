def hanoi(n, P1, P2, P3):
    """ Move n discs from pole P1 to pole P3. """
    global m
    global count

    if n == 0:
        return
    hanoi(n - 1, P1, P3, P2)
    m = m - 1
    if m <= -1:
        return
    if P1:
        P3.append(P1.pop())
        count += 1
        print('Step ', count)
        show_pole(A, B, C)

    hanoi(n - 1, P2, P1, P3)


def show_pole(A, B, C):
    print(' ' * 8, '||', ' ' * 22, '||', ' ' * 21, '||')

    for i in range(z, -1, -1):
        if len(A) > i:
            disk1 = '=' * (A[i] * 2)
            spaces1 = ' ' * (10 - A[i])
            print(spaces1, disk1, spaces1 + '', end = '', sep = '')
        else:
            print(' ' * 8, '||', ' ' * 8, end = '')

        if len(B) > i:
            disk2 = '=' * (B[i] * 2)
            spaces2 = ' ' * (14 - B[i])
            print(spaces2 + '  ', disk2, spaces2, end = '', sep = '')
        else:
            print(' ' * 14, '||', ' ' * 12, end = '')

        if len(C) > i:
            disk3 = '=' * (C[i] * 2)
            spaces3 = ' ' * (11 - C[i])
            print(spaces3, disk3, sep = '')
        else:
            print(' ' * 9, '||')

    print(20 * '-', ' ' * 4, 20 * '-', ' ' * 3, 20 * '-')
    print(' ' * 5, 'Tower #0', ' ' * 16, 'Tower #1', ' ' * 16, 'Tower #2\n\n')


global z

n, m = input('Enter number of discs and steps with space: ').split()
n = int(n)
m = int(m)

count = 0
z = n

A = list(range(n, 0, -1))
B, C = [], []

show_pole(A, B, C)
hanoi(n, A, B, C)
