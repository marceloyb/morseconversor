#!/usr/bin/python3
import sys
import os.path


morsedictionary = { 'A': '.-', 'B': '-...', 'C': '-.-.',
                    'D': '-..', 'E': '.', 'F': '..-.',
                    'G': '--.', 'H': '....', 'I': '..',
                    'J': '.---', 'K': '-.-', 'L': '.-..',
                    'M': '--', 'N': '-.', 'O': '---',
                    'P': '.--.', 'Q': '--.-', 'R': '.-.',
                    'S': '...', 'T': '-', 'U': '..-',
                    'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...',
                    '8': '---..', '9': '----.', '10': '-----',
                    '\n': '\n', ' ': ' '}

#get input and return wav audio for it
# def audio():
#     with open(sys.argv[1], "r") as f:
#         print(f)

# get input and return morse code for it
def morse(extension):
    text = ''
    if extension == ".txt":
        with open(sys.argv[1], "r") as f:
            content = f.read()
            for letter in content:
                morse = morsedictionary.get(letter.upper())
                if morse:
                    text += morse
                else:
                    text += letter
        with open("code.morse", "w") as f:
            f.write(text)
    # elif extension == ".wav":


#get input and return ascii text for it
def text():
    with open(sys.argv[1], "r") as f:
        content = f.read()

def main():
    arg, extension = os.path.splitext(sys.argv[1])

    if extension == ".txt":
        #audio()
        morse('txt')
    
    elif extension == ".wav":
        morse()
        text()
    
    elif extension == ".morse":
        #audio()
        text()
    
    else:
        print("This extension is not accepted in this program. Only txt, wav or morse files accepted.")

if __name__ == '__main__':
    main()