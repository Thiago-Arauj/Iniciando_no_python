# 1097
#================================================
# Começamos definindo as variaveis
# Dizendo qual será o primeiro valor de i e de j
# e o primeiro valor do limite inferior
#================================================
i = 1
j = 7
inferior = 5

while i <= 9:
    while j >= inferior:
        # neste loop fazemos uma contagem
        # que vai do valor de j até o
        # limite inferior para atualizarmos
        # os valores de i e de j na frequencia
        # correta
        print(f'I={i} J={j}')
        j -= 1
    i += 2
    # aqui fazemos j voltar ao valor anterior
    j += 3 
    # agora atribiumos esse valor ao  limite
    inferior = j 
    # e depois definimos o novo valor para j
    j += 2

# 1098
# Começamos definindo as variaveis
# Dizendo qual será o primeiro valor de i e de j
i = 0
j = 1

# Aqui sabemos que o valor máximo de i será 2
# e que i será incrementado em 0.2 a cada
# terceira incrementação de j, que será de 1 a 3
# sempre sendo somado com o valor de i
while i <= 2:
    while j <= 3:
        # aqui checamos se i será um inteiro ou
        # um float, sendo inteiro ele imprime
        # os numeros sem casa decimal
        if type(i) == int:
            j = int(j)
            print(f'I={i} J={j + i}')
        else:
            print(f'I={i:.1f} J={(j + i):.1f}')
        j += 1
    # aqui resetamos o valor de j e começamos a
    # incrementar o valor de i
    i += 0.2
    j = 1
# para descobrir quando i é um inteiro ou não
# primeiro transformamos ele em uma string 
# arredondada para uma casa decimal e logo em
# seguida verficamos se o numero depois da virgula
# é 0 ou não, se for 0 (exemplo 2.0) então podemos
# transformar ele em inteiro (exemplo 2.0 vira 2)
    i = str(f'{i:.1f}')
    if i[-1] == '0':
        i = int(i[0])
    else:
        i = float(i)

#1099
#================================================
# Aqui começamos definindo primeiramente o numero
# de repetições que serão feitas, representado
# por n, e iniciamos o contador e a soma
#================================================
n = int(input())
contador = 0
soma = 0

while contador < n:
# aqui resetamos o valor da soma
    soma = 0
# aqui recebemos x e y numa mesma linha e os 
# separamos em duas variaveis distintas que
# serão os limites do nosso intervalo
    x, y = input().split()
    x = int(x)
    y = int(y)
    
# aqui vemos qual é o maior entre x e y e se
# ambos forem iguais ele dirá que não tem nenhum
# impar no intervalo e irá imprimir 0
    if x > y:
        corredor = y + 1
        while y < corredor < x:
            if corredor % 2 != 0:
                soma += corredor
            corredor += 1
        print(soma)
    elif y > x:
        corredor = x + 1
        while x < corredor < y:
            if corredor % 2 != 0:
                soma += corredor
            corredor += 1
        print(soma)
    else:
        print(0)
    contador += 1

#1101 // Tá mais ou menos, precisa consertar
while True:
    m, n = input().split()
    m = int(m)
    n = int(n)
    soma = 0
    
    if m or n <= 0:
        break
    
    if m > n:
            corredor = n
            while corredor <= m:
                print(corredor, end='')
                soma += corredor
            else:
                print(soma)
    elif n > m:
        corredor = m
        while corredor <= n:
            print(corredor, end='')
            soma += corredor
        else:
            print(soma)

#1115
#================================================
# Aqui fazemos um loop infinito que vai checar
# em qual quadrante as coordenadas se encaixam
# e ele irá se repetir até que ou x ou y seja 0
#================================================
while True:
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    elif x > 0 and y < 0:
        print("quarto")
    else:
        break

#1117
#================================================
# Aqui vamos receber notas até que tenham 2 notas
# válidas e sempre que encontrarmos uma inválida
# vamos imprimir uma mensagem especifica e não
# iremos atualizar o contador, ele só deve ser
# atualizado quando encontrar nota válida
#================================================ 
soma = 0
contador = 0
while contador < 2:
    nota = float(input())

    if 0 <= nota <= 10:
        soma += nota
        contador += 1
    else:
        print('nota invalida')
else:
    media = soma / contador
    print(f'media = {media:.2f}')