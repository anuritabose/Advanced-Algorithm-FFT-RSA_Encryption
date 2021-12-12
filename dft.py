import numpy as np
import time
import cmath

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

#code to do pointwise multiplication
def dft_multiply(a,b):
    VA=dft(a)
    VB=dft(b)
    C = []
    for i in range(VA.shape[0]):
        C.append(VA[i]*VB[i])
    return C
    
#driver code
i = 4
poly_a = list(np.random.randint(low = -1000, high = 1000, size = i))
poly_b = list(np.random.randint(low = -1000, high = 1000, size = i))
start_time = time.time()
dft_res_a=dft(poly_a)
dft_res_b=dft(poly_b)
C = dft_multiply(dft_res_a,dft_res_b)
VC=inv_dft(C)
print(np.fft.ifft(C))
print(VC)
print("\n\n")
#print(time.time()-start_time)





    
    
    
