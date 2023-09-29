lista=[]
maior=0
menor=0
for contagem in range(0,5):
    lista.append(float(input(f"digite um valor real para a posiçao {contagem}: ")))
    if contagem == 0:
        maior = menor = lista[contagem]
else:
    if lista[contagem]> maior:
        maior=lista[contagem]
    if lista[contagem]< menor:
        menor= lista[contagem]
print("="*30)
print(f"os valores da lista sao:{lista}")
print(f'o maior valor foi:{max(lista)}')
for i, v in enumerate(lista):
    if min(lista)== v:
        print(f'{i}')
print(f'o menor valor foi:{min(lista)}')







