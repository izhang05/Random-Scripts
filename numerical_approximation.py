from tabulate import tabulate
from matplotlib import pyplot as plt
from math import sqrt, log
import numpy as np


def f(x, y):
    return 50 / (5 - x * x)


def y(x, y_0):
    return -5 * sqrt(5) * (log(sqrt(5) - x) - log(x + sqrt(5))) + y_0


def euler(a, y_a, b, steps, log=True):
    if log:
        print("Euler:")
    data = [["x", "y", "slope", "next-y"]]
    size = float(b) / steps
    res = float(y_a)
    x = float(a)
    for i in range(steps):
        data.append([round(j, 6) for j in [x, res, f(x, res), res + f(x, res) * size]])
        res += f(x, res) * size
        x += size
    if log:
        print(tabulate(data))
    return res


def heun(a, y_a, b, steps, log=True):
    if log:
        print("Heun:")
    data = [["x", "y", "euler-slope", "euler_y", "slope", "next-y"]]
    size = float(b) / steps
    res = y_a
    x = a
    for i in range(steps):
        euler_y = res + size * f(x, res)
        data.append([round(j, 6) for j in [x, res, f(x, res), euler_y, (f(x, res) + f(x + size, euler_y)) / 2,
                                           res + size * (f(x, res) + f(x + size, euler_y)) / 2]])
        res += size * (f(x, res) + f(x + size, euler_y)) / 2
        x += size
    if log:
        print(tabulate(data))
    return res


def main(a, y_a, b, steps):
    print("Using starting value of y({}) = {} and {} steps of size {}.".format(a, y_a, steps, float(b) / steps))
    print(euler(a, y_a, b, steps))
    print()
    print(heun(a, y_a, b, steps))
    print("Actual:", y(b, y_a))
    plt.title("Euler and Heun estimations vs Step Size")
    plt.xlabel("Step size")
    plt.ylabel("y(1)")
    x = []
    euler_data = []
    heun_data = []
    for s in range(1, 3000):
        size = float(b) / s
        x.append(size)
        euler_data.append(euler(a, y_a, b, s, False))
        heun_data.append(heun(a, y_a, b, s, False))
    plt.plot(x, euler_data, 'bo', label="Euler")
    plt.plot(x, heun_data, 'ro', label="Heun")
    plt.plot(np.linspace(0, 1, 10000), [y(b, y_a) for _ in range(10000)], label="Actual")
    plt.legend()
    plt.savefig("approximation_project.png")
    plt.show()
    plt.close()


if __name__ == "__main__":
    main(0, 6, 1, 4)
