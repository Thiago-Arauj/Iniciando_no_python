# NÃO ITERAVEIS

inteiro = 10
entrada1 = int(input())

flutuante = 10.0
entrada2 = float(input())
entrada2 += 2.25
print(f'{entrada2:.1f}')

booleano = True

a = int(input())
b = 100

# # >, <, >=, <=, ==, !=
# # +, -, *, /, **, %
print(a % b == 60)

# ITERAVEIS

texto = 'Thiago Rodrigues '
texto += 'Mendes' # É o mesmo que: texto = texto + 'Mendes'
print(texto)
print(len(texto))

print(texto) # Ele inclui o começo e para um antes do fim
lista = [10, 10.0, 'Oi', True]
print(lista[3])
print(len(lista))

lista.append('Olá mundo')
print(lista)

lista[0] = 'Não gosto de 10'
print(lista)