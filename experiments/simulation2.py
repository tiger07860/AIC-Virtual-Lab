import matplotlib.pyplot as plt
import numpy as np
import math
from io import StringIO
from scipy import signal


def result(Rf = 10,R = (10,10,10),A =(1,1,1),freq = (1,1,1),type = ('sin','sin','sin')):
    
    def sin_(freq,X):
        return np.sin(2*np.pi*freq*X)
    
    def square_(freq,X):
        return signal.square(2*np.pi*freq*X)
    
    R1,R2,R3 = R
    A1,A2,A3 = A
    freq1,freq2,freq3 = freq
    t1,t2,t3 = type
    R1 = R1*1000
    R2 = R2*1000
    R3 = R3*1000
    Rf = Rf*1000
    
    X = np.linspace(0, 5*(1/max(freq1,freq2,freq3)),200)
    
    X1 = np.linspace(0, 5*(1/freq1),200)
    X2 = np.linspace(0, 5*(1/freq2),200)
    X3 = np.linspace(0, 5*(1/freq3),200)
    
    if t1 == 'sin':
        S1 = A1*sin_(freq1,X)
        S1_ = A1*sin_(freq1,X1)
    else :
        S1 = A1*square_(freq1,X)
        S1_ = A1*square_(freq1,X1)
    if t2 == 'sin':
        S2 = A2*sin_(freq2,X)
        S2_ = A2*sin_(freq2,X2)
    else :
        S2 = A2*square_(freq2,X)
        S2_ = A2*square_(freq2,X2)
    if t3 == 'sin':
        S3 = A3*sin_(freq3,X)
        S3_ = A3*sin_(freq3,X3)
    else :
        S3 = A3*square_(freq3,X)
        S3_ = A3*square_(freq3,X3)
    
    Y = - Rf*(S1/R1 + S2/R2 + S3/R3)
    
    plt.switch_backend('agg')
    figure, axes = plt.subplots(4, figsize=(12, 8))
        
    plt.subplot(4, 1, 1)
    plt.plot(X1,S1_)
    plt.grid()
    plt.title('Signal 1')
    
    plt.subplot(4, 1, 2)
    plt.plot(X2,S2_)
    plt.grid()
    plt.title('Signal 2')
    
    plt.subplot(4, 1, 3)
    plt.plot(X3,S3_)
    plt.grid()
    plt.title('Signal 3')
    
    plt.subplot(4, 1, 4)
    plt.plot(X,Y)
    plt.grid()
    plt.title('Output Wave')
    
    plt.tight_layout()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


