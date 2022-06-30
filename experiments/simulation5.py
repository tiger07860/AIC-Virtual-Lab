from PySpice.Unit import *
from PySpice.Spice.Netlist import Circuit
import math
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

import PySpice.Logging.Logging as Logging
def graph(R1_val=1,R2_val=1,R3_val = 9,C1_val=1):
    logger = Logging.setup_logging()
    
    
    def bode_diagram_gain(axe, frequency, gain, **kwargs):
    
        axe.semilogx(frequency, gain, base=10, **kwargs)
        axe.grid(True)
        axe.grid(True, which='minor')
        axe.set_xlabel("Frequency [Hz]")
        axe.set_ylabel("Gain [dB]")
    
    
    ####################################################################################################
    
    def bode_diagram_phase(axe, frequency, phase, **kwargs):
    
        axe.semilogx(frequency, phase, base=10, **kwargs)
        axe.set_ylim(-math.pi, math.pi)
        axe.grid(True)
        axe.grid(True, which='minor')
        axe.set_xlabel("Frequency [Hz]")
        axe.set_ylabel("Phase [rads]")
        axe.set_yticks # Fixme:
        plt.yticks((-math.pi, -math.pi/2, 0, math.pi/2, math.pi),
                   (r"$-\pi$", r"$-\frac{\pi}{2}$", "0", r"$\frac{\pi}{2}$", r"$\pi$"))
    
    
    ####################################################################################################
    
    def bode_diagram(axes, frequency, gain, phase, **kwargs):
        bode_diagram_gain(axes, frequency, gain, **kwargs)
        #bode_diagram_phase(axes[1], frequency, phase, **kwargs)
    
    
    circuit = Circuit('Low-Pass RC Filter')
    circuit.SinusoidalVoltageSource('input', 'in', circuit.gnd, amplitude=1@u_V)
    R1 = circuit.R(1, 'in', 'out', R1_val@u_kΩ)
    C1 = circuit.C(1, 'out', circuit.gnd, C1_val@u_uF)
    break_frequency = 1 / (2 * math.pi * float(R1.resistance * C1.capacitance))
    break_frequency = round(break_frequency,2)
    # print("Break frequency = {:.1f} Hz".format(break_frequency))
    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.ac(start_frequency=1@u_Hz, stop_frequency=10@u_MHz, number_of_points=10,  variation='dec')
    plt.switch_backend('agg')
    figure, axes = plt.subplots(1, figsize=(12, 4))
    plt.title("Bode Diagram of a Low-Pass Filter")
    bode_diagram(axes=axes,
                 frequency=analysis.frequency,
                 gain=20*np.log10(1+R2_val/R3_val) + 20*np.log10(np.absolute(analysis.out)),
                 phase=np.angle(analysis.out, deg=False),
                 marker='.',
                 color='blue',
                 linestyle='-',
                 )
    axes.axvline(x=break_frequency, color='red')
    
    plt.tight_layout()
    #plt.show()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data, break_frequency

