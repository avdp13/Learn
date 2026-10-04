import ast
import random
import time

def minuten(tijd):
    if (tijd > 60.0):
        m = int(tijd // 60)
        s = round(tijd % 60)
    else:
        m = 0
        s = tijd

    if len(str(round(s))) == 1:
        return f"{m}:0{round(s)}"
    else:
        return f"{m}:{round(s)}"

def bestandsnaam(hvlf):
    while True:
        bestand1 = "dicts/" + input(f'    Wat is de naam van het {hvlf+1}e bestand? (Zonder .txt) ') + '.txt'
        try:
            open(bestand1, 'r', encoding='utf-8').close()
            return bestand1
        except FileNotFoundError:
            print('    Het bestand bestaat niet. Probeer het opnieuw.')

def tojuis(fouten, juisten, foutenlijst, woord):
    print()
    while True:
        greken = input('Wil je het toch goedrekenen? (Doe dit alleen bij typfout/meerdere goede antwoorden.) Y[es]/ N[o] ').lower().strip()
        if greken == 'n':
            fouten += 1
            foutenlijst.append(woord)
            print('Het is fout gerekend.\n')
            return fouten, juisten, foutenlijst
                
        elif greken == 'y':
            print('Het is juist gerekend.\n')
            juisten += 1
            return fouten, juisten, foutenlijst
        
        else:
            print('Voer Y of N in.')
        

talen = {'Du': 'Duits', 'En': 'Engels', 'Fa': 'Frans', 'La': 'Nederlands', 'Gr': 'Nederlands'}
opvragen = {}

hoeveelhtxts = int(input('Hoeveel lijsten wil je invoegen? (Het moet allemaal dezelfde taal zijn.) '))
for w in range(hoeveelhtxts):
    bestand2 = bestandsnaam(w)
    with open(bestand2, 'r', encoding='utf-8') as bestand3:
        inhoud = bestand3.read()
        opvragen1 = ast.literal_eval(inhoud)
        opvragen = opvragen | opvragen1

print(f'\nHoeveelheid woorden die opgevraagd gaan worden: {len(opvragen)}')

with open(bestand2, 'r', encoding='utf-8') as bestand:
    inhoud = bestand.read()
    bestand4 = bestand2[:-4]
    l2ob = bestand4[-2:]
    
    if l2ob in ["La", 'Gr']:
        taleno = {'La': 'Nederlands', 'Gr': 'Nederlands'}
        
    else:
        naarovanuit = input(f"Wil je het naar het {talen[l2ob]} of vanuit het {talen[l2ob]}? (Typ N(aar) of V(anuit)) ").lower()
        if naarovanuit == "n":
            taleno = {'Du': 'Duits', 'En': 'Engels', 'Fa': 'Frans'}
            opvragen1 = opvragen
            opvragen = {v: k for k, v in opvragen1.items()}
            
        elif naarovanuit == "v":
            taleno = {'Du': 'Nederlands', 'En': 'Nederlands', 'Fa': 'Nederlands'}

start = time.time()
woorden = list(opvragen.keys())
random.shuffle(woorden)
fouten = 0
juisten = 0
foutenlijst = []

for woord in woorden:
    print()
    a = input(f"Wat is {woord} in het {taleno[l2ob]}? ").lower()
    if a == opvragen[woord]:
        print("Juist!")
        juisten += 1
        
    else:
        print(f'Fout. Het was {opvragen[woord]}')
        if a in ['', '?']:
            fouten += 1
            foutenlijst.append(woord)
        else:
            fouten, juisten, foutenlijst = tojuis(fouten, juisten, foutenlijst, woord)
        
end = time.time()
tijd = minuten(round(end - start, 0))

print()
print(f"""Hoeveelheid fouten: {fouten}
Hoeveelheid juist: {juisten}
Hoeveelheid vragen: {len(opvragen)}
Hoeveelheid tijd: {tijd}
Cijfer: {round(juisten/(juisten+fouten)*10, 1)}
""")
if not foutenlijst:
    print('Je had alles goed!')
else:
    print("Je had fout:")
    for woordfout in foutenlijst:
        print(f"    {woordfout}: {opvragen[woordfout]}")
