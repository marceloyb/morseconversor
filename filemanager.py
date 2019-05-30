from enum import Enum


class Extension(Enum):
    AUDIO = ".wav"
    MORSE = ".morse"
    TEXT = ".txt"


def write_morse(output):
    with open("code.morse", "w") as f:
        f.write(output[:-6])