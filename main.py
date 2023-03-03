import hg
import guess

print("-------------------")
print("---Avaible Games---")
print("-------------------")

print("(1)Forca (2)GuessGame")

game = int(input("Escolha o jogo: "))

if(game == 1):
    print("HG GAME!!")
    hg.playhg()

if(game == 2):
    print("GuessGame!!")
    guess.pguessgame()