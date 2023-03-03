
def pguessgame():
    import random

    print("-------------")
    print("--Guessgame--")
    print("-------------")

    random = random.random() * 20
    secret_number = int(random)
    turn = 1
    guesses = 0

    print('Níveis de Dificuldade')
    print("(1)Easy (2)Normal (3)Hard")

    difchange = int(input("Setar dificuldade: "))

    if (difchange == 1):
        guesses = 10
    elif(difchange == 2):
        guesses = 5
    else:
        guesses = 3


    while guesses > 0:
        guess = input('Digite o seu número: ')
        guess = int(guess)
        print('-----------------------------')
        print('Gastou 1 chance(s) de {}.'.format(guesses))
        if guess < 1 or guess > 20:
            print('O número deve estar entre 1 e 20.')
            continue
        check = guess == secret_number
        print('Você digitou:', guess)
        if check:
            print('=============')
            print('Você acertou!')
            print('=============')
            break
        else:
            if guess > secret_number:
                print('Você chutou acima do número.')
                print('-----------------------------')
            else:
                print('Você chutou abaixo do número.')
                print('-----------------------------')
            guesses -= 1

    if guesses == 0:
        print('Suas tentativas acabaram. O número secreto era', secret_number)