import keyboard

negr = {'a': 'α', 'b': 'β', 'c': 'ψ', 'd': 'δ', 'e': 'ε', 'f': 'φ', 'g': 'γ', 'h': 'η', 'i': 'ι', 'j': 'ξ', 'k': 'κ', 'l': 'λ', 'm': 'μ', 'n': 'ν', 'o': 'ο', 'p': 'π', 'q': ';', 'r': 'ρ', 's': 'σ', 't': 'τ', 'u': 'θ', 'v': 'ω', 'w': 'ς', 'x': 'χ', 'y': 'υ', 'z': 'ζ',
        'A': 'Α', 'B': 'Β', 'C': 'Ψ', 'D': 'Δ', 'E': 'Ε', 'F': 'Φ', 'G': 'Γ', 'H': 'Η', 'I': 'Ι', 'J': 'Ξ', 'K': 'Κ', 'L': 'Λ', 'M': 'Μ', 'N': 'Ν', 'O': 'Ο', 'P': 'Π', 'Q': '·', 'R': 'Ρ', 'S': 'Σ', 'T': 'Τ', 'U': 'Θ', 'V': 'Ω', 'W': 'Σ', 'X': 'Χ', 'Y': 'Υ', 'Z': 'Ζ',
        '?': ';', ':': '·'}
ltsa = {'v': 'ὡ', 'V': 'Ὡ', 'o': 'ὁ', 'O': 'Ὁ', 'i': 'ἱ', 'I': 'Ἱ', 'A': 'Ἁ', 'a': 'ἁ', 'R': 'Ῥ', 'r': 'ῥ', 'H': 'Ἡ', 'h': 'ἡ', 'y': 'ὑ', 'Y': 'Ὑ', 'e': 'ἑ', 'E': 'Ἑ'}
ltsl = {'v': 'ὠ', 'V': 'Ὠ', 'o': 'ὀ', 'O': 'Ὀ', 'i': 'ἰ', 'I': 'Ἰ', 'A': 'Ἀ', 'a': 'ἀ', 'R': 'Ῥ', 'r': 'ῤ', 'H': 'Ἠ', 'h': 'ἠ', 'y': 'ὐ', 'e': 'ἐ', 'E': 'Ἐ'}
ltis = {'v': 'ῳ', 'V': 'ῼ', 'H': 'ῌ', 'h': 'ῃ', 'a': 'ᾳ', 'A': 'ᾼ'}
ltai = {'v': 'ᾡ', 'V': 'ᾩ', 'H': 'ᾙ', 'h': 'ᾑ', 'a': 'ᾁ', 'A': 'ᾉ'}
ltli = {'v': 'ᾠ', 'V': 'ᾨ', 'H': 'ᾘ', 'h': 'ᾐ', 'a': 'ᾀ', 'A': 'ᾈ'}

a = i = l = au = False

print('Grieks typen ingeschakeld')

def rt(gebeurtenis):
    global i, a, l, au
    
    if gebeurtenis.event_type == keyboard.KEY_DOWN:
        try:
            if gebeurtenis.name == 'esc':
                au = not au
                if au:
                    print('Grieks typen uitgeschakeld')
                else:
                    print('Grieks typen ingeschakeld')

            if au:
                return

            if keyboard.is_pressed('ctrl') or keyboard.is_pressed('alt'):
                return
        
            if gebeurtenis.name == '[':
                keyboard.press_and_release("backspace")
                i = True
                return
            
            if gebeurtenis.name == '{':
                keyboard.press_and_release("backspace")
                a = True
                l = False
                return

            if gebeurtenis.name == '}':
                keyboard.press_and_release("backspace")
                l = True
                a = False
                return
            
            if gebeurtenis.name in negr:
                if i and not a and not l and gebeurtenis.name in ['v', 'V', 'h', 'H', 'a', 'A']:
                    keyboard.press_and_release("backspace")
                    keyboard.write(ltis[gebeurtenis.name])
                    a = i = l = False
                elif a and not i and gebeurtenis.name in ['v', 'V', 'o', 'O', 'i', 'I', 'A', 'a', 'R', 'r', 'H', 'h', 'y', 'Y', 'e', 'E']:
                    keyboard.press_and_release("backspace")
                    keyboard.write(ltsa[gebeurtenis.name])
                    a = i = l = False
                elif l and not i and gebeurtenis.name in ['v', 'V', 'o', 'O', 'i', 'I', 'A', 'a', 'R', 'r', 'H', 'h', 'e', 'E', 'y']:
                    keyboard.press_and_release("backspace")
                    keyboard.write(ltsl[gebeurtenis.name])
                    a = i = l = False

                elif a and i and gebeurtenis.name in ['v', 'V', 'h', 'H', 'a', 'A']:
                    keyboard.press_and_release("backspace")
                    keyboard.write(ltai[gebeurtenis.name])
                    a = i = l = False
                elif l and i and gebeurtenis.name in ['v', 'V', 'h', 'H', 'a', 'A']:
                    keyboard.press_and_release("backspace")
                    keyboard.write(ltli[gebeurtenis.name])
                    a = i = l = False

                else:
                    a = i = l = False
                    keyboard.press_and_release("backspace")
                    keyboard.write(negr[gebeurtenis.name])
        except KeyboardInterrupt:
            pass

keyboard.hook(rt)
keyboard.wait()
