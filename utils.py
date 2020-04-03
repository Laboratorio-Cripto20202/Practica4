from random import randint

import math

#Saca el valor 2-adico del número n
def get2adicVal(n): 
    val = 0
    num = n
    while (num % 2 == 0):
        val = val + 1
        #floor division
        num = num // 2
    return val

#Obtenemos una base a, donde gcd(a,n) = 1
def getA(n):
    if n <= 4: 
        return n
    r = randint(2,n-2)
    while math.gcd(r,n) != 1:
        r = randint(2,n-2)
    return r

#Verificamos si un número es congruente con otro modulo n
def congruentWithBMod(a,b,mod):
    return (a) == (b % mod)