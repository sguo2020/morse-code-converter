from ascii_art import LOGO
from morse_dict import MORSE_CODE_DICT, inverted_map

print(LOGO)
print('Welcome to MORSE Code Converter.')
choice = input('Choose Morse Code translator or Morse Code decoder. T for Translator and D for Decoder: (T/D)  ')


def Morse_decoder():
    print('You selected Morse decoder.')
    message = input('What the Morse code you like to decipher?  ')
    message += ' '
    decipher = ''
    char_code = ''
    print(message, decipher, char_code, 15)
    for code in message:
        # checks for space
        if (code != ' '):
            # counter to keep track of space
            space_count = 0
            # storing morse code of a single character
            char_code += code

        # in case of space
        else:
            print(char_code, 26)
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
    Morse_translator()

elif choice.lower() == "d":
    Morse_decoder()