import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from scipy.misc import derivative
from io import StringIO
from scipy import signal


def integration_sin(R=1, C=2, freq=1):
    def sin_integral(x):
        return np.sin(2*np.pi*freq*x)
    R = R*1000
    C = C*1e-6
    X = np.arange(0, 5*(1/freq), 0.005)
    sin_ = np.sin(2*np.pi*freq*X)

    DF = [integrate.quad(sin_integral, a, b)[0] for a, b in zip(X[:-1], X[1:])]
    F = np.cumsum(DF)
    F = F - F.max()/2
    F = -F/(R*C)
    plt.switch_backend('agg')
    figure, axes = plt.subplots(2, figsize=(12, 5))
    plt.subplot(2, 1, 1)
    plt.plot(X, sin_)
    plt.grid()
    plt.title("Sin Wave")
    plt.subplot(2, 1, 2)
    plt.plot(X[1:], F)
    plt.grid()
    plt.title("Integrator Output")

    plt.tight_layout()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def integration_pulse(R=1, C=2, freq=1):

    def square_integral(x):
        return signal.square(2*np.pi*freq*x)

    R = R*1000
    C = C*1e-6
    X = np.arange(0, 5*(1/freq), 0.005)
    square_ = signal.square(2*np.pi*freq*X)
    DF = [integrate.quad(square_integral, a, b)[0]
          for a, b in zip(X[:-1], X[1:])]
    F = np.cumsum(DF)
    F = F - F.max()/2
    F = -F/(R*C)

    plt.switch_backend('agg')
    figure, axes = plt.subplots(2, figsize=(12, 5))

    plt.subplot(2, 1, 1)
    plt.plot(X, square_)
    plt.grid()
    plt.title('Square Wave')
    plt.subplot(2, 1, 2)
    plt.plot(X[1:], F)
    plt.grid()
    plt.title("Integrator Output")

    plt.tight_layout()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def diff_sin(R=1, C=2, freq=1):
    def function(x):
        return np.sin(2*np.pi*freq*x)

    def sin_diff(x):
        return derivative(function, x, dx=1e-3)
    R = R*1000
    C = C*1e-6
    X = np.arange(0, 5*(1/freq), 0.005)
    sin_ = np.sin(2*np.pi*freq*X)

    plt.switch_backend('agg')
    figure, axes = plt.subplots(2, figsize=(12, 5))
    plt.subplot(2, 1, 1)
    plt.plot(X, sin_)
    plt.grid()
    plt.title("Sin Wave")
    plt.subplot(2, 1, 2)
    plt.plot(X, -R*C*sin_diff(X))
    plt.grid()
    plt.title("Differentiator Output")

    plt.tight_layout()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def diff_pulse(R=1, C=2, freq=1):
    def function(x):
        return signal.square(2*np.pi*freq*x)

    def square_diff(x):
        return derivative(function, x, dx=1e-3)
    R = R*1000
    C = C*1e-6
    X = np.arange(0, 5*(1/freq), 0.005)
    square_ = signal.square(2*np.pi*freq*X)

    plt.switch_backend('agg')
    figure, axes = plt.subplots(2, figsize=(12, 5))
    plt.subplot(2, 1, 1)
    plt.plot(X, square_)
    plt.grid()
    plt.title("Square Wave")
    plt.subplot(2, 1, 2)
    plt.plot(X, -R*C*square_diff(X))
    plt.grid()
    plt.title("Differentiator Output")

    plt.tight_layout()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
