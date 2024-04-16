# 1097
# i = 1
# j = 7
# inferior = 5

# while i <= 9:
#     while j >= inferior:
#         print(f'I={i} J={j}')
#         j -= 1
#     i += 2
#     j += 3
#     inferior = j
#     j += 2

# 1098
# i = 0
# j = 1

# while i <= 2:
#     while j <= 3:
#         if type(i) == int:
#             j = int(j)
#             print(f'I={i} J={j + i}')
#         else:
#             print(f'I={i:.1f} J={(j + i):.1f}')
#         j += 1
#     i += 0.2
#     i = str(f'{i:.1f}')
#     j = 1
#     if i[-1] == '0':
#         i = int(i[0])
#     else:
#         i = float(i)

#1099
n = int(input())
contador = 0
soma = 0

while contador < n:
    x, y = input().split()
    x = int(x)
    y = int(y)
    
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


