import re

def validate_numero_telefone(phone_number):

    # \ serve para dizer que quero especificamente aquele simbolo
    pattern = '\(\d{2}\)\s9\d{4}-\d{4}'
    match = re.fullmatch(pattern, phone_number)

    if match:  
      return 'Número de telefone válido.'
    else:
      return 'Número de telefone inválido.'

phone_number = input()
result = validate_numero_telefone(phone_number)

print(result)
