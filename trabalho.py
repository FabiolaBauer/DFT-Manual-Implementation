import matplotlib.pyplot as plt
import numpy as np

Fs = 1000;  # taxa de amostragem
Ts = 1.0/Fs; # periodo de amostragem
t = np.arange(0,1,Ts) # vetor de tempo

f = 100;   # frequencia do sinal
x1_n = np.sin(2*np.pi*f*t + 0)
f = 300;   # frequencia do sinal
x2_n = np.sin(2*np.pi*f*t + 180)

x_n = x1_n + x2_n

n = len(x_n) # tamanho do sinal
k = np.arange(n) #vetor em k
T = n/Fs
frq = k/T # os dois lados do vetor de frequencia
frq = frq[range(int(n/2))] # apenas um lado

X = np.zeros(n, dtype=complex) # vetor para armazenar a DFT

for k in range(0, n): #para cada frequencia de 0 a Fs-1
    for a in range(0, n): #para cada amostra do sinal no tempo n
        X[k] = X[k] + x_n[a]*(np.cos(2*np.pi*k*a/n) - 1j*np.sin(2*np.pi*k*a/n)) #calculo da DFT
        
    X[k] = X[k]/n #normalização por n (tamanho do sinal)  

modulo = np.zeros(n//2) # vetor para armazenar o modulo da DFT
for k in range(0, n//2): #para cada frequencia de 0 a Fs/2
    modulo[k] = np.sqrt(X[k].real**2 + X[k].imag**2) #calculo do modulo da DFT


fig, ax = plt.subplots(2, 1)
ax[0].plot(t,x_n)
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,modulo,'r')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|X(freq)|')
plt.show()