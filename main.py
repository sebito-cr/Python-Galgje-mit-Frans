print("Welkom bij galgje")
import random
WoordLijst = ['informatica','informatiekunde','spelletje','aardigheidje','scholier','fotografie','waardebepaling','specialiteit','verzekering','universiteit','heesterperk']
GeheimWoord = WoordLijst[random.randrange(0, len(WoordLijst))]
GeradenLetters = []
levens = 5