from random import random
import string

letraAleatoria = random.choice(string.ascii_letters)

chances = 0
'''quase jogo da forca'''
while chances <= 5:

     letraJogador = str(input("Digite uma letra: ")) 
     if letraJogador == letraAleatoria :
         print("Você venceu!")
         print("Sua jogada" + str(letraJogador))
         print("Letra correta" + str(letraAleatoria))
     else:
         print("Tente novamente")
         chances =+1
