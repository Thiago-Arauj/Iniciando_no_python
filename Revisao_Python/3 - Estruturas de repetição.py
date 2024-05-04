# while = enquanto

# a = int(input())
# b = 100

# while a < b:
#     print(a)
#     a += 30
# else:
#     print('Acabou')

# Exercicio da sala
# ==================================================================
texto = ';lkfbsdfisdfiolsadgfilahfawsegbawifçbpvwsei~fbvcpaesw'
saida = ''

for letra in texto:
    if letra not in saida:
        saida += letra

print(saida)
# ==================================================================

for letra in texto: # imprime valores
    print(letra)
 
for numero in range(len(texto)): # imprime indices
    print(numero)