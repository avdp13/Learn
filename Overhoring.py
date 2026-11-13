import ast
import random
import time

def minuten(tijd):
    if (tijd >= 60.0):
        m = int(round(tijd)) // 60
        s = round(tijd) % 60
    else:
        m = 0
        s = tijd

    if len(str(round(s))) == 1:
        return f"{m}:0{round(s)}"
    else:
        return f"{m}:{round(s)}"

def bestandsnaam(hvlf):
    while True:
        bestand1 = "Dicts/" + input(f'\033[38;2;0;0;255m    Wat is de naam van het {hvlf+1}e bestand? (Zonder .txt) \033[0m') + '.txt'
        try:
            open(bestand1, 'r', encoding='utf-8').close()
            lang = bestand1[:-4][-2:].lower()
            
            if lang not in talen:
                while True:
                    lang = input(f"\033[38;2;0;0;255mDe taal van het bestand is niet herkend. Wat is de taal van het bestand? (du, en, fa, la, gr) \033[0m").lower().strip()
                    if lang not in talen:
                        print('\033[38;2;0;0;255mKies uit: du, en, fa, la, gr')
                    else:
                        break
            return bestand1, lang
        except FileNotFoundError:
            print('\033[38;2;0;0;255m    Het bestand bestaat niet. Probeer het opnieuw.')

def review(foutenlijst, fouten, juisten, tijd, opvragen):
    print()
    print(f"""Hoeveelheid fouten: {fouten}
Hoeveelheid juist: {juisten}
Hoeveelheid vragen: {len(opvragen)}
Hoeveelheid tijd: {tijd}
Cijfer: {round(juisten/(juisten+fouten)*10, 1)}""")
    if not foutenlijst:
        print('\nJe had alles goed!')
    else:
        foutenlijst.sort(key=str.lower)
        print("Je had fout:")
        for woordfout in foutenlijst:
            print(f"    {woordfout}: {opvragen[woordfout]}")
        print()
        while True:
            opnieuw = input('Wil je je fouten opnieuw doen? [y/n]\033[0m ').lower().strip()
            if opnieuw == 'y':
                opvragen1 = {}
                for fout in foutenlijst:
                    opvragen1[fout] = opvragen[fout]
                opvragenfunc(opvragen1)
                break
            elif opnieuw == 'n':
                break
            else:
                print('\033[38;2;0;0;255mVul Y of N in.')

def opvragenfunc(opvragen):
    start = time.time()
    woorden = list(opvragen.keys())
    random.shuffle(woorden)
    fouten = 0
    juisten = 0
    foutenlijst = []

    print(f'\n\033[38;2;0;0;255mHoeveelheid woorden die opgevraagd gaan worden: {len(opvragen)}')

    for woord in woorden:
        a = input(f"\n{woorden.index(woord)+1}. Wat is \033[1;38;2;0;0;255m{woord}\033[0m\033[38;2;0;0;255m in het {taleno[l2ob]}? \033[0m").lower().strip()
        if a == opvragen[woord].lower().strip():
            print("\033[38;2;0;0;255mJuist!")
            juisten += 1
                
        else:
            print(f'\033[38;2;0;0;255mFout. Het was \033[1;38;2;0;0;255m{opvragen[woord]}\033[0m\033[38;2;0;0;255m.')
            if a in ['', '?']:
                fouten += 1
                foutenlijst.append(woord)
            else:
                print()
                while True:
                    greken = input('Wil je het toch goedrekenen? (Doe dit alleen bij typfout/meerdere goede antwoorden.) Y[es]/ N[o] \033[0m').lower().strip()
                    if greken == 'n':
                        fouten += 1
                        foutenlijst.append(woord)
                        print('\033[38;2;0;0;255mHet is fout gerekend.\n')
                        break
                            
                    elif greken == 'y':
                        print('\033[38;2;0;0;255mHet is juist gerekend.\n')
                        juisten += 1
                        break
                     
                    else:
                        print('\033[38;2;0;0;255mVoer Y of N in.')
    end = time.time()
    tijd = minuten(round(end - start, 0))

    review(foutenlijst, fouten, juisten, tijd, opvragen)

talen = {'du': 'Duits', 'en': 'Engels', 'fa': 'Frans', 'la': 'Nederlands', 'gr': 'Nederlands'}

print('\033[38;2;0;0;255mWelkom bij de overhoring!\n')

while True:
    try:
        hoeveelhtxts = max(1, int(input('Hoeveel lijsten wil je invoegen? (Het moet allemaal dezelfde taal zijn.) \033[0m')))
        break
    except ValueError:
        print('\033[38;2;0;0;255mVoer een getal in.')

while True:
    opvragen = {}
    difflangs = []
    for w in range(hoeveelhtxts):
        bestand2, lang = bestandsnaam(w)
        difflangs.append(lang)
        with open(bestand2, 'r', encoding='utf-8') as bestand3:
            inhoud = bestand3.read()
            opvragen1 = ast.literal_eval(inhoud)
            opvragen = opvragen | opvragen1

    if len(set(difflangs)) <= 1:
        break
    else:
        print('\033[38;2;0;0;255mDe talen van de bestanden zijn niet hetzelfde. Probeer het opnieuw. \033[0m \n')


with open(bestand2, 'r', encoding='utf-8') as bestand:
    inhoud = bestand.read()

    l2ob = difflangs[0]

    if l2ob in ["la", 'gr']:
        taleno = {'la': 'Nederlands', 'gr': 'Nederlands'}
        
    else:
        while True:
            naarovanuit = input(f"\033[38;2;0;0;255mWil je het naar het {talen[l2ob]} of vanuit het {talen[l2ob]}? (Typ N(aar) of V(anuit)) \033[0m").lower().strip()
            if naarovanuit not in ["n", "v"]:
                print('Kies uit n of v')
            else:
                break
        if naarovanuit == "n":
            taleno = {'du': 'Duits', 'en': 'Engels', 'fa': 'Frans'}
            opvragen1 = opvragen
            opvragen = {v: k for k, v in opvragen1.items()}
            
        elif naarovanuit == "v":
            taleno = {'du': 'Nederlands', 'en': 'Nederlands', 'fa': 'Nederlands'}

if len(opvragen) == 0:
    print('\033[38;2;0;0;255mEr zijn geen woorden om op te vragen. Het programma wordt afgesloten.\033[0m')
else:
    opvragenfunc(opvragen)

print('\n\033[38;2;0;0;255mOverhoring voltooid!\033[0m')