### Data Types ###

import numpy as np

#integers

i = 10
print(type(i))

a_i = np.zeros(i, dtype=int) #declare an array of ints
print(type(a_i))
print(type(a_i[0]))

#floats

x = 119.0
print(type(x))

y = 1.19e2
print(type(y))

z = np.zeros(i, dtype=float)
print(type(z))
print(type(z[0]))