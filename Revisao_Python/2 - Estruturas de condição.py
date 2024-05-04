a = int(input())
b = 10

if a > b:
    if a > 100:
        print('Passou e muito')
elif b > a:
    print('B é maior')
else:
    print('São iguais')

# Como checar se é impar ou par?

if a % 2 == 0: # Checa se é par
    print('É par')
    
if a % 2 != 0: # Checa se é impar
    print('É impar')