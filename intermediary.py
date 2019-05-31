import numpy as np
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

def text_to_morse(text):
    morsecode = ''
    morse = ''
    for letter in text:
        morse = morsedictionary.get(letter.upper())
        if morse:
            morsecode += morse + " "
    return morsecode[:-3]

def morse_to_binary(morsecode):
    binary = ''
    for letter in morsecode:
        for numeral, char in enumerate(letter):
            if char == ".":
                binary += '1'
            elif char == "-":
                binary += '111'
            elif char == " ":
                binary += '0'
            binary += '0'
    return binary[:-1]


def binary_to_audio(binary):
    frequency = 440
    sound_unit = 0.25
    sampling_rate = 48000
    audio = []
    num_samples = int(sampling_rate * sound_unit)
    for bit in binary:
        if bit == '1':
            audio.append([np.sin(2 * np.pi * frequency * x / sampling_rate) for x in range(num_samples)])
        else:
            audio.append([0] * num_samples)
    return audio

def binary_to_morse(binary):
    morse_words = []
    morsecode = ''
    words = binary.split("0000000")
    for word in words:
        letters = word.split("000")
        for letter in letters:
            letter_parts = letter.split("0")
            for letter_part in letter_parts:
                if letter_part == "1":
                    morsecode += "."
                else: 
                    morsecode += "-"
            morsecode += " "
        morse_words.append(morsecode)
        morsecode = ''
    return morse_words

def morse_to_text(morsecode):
    text = ''
    for word in morsecode:
        morse_letters = word.split()
        for morse_letter in morse_letters:
            letter = reversemorsedictionary.get(morse_letter)
            text += letter
        text += ' '
    return text

def audio_to_morse(audio):
    audio = []
    morsecode = ''
    return morsecode