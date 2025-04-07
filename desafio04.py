#jogo da adivinhação

import random

n1 = int(input('Escolha um numero De 1 a 100: '))

n2 = random.randint(1,100)
print(n2)
e = 0
while True:
    if n1 == n2:
        print(f"o computador escolheu {n2} e você {n1} ")
        print('você conseguiu!!')
        break
    elif n1 > n2:
        print("o Numero é menor, tente novamente")
        n1 = int(input('Escolha um numero De 1 a 100: '))
        e + 1
    elif n1 < n2:
        print("o Numero é maior, tente novamente")
        n1 = int(input('Escolha um numero De 1 a 100: '))
        e += 1
print(f"seu numero de erros foi: {e}")