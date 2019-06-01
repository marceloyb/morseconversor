import numpy as np
from app import *

audio = read_file('./test/audio.wav')
morse = read_file('./test/code.morse')
text = read_file('./test/text.txt')

def test_morse_to_audio():
    assert np.array_equal(to_audio('.morse', morse), audio)

def test_text_to_audio():
    assert np.array_equal(to_audio('.txt', text), audio)

def test_audio_to_morse():
    assert to_morse('.wav', audio) == morse

def test_text_to_morse():
    assert to_morse('.txt', text) == morse

def test_audio_to_text():
    assert to_text('.wav', audio) == text

def test_morse_to_text():
    assert to_text('.morse', morse) == text