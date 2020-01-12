from string import ascii_lowercase
import timeit

morse_alphabet = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
morse_to_char = dict(zip(morse_alphabet, ascii_lowercase))
char_to_morse = dict(zip(ascii_lowercase, morse_alphabet))


def recurse(smorse, remaining = set(morse_alphabet), found = []):
    if not smorse:
        yield found
        return
    
    for morse in remaining:
        if morse == smorse[:len(morse)]:
            found.append(morse)
            trim = remaining.copy()
            trim.remove(morse)
            yield from recurse(smorse[len(morse):], trim, found)
            found.pop()

def smalpha(smorse):
    for found in recurse(smorse):
        return ''.join([morse_to_char[morse] for morse in found])

def encode(string: str):
    return ''.join(char_to_morse[char] for char in string)

def check(input):
    output = smalpha(input)
    assert encode(output) == input
    assert set(output) == set(ascii_lowercase)
    return output

def challenge():
    check('.--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..')
    return print('Challenge Passed!')

challenge()