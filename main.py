from ascii_art import LOGO
from morse_dict import MORSE_CODE_DICT, inverted_map
import click

# print(LOGO)
print('Welcome to MORSE Code Converter.\n\n')
choice = input('Choose Morse Code translator or Morse Code decoder. \nType T for Translator or D for Decoder: (T/D)  ')

def morse_translator():
    print('\n'*10)
    click.clear()
    print('You selected Morse translator.')
    message = input('What message do you want to encrypt?  ')
    cipher = ""

    for char in message:
        if char != " ":
            cipher += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            cipher += ' '

    print(f"The Morse Code for your message is: {cipher}")


def morse_decoder():
    click.clear()
    print('You selected Morse decoder.')
    message = input('What the Morse code you like to decipher?  ')
    message += ' '
    decipher = ''
    char_code = ''
    space_count = 0

    for code in message:
        # checks for space
        if code != ' ':
            # counter to keep track of space
            space_count = 0
            # storing morse code of a single character
            char_code += code

        # in case of space
        else:
            # if space_count = 1 that indicates a new character
            space_count += 1
            # if i = 2 that indicates a new word
            if space_count == 2:
                # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += inverted_map[char_code]
                char_code = ''

    print(f"The decrypted message is '{decipher}'")


if choice.lower() == "t":
    morse_translator()

elif choice.lower() == "d":
    morse_decoder()
