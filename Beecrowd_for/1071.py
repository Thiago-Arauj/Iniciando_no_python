x = int(input())
y = int(input())
soma = 0

if x > y:
    aux = x
    x = y
    y = aux

for n in range(x + 1, y):
    if n % 2 != 0:
        soma += n

print(soma)