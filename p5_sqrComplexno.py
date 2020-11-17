import cmath
number = 1+2j

squreRoot=cmath.sqrt(number)

print('squre root of {0} is {1:0.3f}+{2:0.3f}j'.format(number,squreRoot.real,squreRoot.imag))

#we format the complex number with .real and .imag to get a shorte answer