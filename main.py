import matplotlib.pyplot as plotter
from scipy.io import wavfile as wav
from scipy.fftpack import fft as fourier
import numpy as np


rate, data = wav.read("sound.wav")
ff_out = fourier(data)

plotter.plot(data, ff_out)
plotter.show()



