import numpy as np
import matplotlib.pyplot as plt

def circle_points(n):
    circles = []
    for n in n:
        t = np.linspace(0, 2*np.pi, n, endpoint=False)
        x = 1 * np.cos(t)
        y = 1 * np.sin(t)
        circles.append(np.c_[x, y])
    return circles
def area_aprox_1(n):
    areas = []
    for n in n:
        angle = 2*np.pi/n
        b = np.sin(angle/2)
        h = np.cos(angle/2)
        area = 2*n * 0.5*b*h
        areas.append(area)
    return areas

n = [4, 10, 20, 40, 100]
circles = circle_points(n)
areas1 = area_aprox_1(n)

top = ''
label = 'N  | Area'
print(top.center(25,'-'))
print(label.center(25, ' '))
print(top.center(25,'-'))
for i in range(len(n)):
    print("     {0:3d}     {1:2f}".format(n[i], areas1[i]))



print(areas1)

fig, ax = plt.subplots(3,2)
circle1 = plt.Circle((0, 0), 1, color='b', fill=False)
ax[0,0].add_patch(circle1)
ax[0,0].scatter(circles[0][:, 0], circles[0][:, 1], s = 20)
ax[0,0].set_aspect('equal')

circle3 = plt.Circle((0, 0), 1, color='b', fill=False)
ax[0,1].add_patch(circle3)
ax[0,1].scatter(circles[1][:, 0], circles[1][:, 1], s = 20)
ax[0,1].set_aspect('equal')

circle4 = plt.Circle((0, 0), 1, color='b', fill=False)
ax[1,0].add_patch(circle4)
ax[1,0].scatter(circles[2][:, 0], circles[2][:, 1], s = 20)
ax[1,0].set_aspect('equal')

circle5 = plt.Circle((0, 0), 1, color='b', fill=False)
ax[1,1].add_patch(circle5)
ax[1,1].scatter(circles[3][:, 0], circles[3][:, 1], s = 20)
ax[1,1].set_aspect('equal')

circle6 = plt.Circle((0, 0), 1, color='b', fill=False)
ax[2,0].add_patch(circle6)
ax[2,0].scatter(circles[4][:, 0], circles[4][:, 1], s = 20)
ax[2,0].set_aspect('equal')

circle2 = plt.Circle((0.5, 0.5), 0.5, color='b', fill=False)
ax[2,1].add_patch(circle2)
ax[2,1].set_aspect('equal')
plt.show()