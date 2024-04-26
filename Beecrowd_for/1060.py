quantia = 0

for n in range(6):
    valor = float(input())
    
    if valor > 0:
        quantia += 1
        
print(f'{quantia} valores positivos')