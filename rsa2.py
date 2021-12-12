import numpy as np
import random
import cmath
import math


#generate two large odd numbers of a specific bit size
def generateLargeOdd(bitSize):
    a = random.getrandbits(128) | 1
    #print(a)
    return a


#Primality check using Fermat Theorem to identify base 2 pseudoprimes
def checkPseudoprimeFermat(num):
    base = 2
    if (checkPrimeModularExponentiation(num-1, base, num)) == 1:
        return True #returns true if prime
    return False #returns false if composite


#Primality check using Modular Exponentiation to the base 2
def checkPrimeModularExponentiation(num2, base, num):
    res = 1 
    base%=num
    if (base == 0) :
        res = 0
        return res
    while (num2 > 0) :
        #print("base:", base)
        if ((int(num2) & 1) == 1) :
            res = (res * base) % num
        base = (base * base) % num
        num2 = int(num2) >> 1 # num = num/2
    #print("/n/n/nRESULTTTTTT:", res)
    return res #if res is 1 or n-1 it is prime



#Helper function for Miller Rabin test
def millerHelper(d, n):
    a = 2 + random.randint(1, n - 4)
    #print("base:", a)
    x = checkPrimeModularExponentiation(d, a, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False

 

#Primality check using Miller Rabin test
def checkPrimeMillerRabin(n):
    k = 4 #no. of iterations
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    for i in range(k): #Iterating k times
        if not millerHelper(d, n):
            return False
    return True




#Primality check using Trial Division
def checkPrimeTrialDivision(a):
    for i in range(2, math.ceil(pow(a, 0.5))):
        if a%i == 0: 
            return False
    return True



#Find relative prime of a number
def relativePrime(p,q):
    phi = (p-1)*(q-1)
    for e in range(3, phi, 2):
        if phi%e != 0:
            return e



#Extended Euclid
def egcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t # return gcd, x, y



#To find modular multiplicative inverse of e 
def modularMultiplicativeInverse(e, p, q):
    phi = (p-1)*(q-1)
    gcd, x, y = egcd(e, phi)
    if x < 0:
        x += phi
    return x



def rsaEncrypt(M, e, n):
    C = []
    for m in M:
        ex = checkPrimeModularExponentiation(e, m, n)
        #ex = (pow(m, e))%n
        C.append(int(ex))
    C = np.array(C)
    return C


def rsaDecrypt(C, d, n):
    MD = []
    for c in C:
        de = checkPrimeModularExponentiation(d, c, n)
        #de = (pow(c, d))%n
        MD.append(de)
    MD = np.array(MD)
    return MD



def rsaHelper(M):
    count = 0
    #a = 6967
    
    largePrimes = []
    while(count<2):
        oddNum = generateLargeOdd(128)
        if count==1 and oddNum == largePrimes[0]: continue
        if checkPrimeModularExponentiation(oddNum-1, 2, oddNum)!=1: 
            continue
        if not checkPseudoprimeFermat(oddNum): 
            if not checkPrimeMillerRabin(oddNum):
                continue #continue searching if number is composite
        #if not checkPrimeTrialDivisionLoop(oddNum):
            #continue 
        count+=1
        largePrimes.append(oddNum) 


    #largePrimes = [6967, 7253]

    a, b = largePrimes[0], largePrimes[1]
    #print("First large prime number p:", a, '\n')
    #print("Second large prime number q:", b, '\n')
    n = a*b
    #print("n = p * q:", n, '\n')
    e = relativePrime(a, b)
    #print("e:", e, '\n')
    d = modularMultiplicativeInverse(e, a, b)
    #print("d:", d, '\n')
    C = rsaEncrypt(M, e, n)
    MD = rsaDecrypt(C, d, n)
    #print("phi(n):", (a-1)*(b-1), '\n')
    #print("Original message M:", M, '\n')
    #print("Encrypted message (Cyphertext) C:", C, '\n')
    #print("Decrypted message M_decrypted:", MD, '\n')
    print("hey")
    return MD




if __name__ == '__main__':

    #VC = [0,2,0,2]
    VC = [5,7, 8, 10]
    VC = np.array(VC)
    VCD = rsaHelper(VC)
    print(np.allclose(VC, VCD))

    

