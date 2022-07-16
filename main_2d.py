import matplotlib.pyplot as plt
import math
import numpy as np

o = [0,0]
a = [7,0]
b = [3.50000,6.06218]
a2 = [1,0]
b2 = [1.3,2]

def calc_2d(a,b):
    ab_star = (2* math.pi)/(a[0] * b[1] - a[1] * b[0]) * np.array([[b[1],-a[1]],[-b[0],a[0]]])
    a_star = ab_star[0,:]
    b_star = ab_star[1,:]
    return a_star, b_star


def draw_cell(a, b, color,name):
    x_all = np.zeros(10000)
    y_all = np.zeros(10000)
    i = 0
    for x in range(-40,40):
        for y in range(-40,40):
            x_all[i]=a[0]*x+b[0]*y
            y_all[i]=a[1]*x+b[1]*y
            i += 1
            
    plt.scatter(x_all, y_all, color=color, s=30)
    plt.scatter(0,0, color=color,label=name, s=50)
    plt.scatter(a[0]+b[0],a[1]+b[1], color=color, s=50)
    plt.scatter(a[0],a[1], color=color, s=50)
    plt.scatter(b[0],b[1], color=color, s=50)
    plt.plot([0,a[0],a[0]+b[0],b[0],0], [0,a[1],a[1]+b[1],b[1],0], color=color)
    return


def draw_2d(a,b,a_star,b_star):
    fig = plt.figure(figsize=(10, 10))
    plt.title("2D real space lattice and reciprocal space lattice")
    plt.gca().set_aspect('equal', adjustable='datalim')
    plt.grid()
    draw_cell(a,b,"teal","real")
    draw_cell(a_star,b_star,"orange","reciprocal")
    plt.xlim(-12,12)
    plt.ylim(-12,12)
    plt.legend()
    plt.draw()
    plt.show()
    return


a_star, b_star = calc_2d(a,b)

print("Real lattice vectors:\n a = ", a, "\n b = ", b)
print("Reciprocal lattice vectors:\n a* = ", a_star, "\n b* = ", b_star)

draw_2d(a,b,a_star,b_star)
