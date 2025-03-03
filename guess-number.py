from random import randint
n = randint(1, 100)
cont=0
while True:
    cont+=1
    numero = int(input('Adivinhe o número: '))
    if numero < 1 or numero > 100:
        print('O número deve estar entre 1 e 100!')
        continue
    if numero == n:
        print(f'Parabéns, você acertou em {cont} tentativas!')
        break
    elif numero < n:
        print('Muito Baixo!')
    else:
        print('Muito Alto!')