from fraction import Fraction
def Harmonic(n):
    result = Fraction(0,1)
    for x in range(1, 1+n):
        frac = Fraction(1,x)
        result += frac
    print(result)

def Two(n):
    result = Fraction(0,1)
    for x in range(1, n+1):
        frac = (Fraction(1,2)**x)
        result += frac
    print(result)
def Zero(n):
    result = Fraction(0,1)
    for x in range (1, 1+n):
        frac = (Fraction(1,2)**x)
        result += frac
    print(Fraction(2,1) - result)
def Riemann(n, b):
    num = n
    k = 1
    for i in b:
        frac = Fraction(0, 5)
        for j in range(k, n + 1):
            frac += Fraction(1, j) ** i
        print("R(" + str(n) + "," + str(i) + ")= " + str(frac))
        print("R(" + str(n) + "," + str(i) + ")~={:.8f}".format(frac.approximate()))



print('Welcome to Fun with Fractions')
while True:
    try:
        userRes = int(input('Enter Number of iterations (integer>0):\n'))
        Two(userRes)
        break
    except ValueError:
        userRes = int(input('Enter Number of iterations (integer>0):\n'))
        continue
