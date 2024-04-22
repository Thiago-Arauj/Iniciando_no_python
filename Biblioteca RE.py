import re

def validate_numero_telefone(phone_number):

    # pattern = re.compile(r'([0-9]{2}) 9[0-9]{4}-[0-9]{4}')
    match = re.fullmatch('\d{2}\s9\d{4}-\d{4}', phone_number)

    if match:  
      return 'Número de telefone válido.'
    else:
      return 'Número de telefone inválido.'

phone_number = input()
result = validate_numero_telefone(phone_number)

print(result)

# lista = [1, 2, 3, 'a', 'b', 'c']

# for i, v in enumerate(lista):
#     print(f'Indice={i} Valor={v}')