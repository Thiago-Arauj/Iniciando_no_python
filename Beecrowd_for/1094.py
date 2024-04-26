n = int(input())
Total_C = 0
Total_R = 0
Total_S = 0

for caso in range(n):
    quantia, tipo = input().split()
    quantia = int(quantia)

    if tipo == 'C':
        Total_C += quantia
    
    elif tipo == 'R':
        Total_R += quantia
    
    elif tipo == 'S':
        Total_S += quantia

Total = Total_S + Total_C + Total_R

print(f'Total: {Total} cobaias')
print(f'Total de coelhos: {Total_C}')
print(f'Total de ratos: {Total_R}')
print(f'Total de sapos: {Total_S}')
print(f'Percentual de coelhos: {((Total_C/Total)*100):.2f} %')
print(f'Percentual de ratos: {((Total_R/Total)*100):.2f} %')
print(f'Percentual de sapos: {((Total_S/Total)*100):.2f} %')
