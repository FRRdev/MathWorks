import matplotlib.pyplot as plt
import numpy as np
from decimal import getcontext, Decimal

getcontext().prec = 5  # setting decimal allowance

t = np.linspace(0, 1000.0, 100000)  # timestep vector with timestep t[1] - t[0]

I = [np.array([0.1223, 0.114, 0.01, 0.0]), \
     np.array([0.408248, 0.0, 0.3325, 0.0]), \
     np.array([0.1, 0.02, 0.408248, 0.232]), \
     np.array([0.3, 0.1, 0.22, 0.4])]  # array of various inital vectors


def m(vpair, tpair):  # defining heinon heiles eqations  of motion

    (x, y, px, py) = tuple(vpair)  # forms iterable item from array vpair

    return np.array([px, py, -(x) - 2 * (x) * (y), -(y) - ((x) ** 2 - (y) ** 2)]).T


def rk4(f, t, y0): #definig runge kutta function for multiple coupled equations with initial conditions
    N = len(t)

    y = np.array([k * np.ones(N) for k in y0]).T # N by step length(v0) array to store iterations

    for ii in range(N - 1):
        h = t[ii + 1] - t[ii]
        k1 = h * f(y[ii], t[ii])
        k2 = h * f(y[ii] + 0.5 * k1, t[ii] + 0.5 * h)
        k3 = h * f(y[ii] + 0.5 * k2, t[ii] + 0.5 * h)
        k4 = h * f(y[ii] + k3, t[ii + 1])
        y[ii + 1] = y[ii] + (k1 + 2.0 * (k2 + k3) + k4) / 6.0

    return y


def zeros(vec): # generate array for which has entries corresponding to zero positions in a vector
    #             we will use this to find the poincare plot of system
    p = list()
    for ii in range(len(vec) - 1):
        if (vec[ii] > 0) & (vec[ii + 1] < 0):
            p.append(ii)
        if (vec[ii] < 0) & (vec[ii + 1] > 0):
            p.append(ii)
    return np.array(p)


fin = list() # list to store data for final rk approximations
for k in I: # running thr above functions to form runge kutta data set with the defined initial conditions
    fin.append(rk4(m,t,k))

fig2 = plt.figure(2) # creates figure to plot the poincare section for x = 0
for ii in range(4):
    plt.subplot(2,2,ii+1)
    xzeros = zeros(fin[ii][:,0])
    yints = [.5*(fin[ii][k,1] + fin[ii][k+1,1]) for k in xzeros]
    pyints = [.5*(fin[ii][k,3] + fin[ii][k+1,3]) for k in xzeros]
    plt.plot(yints,pyints,'r.')
    plt.ylabel("py")
    plt.xlabel("y")

plt.show()



