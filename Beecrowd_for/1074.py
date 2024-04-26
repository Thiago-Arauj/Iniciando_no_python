n = int(input())

for x in range(n):
    num = int(input())

    if num == 0:
        print('NULL')
    else:
        if num % 2 == 0:
            print('EVEN', end=' ')
        else:
            print('ODD', end=' ')
        
        if num > 0:
            print('POSITIVE')
        else:
            print('NEGATIVE')