import numpy as np
import matplotlib.pyplot as plt
 
t=np.arange(0,3,0.02)
freqs=[1, 1]
amps=[1, 0.5]
phis=[-np.pi/2, np.pi/6]
 

for (freq, amp, phi) in zip(freqs,amps,phis):
    omega=2*np.pi*freq
    signal=amp*np.cos(omega*t+phi)
    plt.plot(t,signal, label=f'{freq} Hz')

plt.legend()
plt.show()