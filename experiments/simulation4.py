import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.integrate as integrate
from io import StringIO
from scipy import signal


def function_gen(R = 4.7,R1=20, R2 = 5,R3 = 10,R4 = 10,R5 = 10,C1=0.1, C2 = 0.1,C3 = 0.1,limit = 15):
    
    freq_tri = R2/(4*R3*C2*R1)
    freq_sin = R2/(4*R4*C3*R1)
    freq_sq = 1/(2*R*C1*math.pi*math.log((2*R1 + R2)/R2))
    
    R1 = R1*1000
    R2 = R2*1000
    R3 = R3*1000
    R4 = R4*1000
    R5 = R5*1000
    C1 = C1*1e-6
    C2 = C2*1e-6
    C3 = C3*1e-6
    
    X_sq = np.linspace(0, 5*(1/freq_sq),200)
    X_tri = np.linspace(0, 5*(1/freq_tri),200)
    X_sin = np.linspace(0, 5*(1/freq_sin),200)
    sin_ = np.sin(2*np.pi*freq_sin*X_sin)
    square_ = signal.square(2*np.pi*freq_sq*X_sq)
    tri_ = signal.sawtooth(2*np.pi*freq_tri*X_tri,0.5)
    
    square_ = -limit*square_
    tri_ = (R1*limit/R2)*tri_
    sin_ = (R1*limit/R2)*sin_
    
    plt.switch_backend('agg')
    figure, axes = plt.subplots(3, figsize=(12, 8))
        
    plt.subplot(3, 1, 1)
    plt.plot(X_sq, square_)
    plt.grid()
    plt.title('Square Wave')
    
    plt.subplot(3, 1, 2)
    plt.plot(X_tri, tri_)
    plt.grid()
    plt.title("Trialngular Wave")

    plt.subplot(3, 1, 3)
    plt.plot(X_sin, sin_)
    plt.grid()
    plt.title('Sin Wave')
    
    plt.tight_layout()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


