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

reversemorsedictionary = {morsedictionary[k] : k for k in morsedictionary}

def text_to_morse(filename):
    morsecode = ''
    with open(filename, "r") as f:
        content = f.read()
        for letter in content:
            morse = morsedictionary.get(letter.upper())
            if morse:
                morsecode += morse + " "
    return morsecode

def binary_to_morse(filename):
    morse_words = []
    morsecode = ''
    with open(filename, "r") as f:
        binary = f.read()
        words = binary.split("0000000")
        for word in words:
            letters = word.split("000")
            for letter in letters:
                letter_parts = letter.split("0")
                for letter_part in letter_parts:
                    if letter_part == "111":
                        morsecode += "-"
                    else: 
                        morsecode += "."
                morsecode += " "
            morse_words.append(morsecode)
            morsecode = ''
    return morse_words
