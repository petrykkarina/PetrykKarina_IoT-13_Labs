age = 17
age_president = 35
if age < age_president:
    print('You can`t be president')
else:
   print('You can be president')


country = 'Ukraine'
print(country)


is_holiday = True
is_weekend = False
print("is_holiday and is_weekend:", is_holiday and is_weekend)
print("is_holiday or is_weekend:", is_holiday or is_weekend)
print("not is_holiday:", not is_holiday)
print("not is_weekend:", not is_weekend)


import math
from math import sqrt
from math import log

x = 1.549
y = 7.317


term1 = 3.14 * x**2
term2 = 7 * y**(-2)
term3 = x * y**3
term4 = 7 * sqrt(y)
term5 = log(x + 7 * sqrt(y))

result = term1 - term2 + term3 + term4 + term5

print(result)