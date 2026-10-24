import math
import librosa
import soundfile
import random
import numpy

def identity(n): return n

def clamp(n, a = -1, b = 1): return min(max(n, a), b)
def noise(n, scale): return n + random.random() * scale - scale / 2

def overdrive(n, k): return math.tanh(n * k)
def distort(n, k): return clamp(n * k)
def fuzz(n, k, bias = 0.15):
    boosted = n * k + bias
    clipped = clamp(boosted)
    return clamp(clipped - bias / 2)

global reverb_previous
reverb_previous = 0

def reverb(n, feedback = 0.5):
    global reverb_previous

    reverb_previous *= feedback
    reverb_previous += n

    return reverb_previous

def echo(signal, delay = 48000, feedback = 0.8):
    output = numpy.array(signal, dtype = numpy.float64)
    
    for i in range(len(output)):
        if i >= delay:
            past = output[i - delay]
            output[i] += past * feedback
            
    return output

y, sr = librosa.load("test.mp3", sr = None, mono = True)
soundfile.write("output.wav", echo(y), sr)