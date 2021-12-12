import numpy as np
from fft import dft,fft,inv_dft,inv_fft
import time
mat_size = 512
upper_limit = 255
lower_limit=0
matrix = np.random.randint(lower_limit,upper_limit,size=(mat_size,mat_size))

def twodfft(matrix):
    # intialize two matrix of same size of orginially generated random matrix
    # one matrix to store the result of FFT of row vectors 
    # another one to store the result of FFT of column vectors of the matrix generated in the previous step 
    z_rows = np.zeros((mat_size,mat_size),dtype=complex)
    z_cols = np.zeros((mat_size,mat_size),dtype=complex)
    # print(z_rows)
    # print(z_cols)
    # store the FFT of row vectors in z_rows
    # every row of z_rows contains FFT of row vector of "matrix"
    for i in range(len(matrix)):
        z_rows[i] = fft(matrix[i])

    # apply FFT on column vectors and store the resultant column vector in z_cols as columns
    # every column of z_cols contains the FFT of column vectors of z_rows
    for i in range(len(z_rows[0])):
        z_cols[:,i] = fft(z_rows[:,i])  
    return z_cols

#print(z_cols)
def inv_2dfft(z_cols):
    i_rows = np.zeros((mat_size,mat_size),dtype=complex)
    i_cols = np.zeros((mat_size,mat_size),dtype=complex)

    for i in range(len(z_cols[0])):
        i_rows[i] = inv_fft(z_cols[i])
    for i in range(len(z_cols[0])):
        i_cols[:,i] = inv_fft(i_rows[:,i])
    return i_cols

#driver program
z_cols = twodfft(matrix)
i_cols = inv_2dfft(z_cols)
start_time = time.time()
if(np.allclose(z_cols, np.fft.fft2(matrix))):
    print("The output of the 2D fft matches the numpy function's output for the 2D fft")

if(np.allclose(i_cols, np.fft.ifft2(z_cols))):
    print("The output of the 2D fft matches the numpy function's output for the 2D fft")
print(time.time() - start_time)



