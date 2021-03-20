from math import pi, exp, sqrt, sin, cos

print(' ')

def AddMult(_a, _b, _c): 
    return _a + _b * _c

print(' ')
print('AddMult(2, 3, 5): ' + str(AddMult(2, 3, 5)))

def SinFunc(): 
    # return sin(pi / 2) + ((cos(pi / 2)) / 2)
    return AddMult(sin(pi/2),cos(pi/2),1/2)

print(' ')
print ('SinFunc: ' + str(SinFunc()))

def SumExpo(_x):
    if isinstance(_x, int): 
        # return sqrt((1 - exp(-_x)) + (_x * exp(-_x)))
        return sqrt(AddMult(1-exp(-_x),_x*exp(-_x),_x))
        #                   |  A     | |  B      | | C |
    else: 
        return 'Please use an integer to receive an input.'

print(' ')
print('SumExpo(5): ' + str(SumExpo(5)))
print('SumExpo(5.2): ' + SumExpo(5.2))
print(' ')