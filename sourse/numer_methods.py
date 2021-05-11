import math
import matplotlib.pyplot as plt


def yy(x, y):
    '''Function initialization'''
    return (x ** y) * math.cos(y)


def Runge4(x0, xn, h, y0):
    '''Fourth-order Runge-Kutta method'''
    X, Y = [], []
    X.append(x0)
    Y.append(y0)
    print("y0=", y0, '\t', "x0=", x0)
    x = x0
    i = 0
    while (x < xn - h):
        k1 = h * yy(X[i], Y[i])
        k2 = h * yy(X[i] + 0.5 * h, Y[i] + 0.5 * k1)
        k3 = h * yy(X[i] + 0.5 * h, Y[i] + 0.5 * k2)
        k4 = h * yy(X[i] + h, Y[i] + k3)
        Yi = Y[i] + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        Y.append(Yi)
        x += h
        X.append(x)
        print('y{0}={1}\tx{2}={3}'.format(i + 1, Y[i + 1], i + 1, round(X[i + 1], 2)))
        i += 1
    plt.plot(X, Y, color="black")
    plt.title("Fourth-order Runge-Kutta method")
    plt.grid(True)
    plt.show()


def Adams3(x0, xn, h, y0):
    '''Third-order Adams method'''
    X, Y = [], []
    X.append(x0)
    Y.append(y0)
    print("y0=", y0, '\t', "x0=", x0)
    x = x0 + 2 * h
    i = 2
    Y.append(Y[0] + h * yy(X[0], Y[0]))
    X.append(x0 + h)
    Y.append(Y[1] + h * yy(X[1], Y[1]))
    X.append(x0 + 2 * h)
    print("y1=", Y[1], "x1=", X[1])
    print("y2=", Y[2], "x1=", X[2])
    while (x < xn - h):
        x += h
        X.append(x)
        Yi = Y[i] + (h / 12) * (23 * yy(X[i], Y[i]) - 16 * yy(X[i - 1], Y[i - 1]) + 5 * yy(X[i - 2], Y[i - 2]))
        Y.append(Yi)
        print('y{0}={1}\tx{2}={3}'.format(i + 1, Y[i + 1], i + 1, round(X[i + 1], 2)))
        i += 1
    plt.plot(X, Y, color="yellow")
    plt.title("Third-order Adams method")
    plt.grid(True)
    plt.show()


def Adams4(x0, xn, h, y0):
    '''Fourth-order Adams method'''
    X, Y = [], []
    X.append(x0)
    Y.append(y0)
    print("y0=", y0, '\t', "x0=", x0)
    x = x0 + 3 * h
    i = 3
    Y.append(Y[0] + h * yy(X[0], Y[0]))
    X.append(x0 + h)
    Y.append(Y[1] + h * yy(X[1], Y[1]))
    X.append(x0 + 2 * h)
    Y.append(Y[2] + h * yy(X[2], Y[2]))
    X.append(x0 + 3 * h)
    print("y1=", Y[1], "x1=", X[1])
    print("y2=", Y[2], "x1=", X[2])
    print("y3=", Y[3], "x1=", X[3])
    while (x < xn - h):
        x += h
        X.append(x)
        Yi = Y[i] + (h / 24) * ( 55 * yy(X[i], Y[i]) - 59 * yy(X[i - 1],\
                    Y[i - 1]) + 37 * yy(X[i - 2], Y[i - 2]) - 9 * yy(X[i - 3], Y[i - 3]))
        Y.append(Yi)
        print('y{0}={1}\tx{2}={3}'.format(i + 1, Y[i + 1], i + 1, round(X[i + 1], 2)))
        i += 1
    plt.plot(X, Y, color="green")
    plt.title("Fourth-order Adams method")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    x0 = float(input("Enter value x0:"))
    xn = float(input("Enter value x n:"))
    h = float(input("enter step h:"))
    y0 = float(input("Enter value y0:"))
    Runge4(x0, xn, h, y0)
    Adams3(x0, xn, h, y0)
    Adams4(x0, xn, h, y0)
