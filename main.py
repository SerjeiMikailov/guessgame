print("---------------------------------")
print("Bem vindo ao jogo!")
print("---------------------------------")

import random


random = random.random() * 20
secret_number = int(random)
turn = 1
guesses = 5

for turn in range(1, guesses + 1):
    print('Gastou {} chance(s) de 5.'.format(turn))
    guess = input('Digite o seu número: ')
    guess = int(guess)
    if guess < 1 or guess > 20:
        print('O número deve estar entre 1 e 20.')
        continue
    check = guess == secret_number
    print('Você digitou:', guess)
    if check:
        print('Você acertou!')
        break
    else:
        if guess > secret_number:
            print('Você chutou acima do número.')
        else:
            print('Você chutou abaixo do número.')
        guesses -= 1

if guesses == 0:
    print('Suas tentativas acabaram. O número secreto era', secret_number)
