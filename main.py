from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

def composite_simpson(a, b, n, func):
    if n % 2 != 0:
        n += 1
    h =  float(b - a) / n
    t=T(n)
    sum=func(a)+4*func(a+h)+func(b)
    for i in range(1, n // 2):
        sum += 2 * func(t[i]) + 4 * func(t[i])
    sum=sum * h / 3
    return sum

def f(t):
    g = 9.8
    a = 1e-7
    b = 1.75418438
    C = 1.03439984
    return 1 / np.sqrt(2 * g) * np.sqrt((2 + 2 *\
(np.sin(2 * t) / (1 - np.cos(2 * t))) ** 2) / (C * (1 - np.cos(2 * t)))) * C * (1 - np.cos(2 * t))

def T(n):
    a = 1e-7
    t=[]
    for i in range(1,n+2):
        t.append(a+(i+1))
    return t

def composite_trapezoid(a, b, n, func):
    h =  (b - a) / n
    t = T(n)
    sum = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        sum += func(a + t[i] * h)
    return sum * h

if __name__ == '__main__':
    g = 9.8
    a = 1e-7
    C = 1.03439984
    b = 1.75418438
    val=np.sqrt(2*C/g)*(b-a)
    ax = plt.subplot()
    for i in range(3,9999,100):
        h = (b-a)/i
        ax.scatter(h,abs(val-composite_simpson(a,b,i,f)),color='red')
        ax.scatter(h,abs(val-composite_trapezoid(a, b, i, f)),color='blue')
    ax.scatter(h, abs(val - composite_simpson(a, b, i, f)), color='red',label='composite_simpson')
    ax.scatter(h, abs(val - composite_trapezoid(a, b, i, f)), color='blue', label='composite_trapezoid')
    h_ = np.logspace(-4, 0, 10000)
    plt.loglog(h_, 10**(-4)*h_ , 'k-', label='O (h)')
    plt.grid()
    plt.loglog()
    ax.legend()
    plt.show()

