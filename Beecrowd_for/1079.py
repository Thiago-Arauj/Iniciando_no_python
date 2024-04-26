n = int(input())
soma = 0

for x in range(n):
    a, b, c = map(float,input().split())
    a *= 2
    b *= 3
    c *= 5
    peso = 10
    print(f'{((a + b + c) / peso):.1f}')