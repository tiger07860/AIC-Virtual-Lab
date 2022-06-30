from math import ceil
import matplotlib.pyplot as plt
from matplotlib import markers, pyplot as plt
from io import StringIO
import os
import PySpice.Logging.Logging as Logging
from PySpice.Probe.Plot import plot
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *



def schmit(amp = 0.2,freq = 1,R1_val = 10,R2_val = 1,limit_op_amp = 10):
    logger = Logging.setup_logging()
    
    ## Circuit Netlist
    circuit = Circuit('Inverting Schmitt Trigger')
    path_opamp = os.path.join(os.getcwd(),"experiments\\uA741.lib")
    circuit.include(path_opamp)
    
    # Define transient simulation step time and stop time
    steptime=1@u_us
    freq = freq@u_kHz
    finaltime = 5*(1/freq)
    
    source = circuit.SinusoidalVoltageSource(1, 'input', circuit.gnd, amplitude=amp@u_V, frequency = freq)
    circuit.V(2, '+Vcc', circuit.gnd,limit_op_amp@u_V)
    circuit.V(3, '-Vcc', circuit.gnd,-limit_op_amp@u_V)
    
    circuit.X(1, 'uA741', circuit.gnd, 'v-', '+Vcc', '-Vcc', 'out')
    val_R_par = ceil(R1_val*R2_val/(R1_val + R2_val))
    circuit.R(1,'input' ,'v-',   val_R_par@u_kΩ)
    circuit.R(2, circuit.gnd,'v+',    R1_val@u_kΩ)
    circuit.R(3, 'v+', 'out',    R2_val@u_kΩ)
    
    threshold = round(limit_op_amp*(R1_val/(R1_val + R2_val )),2)
    
    ##*********************************************
    ## Simulation: Transient Analysis
    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.transient(step_time=steptime, end_time=finaltime)
    
    # PLOTTING COMMANDS
    plt.switch_backend('agg')
    figure, axe = plt.subplots(figsize=(10, 6))
    
    plt.title('Schmitt Trigger')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.grid()
    plot(analysis['input'], axis=axe)
    plot(analysis['out'], axis=axe)
    #plt.axhline(y = threshold,color = 'g',linestyle = ':',label = 'V (ut)')
    #plt.axhline(y = -threshold,color = 'g',linestyle = ':',label = 'V (lt)')
    plt.legend(('sim:input', 'sim:output'), loc=(.05,.1))
    plt.tight_layout()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)
    
    data = imgdata.getvalue()
    return data,threshold,-threshold,2*threshold