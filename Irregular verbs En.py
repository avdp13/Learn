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

nederlnverb = {
    'zijn': 'be',
    'worden': 'become',
    'beginnen': 'begin',
    'buigen': 'bend',
    'wedden': 'bet',
    'bijten': 'bite',
    'blazen, waaien': 'blow',
    'breken': 'break',
    'brengen': 'bring',
    'uitzenden (radio/TV)': 'broadcast',
    'bouwen': 'build',
    '(ver)branden': 'burn',
    'kopen': 'buy',
    'vangen': 'catch',
    'kiezen': 'choose',
    'komen': 'come',
    'kosten': 'cost',
    'snijden': 'cut',
    'graven': 'dig',
    'doen': 'do',
    'trekken/tekenen': 'draw',
    'dromen': 'dream',
    'drinken': 'drink',
    'besturen (bijv. auto, bus)': 'drive',
    'eten': 'eat',
    'vallen': 'fall',
    'voeden': 'feed',
    'voelen': 'feel',
    'vechten': 'fight',
    'vinden': 'find',
    'passen, op maat maken': 'fit',
    'vliegen': 'fly',
    'verbieden': 'forbid',
    'vergeten': 'forget',
    '(be)vriezen': 'freeze',
    'krijgen': 'get',
    'geven': 'give',
    'gaan': 'go',
    'groeien': 'grow',
    'hebben': 'have',
    'horen': 'hear',
    'verstoppen': 'hide',
    'slaan, raken, treffen': 'hit',
    'vasthouden': 'hold',
    'pijn doen': 'hurt',
    'blijven': 'keep',
    'weten': 'know',
    'leggen': 'lay',
    '(zelf) leren': 'learn',
    'vertrekken': 'leave',
    'uitlenen': 'lend',
    'laten, verhuren': 'let',
    'liggen': 'lie',
    'verlichten, aansteken': 'light',
    'verliezen': 'lose',
    'maken': 'make',
    'menen, bedoelen': 'mean',
    'ontmoeten': 'meet',
    'betalen': 'pay',
    'neerleggen, neerzetten': 'put',
    'lezen': 'read',
    '(be)rijden (fiets, paard etc.)': 'ride',
    'bellen, laten rinkelen': 'ring',
    'omhoog komen, stijgen': 'rise',
    'rennen': 'run',
    'zeggen': 'say',
    'zien': 'see',
    'verkopen': 'sell',
    '(ver)zenden, sturen': 'send',
    'plaatsen, zetten': 'set',
    'schudden': 'shake',
    'schijnen': 'shine',
    'schieten': 'shoot',
    'tonen, laten zien': 'show',
    'sluiten': 'shut',
    'zingen': 'sing',
    'zinken': 'sink',
    'zitten': 'sit',
    'slapen': 'sleep',
    'glijden': 'slide',
    'ruiken': 'smell',
    '(uit)spreken': 'speak',
    'snel verplaatsen': 'speed',
    'spellen': 'spell',
    'besteden (v. tijd en geld)': 'spend',
    'knoeien, morsen, overstromen': 'spill',
    'verspreiden': 'spread',
    'staan': 'stand',
    'stelen': 'steal',
    'kleven, plakken': 'stick',
    'zwemmen': 'swim',
    'nemen': 'take',
    'onderwijzen, lesgeven': 'teach',
    'vertellen': 'tell',
    'denken': 'think',
    'gooien': 'throw',
    'begrijpen, verstaan': 'understand',
    'wakker maken/worden': 'wake',
    'dragen (v. kleding)': 'wear',
    'winnen': 'win',
    'schrijven': 'write'
}

verbnpastsim = {
    'be': 'was, were',
    'become': 'became',
    'begin': 'began',
    'bend': 'bent',
    'bet': 'bet',
    'bite': 'bit',
    'blow': 'blew',
    'break': 'broke',
    'bring': 'brought',
    'broadcast': 'broadcast',
    'build': 'built',
    'burn': 'burnt',
    'buy': 'bought',
    'catch': 'caught',
    'choose': 'chose',
    'come': 'came',
    'cost': 'cost',
    'cut': 'cut',
    'dig': 'dug',
    'do': 'did',
    'draw': 'drew',
    'dream': 'dreamt',
    'drink': 'drank',
    'drive': 'drove',
    'eat': 'ate',
    'fall': 'fell',
    'feed': 'fed',
    'feel': 'felt',
    'fight': 'fought',
    'find': 'found',
    'fit': 'fit',
    'fly': 'flew',
    'forbid': 'forbade',
    'forget': 'forgot',
    'freeze': 'froze',
    'get': 'got',
    'give': 'gave',
    'go': 'went',
    'grow': 'grew',
    'have': 'had',
    'hear': 'heard',
    'hide': 'hid',
    'hit': 'hit',
    'hold': 'held',
    'hurt': 'hurt',
    'keep': 'kept',
    'know': 'knew',
    'lay': 'laid',
    'learn': 'learnt',
    'leave': 'left',
    'lend': 'lent',
    'let': 'let',
    'lie': 'lay',
    'light': 'lit',
    'lose': 'lost',
    'make': 'made',
    'mean': 'meant',
    'meet': 'met',
    'pay': 'paid',
    'put': 'put',
    'read': 'read',
    'ride': 'rode',
    'ring': 'rang',
    'rise': 'rose',
    'run': 'ran',
    'say': 'said',
    'see': 'saw',
    'sell': 'sold',
    'send': 'sent',
    'set': 'set',
    'shake': 'shook',
    'shine': 'shone',
    'shoot': 'shot',
    'show': 'showed',
    'shut': 'shut',
    'sing': 'sang',
    'sink': 'sank',
    'sit': 'sat',
    'sleep': 'slept',
    'slide': 'slid',
    'smell': 'smelt',
    'speak': 'spoke',
    'speed': 'sped',
    'spell': 'spelt',
    'spend': 'spent',
    'spill': 'spilt',
    'spread': 'spread',
    'stand': 'stood',
    'steal': 'stole',
    'stick': 'stuck',
    'swim': 'swam',
    'take': 'took',
    'teach': 'taught',
    'tell': 'told',
    'think': 'thought',
    'throw': 'threw',
    'understand': 'understood',
    'wake': 'woke',
    'wear': 'wore',
    'win': 'won',
    'write': 'wrote'
}

pastsimpnpastpartic = {
    "was, were": "been",
    "became": "become",
    "began": "begun",
    "bent": "bent",
    "bet": "bet",
    "bit": "bitten",
    "blew": "blown",
    "broke": "broken",
    "brought": "brought",
    "broadcast": "broadcast",
    "built": "built",
    "burnt": "burnt",
    "bought": "bought",
    "caught": "caught",
    "chose": "chosen",
    "came": "come",
    "cost": "cost",
    "cut": "cut",
    "dug": "dug",
    "did": "done",
    "drew": "drawn",
    "dreamt": "dreamt",
    "drank": "drunk",
    "drove": "driven",
    "ate": "eaten",
    "fell": "fallen",
    "fed": "fed",
    "felt": "felt",
    "fought": "fought",
    "found": "found",
    "fit": "fit",
    "flew": "flown",
    "forbade": "forbidden",
    "forgot": "forgotten",
    "froze": "frozen",
    "got": "got",
    "gave": "given",
    "went": "gone",
    "grew": "grown",
    "had": "had",
    "heard": "heard",
    "hid": "hidden",
    "hit": "hit",
    "held": "held",
    "hurt": "hurt",
    "kept": "kept",
    "knew": "known",
    "laid": "laid",
    "learnt": "learnt",
    "left": "left",
    "lent": "lent",
    "let": "let",
    "lay": "lain",
    "lit": "lit",
    "lost": "lost",
    "made": "made",
    "meant": "meant",
    "met": "met",
    "paid": "paid",
    "put": "put",
    "read": "read",
    "rode": "ridden",
    "rang": "rung",
    "rose": "risen",
    "ran": "run",
    "said": "said",
    "saw": "seen",
    "sold": "sold",
    "sent": "sent",
    "set": "set",
    "shook": "shaken",
    "shone": "shone",
    "shot": "shot",
    "showed": "shown",
    "shut": "shut",
    "sang": "sung",
    "sank": "sunk",
    "sat": "sat",
    "slept": "slept",
    "slid": "slid",
    "smelt": "smelt",
    "spoke": "spoken",
    "sped": "sped",
    "spelt": "spelt",
    "spent": "spent",
    "spilt": "spilt",
    "spread": "spread",
    "stood": "stood",
    "stole": "stolen",
    "stuck": "stuck",
    "swam": "swum",
    "took": "taken",
    "taught": "taught",
    "told": "told",
    "thought": "thought",
    "threw": "thrown",
    "understood": "understood",
    "woke": "woken",
    "wore": "worn",
    "won": "won",
    "wrote": "written"
}

start = time.time()
woorden = list(nederlnverb.keys())
random.shuffle(woorden)

foutenverb = 0
foutenpastsim = 0
foutenpstpart = 0

juistenverb = 0
juistenpastsim = 0
juistenpstpart = 0

foutenlijst = []

for woord in woorden:
    print()
    verbvraag = input(f"Wat is {woord} in het Engels? ").lower()

    if verbvraag == nederlnverb[woord]:
        print("Juist!")
        juistenverb += 1

        pastsimplevraag = input(f"Wat is de past simple van {nederlnverb[woord]}? ").lower()

        if pastsimplevraag == verbnpastsim[nederlnverb[woord]]:
            print("Juist!")
            juistenpastsim += 1

            pastparticiplevraag = input(f'Wat is de past participle van {verbnpastsim[nederlnverb[woord]]}? ').lower()

            if pastparticiplevraag == pastsimpnpastpartic[verbnpastsim[nederlnverb[woord]]]:
                print('Juist!')
                juistenpstpart += 1
            else:
                print(f'Fout. Het was {pastsimpnpastpartic[verbnpastsim[nederlnverb[woord]]]}')
                foutenpstpart += 1
                foutenlijst.append(woord)
        else:
            print(f"Fout, het was {verbnpastsim[nederlnverb[woord]]}")
            foutenpastsim += 1
            foutenlijst.append(woord)
            
    else:
        print(f"Fout, het was {nederlnverb[woord]}")
        foutenverb += 1
        foutenlijst.append(woord)

end = time.time()
tijd = minuten(round(end - start, 0))

print('\n')
print(f"Hoeveelheid fouten bij present simple: {foutenverb}")
print(f"Hoeveelheid fouten bij past simple: {foutenpastsim}")
print(f"Hoeveelheid fouten bij past participle: {foutenpstpart}\n")

print(f"Hoeveelheid juiste bij present simple: {juistenverb}")
print(f"Hoeveelheid juiste bij past simple: {juistenpastsim}")
print(f"Hoeveelheid juiste bij past participle: {juistenpstpart}\n")
print(f"Hoeveelheid tijd: {tijd}")
#print(f"Cijfer: {round(juisten/(juisten+fouten)*10, 1)}")
print()
print("Je had fout:")
for z in foutenlijst:
    print(f"    {z}, {nederlnverb[z]}, {verbnpastsim[nederlnverb[z]]}, {pastsimpnpastpartic[verbnpastsim[nederlnverb[z]]]}")
