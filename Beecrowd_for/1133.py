x = int(input())
y = int(input())

if x > y:
    aux = x
    x = y
    y = aux

for n in range(x + 1, y):
    if n % 5 == 2 or n % 5 == 3:
        print(n)