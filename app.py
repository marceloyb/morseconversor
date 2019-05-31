#!/usr/bin/python3
import sys
import os.path
import scipy.io.wavfile as wavefile
from filemanager import *
from intermediary import *



#get input and return wav audio for it
def audio(extension):
    file_input = read_file(sys.argv[1])
    if extension == Extension.MORSE.value:
        audio = binary_to_audio(file_input)
        audio = np.reshape(audio, -1)
        write_audio(audio)

    elif extension == Extension.TEXT.value:
        morsecode = text_to_morse(file_input)
        morsecode = morse_to_binary(morsecode)
        audio = binary_to_audio(morsecode)
        audio = np.reshape(audio, -1)
        write_audio(audio)

# get input and return morse code for it
def morse(extension):
    file_input = read_file(sys.argv[1])
    if extension == Extension.TEXT.value:
        morsecode = text_to_morse(file_input)
        morsecode = morse_to_binary(morsecode)
        write_morse(morsecode)

    elif extension == Extension.AUDIO.value:
        morsecode = audio_to_morse(file_input)

#get input and return ascii text for it
def text(extension):
    file_input = read_file(sys.argv[1])
    if extension == Extension.MORSE.value:
        text = binary_to_morse(file_input)
        text = morse_to_text(text)
        write_text(text)

    elif extension == Extension.AUDIO.value:
        morsecode = audio_to_morse(file_input)
        text = morse_to_text(morsecode)

        

def main():
    arg, extension = os.path.splitext(sys.argv[1])
    if extension == Extension.TEXT.value:
        audio(Extension.TEXT.value)
        morse(Extension.TEXT.value)
    
    elif extension == Extension.AUDIO.value:
        # morse(Extension.AUDIO.value)
        # text(Extension.AUDIO.value)
        raise NotImplementedError

    elif extension == Extension.MORSE.value:
        audio(Extension.MORSE.value)
        text(Extension.MORSE.value)        

    else:
        print("This extension is not accepted in this program. Only txt, wav or morse files accepted.")

if __name__ == '__main__':
    main()