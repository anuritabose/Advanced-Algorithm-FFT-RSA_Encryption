import numpy as np
import time

def dft(x):
    x = np.asarray(x, dtype=np.cdouble)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def inv_dft(C):
    xa = np.asarray(C, dtype=float)
    N = xa.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(2j * np.pi * k * n / N)
    M_inverse = np.linalg.inv(M)
    VC = np.dot(M_inverse,C)
    return VC


def fft(poly_a):
    poly_a = np.asarray(poly_a, dtype=np.cdouble)
    N = poly_a.shape[0]
    if N % 2 > 0:
        raise ValueError("must be a power of 2")
    elif N <= 2:
        return dft(poly_a)
    else:
        even_terms = fft(poly_a[::2])
        odd_terms = fft(poly_a[1::2])
        terms = np.exp((-2j * np.pi * np.arange(N)) / N)
        return np.concatenate([even_terms + terms[:int(N/2)] * odd_terms,
                               even_terms + terms[int(N/2):] * odd_terms])


def inv_fft(x):
    x = np.asarray(x, dtype=complex)
    x_conj = np.conjugate(x)

    y = fft(x_conj)

    y = np.conjugate(y)
    y = y / x.shape[0]

    return y

def fft_multiply(a,b):
    VA=fft(a)
    VB=fft(b)
    VC = []
    for i in range(VA.shape[0]):
        VC.append(VA[i]*VB[i])
    C=inv_fft(VC)
    return C



i = 2048
poly_a = list(np.random.randint(low = -1000, high = 1000, size = i))
poly_b = list(np.random.randint(low = -1000, high = 1000, size = i))
start_time = time.time()
fft_res_a=dft(poly_a)
fft_res_b=dft(poly_b)
C = fft_multiply(fft_res_a,fft_res_b)
VC=inv_dft(C)
print(np.fft.ifft(C))
print(VC)
print("\n\n")
#print(time.time() - start_time)

