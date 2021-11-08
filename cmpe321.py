import matplotlib.pyplot as plt
import numpy as np
num_pts=100
t=np.arange(0,1,1/num_pts)

x=5*np.sin(2*np.pi*25*t) + 3*np.sin(2*np.pi*15*t)

fft_coeffs=1/num_pts*np.fft.fft(x)
freqs=np.fft.fftfreq(len(x),1/num_pts)
plt.stem(freqs, np.abs(fft_coeffs), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
