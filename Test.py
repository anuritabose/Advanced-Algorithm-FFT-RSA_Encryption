import sys
import importlib
import argparse
import numpy as np
import random
import cmath
import math
from dft import dft, inv_dft
from fft import fft, inv_fft
from rsa import *


#arguments for dft, fft, inverse dft and inverse fft
parameters1 = []
parameters2 = []
i=4
while i<2048:
    param1 = list(np.random.randint(low = 0, high = 1000, size = i))
    parameters1.append(param1)
    param2 = list(np.random.randint(low = 0, high = 1000, size = i)) 
    parameters2.append(param2)
    i=i*2

#arguments for RSA encryption and decryption
VC = [[5,8,12,56], [0j, (2+1.1102230246251565e-16j), (1.4997597826618576e-32-2.4492935982947064e-16j), (2+4.440892098500626e-16j)]]
bits = []
for i in range(7, 11):
    bits.append(2**i)
    

def test_case():  

    try:
        for test in range(len(parameters1)):
            VA = dft(parameters1[test])
            np.allclose(VA, np.fft.fft(parameters1[test]))
            print("Test Case", (test+1), "for the function DFT passed")
    except:
        print("Test Case", (test+1), "for the function DFT failed")

    try:
        for test in range(len(parameters1)):
            VA = fft(parameters1[test])
            np.allclose(VA, np.fft.fft(parameters1[test]))
            print("Test Case", (test+1), "for the function FFT passed")
    except:
        print("Test Case", (test+1), "for the function FFT failed")

def test_case2():

    try:
        for test in range(len(VC)):
            mat = VC[test]
            
            mat2 = rsaHelper(mat)
            mat = np.array(mat)
            mat2 = np.array(mat2)
            np.array_equiv(mat, mat2)
            print("Test Case", (test+1), "for RSA encryption and decryption passed")
    except:
        print("Test Case", (test+1), "for  RSA encryption and decryption failed")
    



if __name__ == "__main__":
    test_case()
    test_case2()
