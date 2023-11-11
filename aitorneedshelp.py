import matplotlib.pyplot as plt
import numpy as np

axis_y = [0,1]
axis_y_true = []

for i in range(2,30):
    axis_y.append(axis_y[i-1] + axis_y[i-2])

x = np.array(axis_y)
x = np.log(x)
x = np.reshape(x, (30,-1))
print(x.shape)
print(axis_y)  
print(x)  
plt.plot(axis_y, x, marker = 'o')
plt.show()

# def generate_fibonacci(n):
#     fibonacci_sequence = [0, 1]
#     for i in range(2, n):
#         fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
#     return np.array(fibonacci_sequence)

# n = 30
# fibonacci_numbers = generate_fibonacci(n)

# x = np.arange(1, n + 1)

# ln_x_values = np.log(x)

# plt.plot(x, ln_x_values, marker='o', linestyle='-', label='ln(x)')
# plt.xlabel('Fibonacci Numbers')
# plt.ylabel('ln(x)')
# plt.title('Natural Logarithm Plot of Fibonacci Numbers')
# plt.legend()
# plt.show()