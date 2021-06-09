print("Welkom bij galgje")
import random
WoordLijst = ['informatica','informatiekunde','spelletje','aardigheidje','scholier','fotografie','waardebepaling','specialiteit','verzekering','universiteit','heesterperk']
GeheimWoord = WoordLijst[random.randrange(0, len(WoordLijst))]
GeradenLetters = []
levens = 5

def checkWin():
    for i in range(len(GeheimWoord)):
        if not GeheimWoord[i] in GeradenLetters:
            return(False)
    return(True)

def renderWoord():
        for a in range(len(GeheimWoord)):
            if GeheimWoord[a] in GeradenLetters:
                print(GeheimWoord[a], '', end='')
            else:
                print('? ', end='')
        print('')
        print('-' * len(GeheimWoord))

renderWoord()

while True:
    letter = input('raad een letter of typ het woord  ')
    if len(letter) == 1:
        if letter in GeradenLetters:
            print('Die letter had je al geraden...')
            renderWoord()