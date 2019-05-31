from enum import Enum
import scipy.io.wavfile


class Extension(Enum):
    AUDIO = ".wav"
    MORSE = ".morse"
    TEXT = ".txt"

def read_file(filename):
    with open(filename, "r") as f:
        content = f.read()
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