import matplotlib.pyplot as plt
import math
import numpy as np

o = np.array([0,0,0])
a = np.array([3,1,0])
b = np.array([0,2,0])
c = np.array([0,-1,2])

def calc_3d(a,b,c):
    V = a.dot(np.cross(b,c))
    a_star, b_star, c_star = np.array([0,0,0])
    a_star = 2 * math.pi * ((np.cross(b,c))/V)
    b_star = 2 * math.pi * ((np.cross(c,a))/V)
    c_star = 2 * math.pi * ((np.cross(a,b))/V)
    return a_star, b_star, c_star


def draw_cell(a, b, c, color,name):
    l_up = 0
    l_down = 5
    x_all = np.zeros(3*(abs(l_up)+abs(l_down)+1)**3)
    y_all = np.zeros(3*(abs(l_up)+abs(l_down)+1)**3)
    z_all = np.zeros(3*(abs(l_up)+abs(l_down)+1)**3)
    i = 0
    for x in range(-2,2):
        for y in range(-2,2):
            for z in range(-2,2):
                x_all[i]=a[0]*x+b[0]*y+c[0]*z
                y_all[i]=a[1]*x+b[1]*y+c[1]*z
                z_all[i]=a[2]*x+b[2]*y+c[2]*z
                i += 3
                
    ax.scatter(x_all, y_all, z_all, color=color, s=30)
    ax.scatter(o[0], o[1], o[2], color=color,label=name, s=50)
    ax.scatter(a[0], a[1], a[2], color=color, s=50)
    ax.scatter(b[0], b[1], b[2], color=color, s=50)
    ax.scatter(c[0], c[1], c[2], color=color, s=50)
    ax.scatter(a[0]+b[0], a[1]+b[1], a[2]+b[2], color=color, s=50)
    ax.scatter(a[0]+c[0], a[1]+c[1], a[2]+c[2], color=color, s=50)
    ax.scatter(b[0]+c[0], b[1]+c[1], b[2]+c[2], color=color, s=50)
    ax.scatter(a[0]+b[0]+c[0], a[1]+b[1]+c[1], a[2]+b[2]+c[2], color=color, s=50)
    x = np.array([o[0],a[0],a[0]+b[0],b[0],o[0],c[0],c[0]+a[0],a[0],c[0]+a[0],c[0]+a[0]+b[0],a[0]+b[0],c[0]+a[0]+b[0],b[0]+c[0],b[0],b[0]+c[0],c[0]])
    y = np.array([o[1],a[1],a[1]+b[1],b[1],o[1],c[1],c[1]+a[1],a[1],c[1]+a[1],c[1]+a[1]+b[1],a[1]+b[1],c[1]+a[1]+b[1],b[1]+c[1],b[1],b[1]+c[1],c[1]])
    z = np.array([o[2],a[2],a[2]+b[2],b[2],o[2],c[2],c[2]+a[2],a[2],c[2]+a[2],c[2]+a[2]+b[2],a[2]+b[2],c[2]+a[2]+b[2],b[2]+c[2],b[2],b[2]+c[2],c[2]])
    ax.plot(x,y,z, color=color)
    return


def draw_3d(a,b,c,a_star,b_star,c_star):
    global ax, fig
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')
    plt.title("3D real space lattice and reciprocal space lattice")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    #plt.gca().set_aspect('equal', adjustable='datalim')
    ax.grid()
    draw_cell(a,b, c, "teal","real")
    draw_cell(a_star, b_star, c_star, "orange","reciprocal")
    #ax.set_xlim3d(-12,12)
    #ax.set_ylim3d(-12,12)
    #ax.set_zlim3d(-12,12)
    ax.legend()
    #plt.draw()
    plt.show()
    return


a_star, b_star, c_star = calc_3d(a, b, c)

print("Real lattice vectors:\n a = ", a, "\n b = ", b, "\n c = ", c)
print("Reciprocal lattice vectors:\n a* = ", a_star, "\n b* = ", b_star, "\n c* = ", c_star)

draw_3d(a,b,c,a_star,b_star, c_star)
