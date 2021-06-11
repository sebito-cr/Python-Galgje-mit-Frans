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
        print('- ' * len(GeheimWoord))

renderWoord()

while True:
    letter = input('raad een letter of typ het woord  ')
    if len(letter) == 1:
        if letter in GeradenLetters:
            print('Clowntje die letter had je al geraden...')
            renderWoord()
        else:
            GeradenLetters += letter
            if letter in GeheimWoord:
                print('Lets go. Die letter zit wel in het woord')
                renderWoord()
                if checkWin():
                    print('Lets go je hebt alle letters geraden, en dus gewonnen!')
                    print('Het woord was: ' + GeheimWoord)
                    break
            else:
                print('Oof. Die letter zit niet in het woord')
                print('-1')
                levens -= 1
                renderWoord()
    elif letter == GeheimWoord:
        print('Lets go je hebt het woord geraden, en dus gewonnen!')
        break
    else:
        print('Oof fout woord!')
        print('-2')
        levens -= 2
        renderWoord()
    if levens <= 0:
        print('Bif oof je hebt verloren! Het woord was ' + GeheimWoord)
        break
    print('Je hebt nog', levens, 'levens over.')
