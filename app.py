#!/usr/bin/python3
import sys
import os.path
from filemanager import *
from intermediary import *



#get input and return wav audio for it
def audio(extension):
    raise NotImplementedError

# get input and return morse code for it
def morse(extension):
    morse = ''
    morsecode = ''
    if extension == Extension.TEXT.value:
        morsecode = text_to_morse(sys.argv[1])
        for letter in morsecode:
            for numeral, char in enumerate(letter):
                if char == ".":
                    morse += '1'
                elif char == "-":
                    morse += '111'
                elif char == " ":
                    morse += '0'
                morse += '0'         
        write_morse(morse)

    # elif extension == Extension.AUDIO.value:


#get input and return ascii text for it
def text(extension):
    text = ''
    if extension == Extension.MORSE.value:
        morse_words = binary_to_morse(sys.argv[1])
    for word in morse_words:
        morse_letters = word.split()
        for morse_letter in morse_letters:
            letter = reversemorsedictionary.get(morse_letter)
            text += letter
        text += ' '
    print(text)

def main():
    arg, extension = os.path.splitext(sys.argv[1])
    if extension == Extension.TEXT.value:
        # audio(Extension.TEXT.value)
        morse(Extension.TEXT.value)
    
    elif extension == Extension.AUDIO.value:
        morse(Extension.AUDIO.value)
        text(Extension.AUDIO.value)

    elif extension == Extension.MORSE.value:
        # audio(Extension.MORSE.value)
        text(Extension.MORSE.value)        

    else:
        print("This extension is not accepted in this program. Only txt, wav or morse files accepted.")

if __name__ == '__main__':
    main()