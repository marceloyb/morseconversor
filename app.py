import sys
import os.path
from filemanager import *
from intermediary import *

#get input and return wav audio for it
def to_audio(extension, file_input):
    if extension == Extension.MORSE.value:
        audio = binary_to_audio(file_input)
        audio = np.reshape(audio, -1)

    elif extension == Extension.TEXT.value:
        morsecode = text_to_morse(file_input)
        binary = morse_to_binary(morsecode)
        audio = binary_to_audio(binary)
        audio = np.reshape(audio, -1)
    
    return audio

# get input and return morse code for it
def to_morse(extension, file_input):
    if extension == Extension.TEXT.value:
        morsecode = text_to_morse(file_input)
        binary = morse_to_binary(morsecode)

    elif extension == Extension.AUDIO.value:
        binary = audio_to_binary(file_input)

    return binary

#get input and return ascii text for it
def to_text(extension, file_input):
    if extension == Extension.MORSE.value:
        morse = binary_to_morse(file_input)
        text = morse_to_text(morse)

    elif extension == Extension.AUDIO.value:
        binary = audio_to_binary(file_input)
        morsecode = binary_to_morse(binary)
        text = morse_to_text(morsecode)
    
    return text
     

def main():
    arg, extension = os.path.splitext(sys.argv[1])
    file_input = read_file(sys.argv[1])

    if extension == Extension.TEXT.value:
        audio = to_audio(Extension.TEXT.value, file_input)
        morse = to_morse(Extension.TEXT.value, file_input)
        text = file_input
    
    elif extension == Extension.AUDIO.value:
        audio = file_input
        morse = to_morse(Extension.AUDIO.value, file_input)
        text = to_text(Extension.AUDIO.value, file_input)

    elif extension == Extension.MORSE.value:
        audio = to_audio(Extension.MORSE.value, file_input)
        morse = file_input
        text = to_text(Extension.MORSE.value, file_input)        

    else:
        raise Exception("This extension is not accepted in this program. Only txt, wav or morse files accepted.")
    
    write_audio(audio)
    write_morse(morse)
    write_text(text)

if __name__ == '__main__':
    main()