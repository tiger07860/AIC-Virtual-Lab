##*********************************************
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import markers, pyplot as plt
from io import StringIO
import os
import PySpice.Logging.Logging as Logging
from PySpice.Probe.Plot import plot
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

    ##*********************************************
    # Set the path where the op-amp uA741.lib file is located
    # Place the *.lib file in the same folder as the script file
def non_inverting(amp = 0.2,freq = 1,R1_val = 10,R2_val = 90,Load = 10,limit_op_amp = 15):
    logger = Logging.setup_logging()
    
    ## Circuit Netlist
    circuit = Circuit('Non-inverting op-amp Amplifier')
    path_opamp = os.path.join(os.getcwd(),"experiments\\uA741.lib")
    circuit.include(path_opamp)
    
    # Define amplitude and frequency of input sinusoid
    amp=amp@u_V
    freq=freq@u_kHz
    
    # Define transient simulation step time and stop time
    steptime=1@u_us
    finaltime = 5*(1/freq)
    
    source = circuit.SinusoidalVoltageSource(1, 'input', circuit.gnd, amplitude=amp, frequency = freq)
    circuit.V(2, '+Vcc', circuit.gnd,limit_op_amp@u_V)
    circuit.V(3, '-Vcc', circuit.gnd,-limit_op_amp@u_V)
    
    circuit.X(1, 'uA741', 'input', 'v-', '+Vcc', '-Vcc', 'out')
    
    circuit.R(1, 'v-', circuit.gnd,   R1_val@u_kΩ)
    circuit.R(2, 'v-', 'out',         R2_val@u_kΩ)
    circuit.R('L', 'out', circuit.gnd,Load@u_kΩ)
    
    
    ##*********************************************
    ## Simulation: Transient Analysis
    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.transient(step_time=steptime, end_time=finaltime)
    
    ##*********************************************
    ## Theory: See video Op-amp circuits - Example 1 Non-inverting op-amp Amplifier
    
    Gain = (1+ circuit.R2.resistance/circuit.R1.resistance)
    time=np.array(analysis.time)
    vout = Gain*(amp)*(np.sin(2*np.pi*freq*time))
    
    ##*********************************************
    # PLOTTING COMMANDS
    plt.switch_backend('agg')
    figure, axe = plt.subplots(figsize=(10, 6))
    
    plt.title('Non-inverting op-amp Amplifier')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.grid()
    plot(analysis['input'], axis=axe)
    #plot(analysis['out'], axis=axe)
    plt.plot(time, vout)
    plt.legend(('sim:input', 'sim:output'), loc=(.05,.1))
    #cursor = Cursor(axe, useblit=True, color='red', linewidth=1)
    plt.tight_layout()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)
    
    data = imgdata.getvalue()
    return data

def inverting(amp = 0.2,freq = 1,R1_val = 10,R2_val = 90,Load = 10,limit_op_amp = 15):
    logger = Logging.setup_logging()
    
    ## Circuit Netlist
    circuit = Circuit('Inverting op-amp Amplifier')
    path_opamp = os.path.join(os.getcwd(),"experiments\\uA741.lib")
    circuit.include(path_opamp)
    
    # Define amplitude and frequency of input sinusoid
    amp=amp@u_V
    freq=freq@u_kHz
    
    # Define transient simulation step time and stop time
    steptime=1@u_us
    finaltime = 5*(1/freq)
    
    source = circuit.SinusoidalVoltageSource(1, 'input', circuit.gnd, amplitude=amp, frequency = freq)
    circuit.V(2, '+Vcc', circuit.gnd,limit_op_amp@u_V)
    circuit.V(3, '-Vcc', circuit.gnd,-limit_op_amp@u_V)
    
    circuit.X(1, 'uA741', circuit.gnd, 'v-', '+Vcc', '-Vcc', 'out')
    
    circuit.R(1,'input' ,'v-',   R1_val@u_kΩ)
    circuit.R(2, 'v-', 'out',         R2_val@u_kΩ)
    circuit.R('L', 'out', circuit.gnd,Load@u_kΩ)
    
    
    ##*********************************************
    ## Simulation: Transient Analysis
    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.transient(step_time=steptime, end_time=finaltime)
    
    ##*********************************************
    ## Theory: See video Op-amp circuits - Example 1 Non-inverting op-amp Amplifier
    
    Gain = -(circuit.R2.resistance/circuit.R1.resistance)
    time=np.array(analysis.time)
    vout = Gain*(amp)*(np.sin(2*np.pi*freq*time))
    
    ##*********************************************
    # PLOTTING COMMANDS
    plt.switch_backend('agg')
    figure, axe = plt.subplots(figsize=(10, 6))
    
    plt.title('Inverting op-amp Amplifier')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.grid()
    plot(analysis['input'], axis=axe)
    #plot(analysis['out'], axis=axe)
    plt.plot(time, vout)
    plt.legend(('sim:input', 'sim:output'), loc=(.05,.1))
    #cursor = Cursor(axe, useblit=True, color='red', linewidth=1)
    plt.tight_layout()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)
    
    data = imgdata.getvalue()
    return data