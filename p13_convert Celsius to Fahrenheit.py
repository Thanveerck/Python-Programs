# take Celsius value using input
c = float(input('Enter temperatures in celsius'))

f = (c*9/5)+32

print('{0} is equal to {1:0.3f} fahrenheit'.format(c, f))