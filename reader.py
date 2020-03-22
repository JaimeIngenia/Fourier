import scipy.io.wavfile as wav
import matplotlib.pyplot as plotter


rate, data = wav.read("sound.wav")

print(rate)
print(data)

plotter.plot(data)
plotter.show()