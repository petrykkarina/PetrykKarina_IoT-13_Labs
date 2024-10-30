from math import atan, tan, log

x = -0.9
h = 0.05

def cotan(formul):
    return (1/tan(formul))

while x <= -0.4:
    if x <= -0.7:
        result = atan(x ** 3)
    elif -0.7<x<=-0.6:
        result = tan(x + log(abs(x)))
    elif x >= -0.6:
        result = cotan(x**2)
    
    print(f'result= ' , result)
    x += h
    x = x.__round__(2)
    print(x)

n = 1
result_final = 0.0
result_curent = 0.0
x = 1
deviation = 0.00001

# виклик циклів
while x <= 1.5:
    result_curent = ((x - 1) ** n)/(n*x**n)
    result_final += result_curent
    while result_curent.__abs__() > deviation:
        result_curent = ((x - 1) ** n)/(n*x**n)
        result_final += result_curent       
        n += 1
    print(
        "x = " + x.__round__(3).__str__() 
        + " result = " + result_final.__round__(2).__str__()
        )
    result_curent = 0.0
    result_final = 0.0
    x += 0.05
    x = x.__round__(2)
    n = 1
