import cmath

a = float(input('enter the number a!=0 '))
b = float(input('enter number b '))
c = float(input('enter number c'))

rootSum = (b**2)-(4*a*c)

value1 = (-b+cmath.sqrt(rootSum))/(2*a)
value2 = (-b-cmath.sqrt(rootSum))/(2*a)

print('solutions of the equations are {0} and {1}'.format(value1,value2))