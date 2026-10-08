naamfile = "dicts/" + input('Wat is de naam van de file? (Zorg ervoor dat de laatste 2 letters de afkorting van de taal zijn.) ') + ".txt"

print("""\033[38;2;0;0;255mTyp de woorden.
Zorg ervoor dat het woord in de andere taal eerst staat, daarna een is teken (=) en daarna het woord in het Nederlands.
    (Tussen de 2 woorden moet precies ' = ' staan.)
Als je een nieuw woord wilt intypen, zorg er dan voor dat je op enter klikt en daarna het nieuwe woord intypt.
Als je na een woord ingetypt te hebben 2 keer op enter klikt kun je geen woorden meer invullen.\033[0m""")
regels = []

while True:
    regel = input()
    if regel == '':
        break
    regels.append(regel)

volledige_tekst = "\n".join(regels)
volledige_tekst2 = '{"' + volledige_tekst.replace(' = ', '\": \"').replace('\n', '", "') + '"}'

with open(naamfile, "w", encoding = 'utf-8') as bestand:
    bestand.write(volledige_tekst2)
