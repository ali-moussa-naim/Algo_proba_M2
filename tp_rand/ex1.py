"""
def toto():
    for j in range(10):
        yield j

for j in toto():
    print()
"""

def gen_alea_B(n):
    X0 = 0
    Xn = 0
    a = 3141592653 
    c = 2718281829 
    m = (1 << 35)

    for i in range(n):
        Xn = (a * X0 + c)
        X0 = Xn % m
    
    return X0 / m

def gen_alea_C(n):
    X0 = 0
    a = (1 << 7) + 1
    c = 1
    m = (1 << 35)

    for i in range(n):
        Xn = (a * X0 + c)
        X0 = Xn % m
    
    return X0/m
    

def gen_alea_D(n):
    X0 = 47594118
    a = 23
    c = 0
    m = 10**8 + 1

    for i in range(n):
        Xn = (a * X0 + c)
        X0 = Xn % m
    
    return X0 / m

def gen_alea_F(n):
    X0 = 314159265
    a = (1 << 18) + 1 
    c = 1 
    m = (1 << 35)

    for i in range(n):
        Xn = (a * X0 + c)
        X0 = Xn % m
    
    return X0 / m


#--------------------------------------TEST-----------------------------------
n = 100
alea_B = gen_alea_B(n)
alea_C = gen_alea_C(n)
alea_D = gen_alea_D(n)
alea_F = gen_alea_F(n)
print(alea_B)
print(alea_C)
print(alea_D)
print(alea_F)
