quantia = 0

for n in range(5):
    valor = int(input())
    
    if valor % 2 == 0:
        quantia += 1
        
print(f'{quantia} valores pares')