import numpy as np

x = 0.85
y = 2

z = np.diag([x, x*y, x/y])
print(z)

p = []
for i in range(2,38,5):
    p.append(i)    
x = np.array(p)
for i,j in enumerate(x):
    x[i] = j*j
z = np.sum(x)
print(z)


