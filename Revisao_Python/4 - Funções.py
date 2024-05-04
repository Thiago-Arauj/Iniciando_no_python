
# Na prova só é necessário enviar isso
def unico(string):
    saida = ''
    for letra in string:
        if letra not in saida:
            saida += letra
    
    return saida

print(unico(string='sdafo~ugsdbdfuo~dfaduoxbjfvzsdgusdgfdhgs')) # Pra testar é assim