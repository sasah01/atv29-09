
l = []
p1 = 'S'
while p1 in 'Ss':
    num = int(input('Digite um numero : '))
    p1 = input('Quer continuar ? [S/N]').strip().upper()
    l.append(num)
    if p1 == 'N':
        break
print(f'Você digitou {len(l)} numeros \n O maior valor foi {max(l)}')