from enum import Enum
import os
import scipy.io.wavfile


class Extension(Enum):
    AUDIO = ".wav"
    MORSE = ".morse"
    TEXT = ".txt"

def read_file(filename):
    arg, extension = os.path.splitext(filename)
    with open(filename, "r") as f:
        if extension == Extension.AUDIO.value:
            fs, content = scipy.io.wavfile.read(filename)
        else:
            content = f.read().rstrip()
    return content 

def write_morse(output):
    with open("code.morse", "w") as f:
        f.write(output)

def write_text(output):
    with open("text.txt", "w") as f:
        f.write(output)

def write_audio(output):
    sampling_rate = 48000
    # print(output)
    scipy.io.wavfile.write('audio.wav', sampling_rate, output)