import numpy as np
from app import *

fs, audio = scipy.io.wavfile.read('./test/audio.wav')
morse = '1110111010111000101011100010001110111000000011101110111000101011100010101000101110000000101010111000100011101000111010111010001'
text = 'QUEM OUSA VENCE'

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