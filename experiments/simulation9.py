# https://github.com/JeffJetton/555-timer-sim/blob/master/astable.py

import math     # Just to get Euler's constant
import matplotlib.pyplot as plt
from io import StringIO

####  Constants  ###############################################################
def graph(vin = 5,farads = 10,ohms_a = 10,ohms_b=10,sim_time = 1):
    vin = vin           # Voltage in
    
    out_high = 2*vin/3     # Voltage output from pin 3 when "high" 
    out_low  = 0.25     # Voltage output from pin 3 when "low"
                        # (These are not simply vin and zero. See datasheet.)
    
    farads = farads/1000000  # Capacitance of primary capacitor, which connects both the
                        # threshold (pin 6) and trigger (pin 2) to ground.
                        
    ohms_a = ohms_a*1000       # Resistance in ohms of resistor A, which connects the
                        # discharge (pin 7) and resistor B to positive voltage.
                        # The primary capacitor charges through this resistor,
                        # but does not discharge through it.
                        
    ohms_b = ohms_b*1000     # Resistance in ohms of resistor B, which both discharges
                        # the capacitor through pin 7 and charges it from the end
                        # of resistor A. Connects to the threshold (pin 6), trigger
                        # (pin 2) and the primary capacitor.
    
    sim_time = sim_time        # Length of time to run the simulation (in seconds)
    
    step = sim_time / 1000  # Time increment for each simulation step (in seconds)
    
    
    
    ####  Utility functions   ######################################################
    
    def update_latch(latch, trigger, threshold, vin):
        """
        Return a boolean representing the state of the internal SR latch, based on
        trigger and threshold voltages, as they compare to the input voltage.
        """
        # Latch is "set" if the trigger voltage is less than 1/3 vin
        # (But not necessarily "unset" if it's not!)
        if trigger < vin / 3:
            latch = True
        
        # Latch is "unset" if the threshold voltage is above 2/3 vin
        # (But not necessarily "set" if it's not!)
        if threshold > vin * 2 / 3:
            latch = False
            
        # For voltages between these, the latch stays at whatever it was
        return latch
        
    
    
    def update_capacitor(cap, farads, res_a, res_b, vin, latch, step):
        """
        Either charges or discharges (depending on latch state) the capacitor 
        based on resistors A & B and vin, over time period 'step'. The percentage
        of change, either way, is based on (1 - 1/e**(t/tc)). That is:
        
            1. Calculate the time constant (capacitance times total resistance)
            2. Figure out the proportion of the time constant that has passed
            3. Raise e to that proportion
            4. Take the inverse of that result
            5. Subtract that from one
        
        Returns the resulting capacitor voltage
        """
        if latch:
            # Charging...
            # Time constant is based on charging through both resistors
            tc = farads * (res_a + res_b)
            # Time proportion
            tp = step / tc
            # Percent change from existing voltage to full voltage (vin)
            pc = 1 - (1/math.e**tp)
            cap += (vin - cap) * pc
        else:
            # Discharging...
            # Calculate time constant based on going through resistor B only
            tc = farads * res_b
            # Time proportion
            tp = step / tc
            # Percent change from existing voltage down to zero
            pc = 1 - (1/math.e**tp)
            cap -= cap * pc
    
        return cap
    
    
    
    ####  Set up  ##################################################################
    
    # At time zero, assume capacitor is not charged and therefore the latch
    # is "on" (since the Trigger voltage will be less than 1/3 vin).
    time = 0
    cap = 0
    latch = True
    vout = out_high
    
    # Vectors to store simulated states
    cap_list = []
    out_list = []
    time_list = []
    
    
    ####  Simulate  ################################################################
    
    while time < sim_time:
        cap = update_capacitor(cap, farads, ohms_a, ohms_b, vin, latch, step)
        latch = update_latch(latch, cap, cap, vin)
        if latch:
            vout = out_high
        else:
            vout = out_low
        cap_list.append(cap)
        out_list.append(vout)
        time_list.append(time)
        time += step
        
    
    ####  Print Stats  #############################################################
    
    # Print constants
    print()
    print('Capacitor: ' + str(farads * 1000000) + 'mf')
    print('Resistor A: ' + str(ohms_a/1000) + 'K')
    print('Resistor B: ' + str(ohms_b/1000) + 'K')
    print('Vcc: +' + str(vin) + 'V')
    print()
    
    # Print out duty cycle info
    time_high = 0.693 * (ohms_a + ohms_b) * farads
    time_low = 0.693 * ohms_b  * farads
    time_total = time_high + time_low
    print('Time high: ' + str(time_high*1000) + 'ms')
    print('Time low: ' + str(time_low*1000) + 'ms')
    print('Total period: ' + str(time_total*1000) + 'ms')
    print('Duty cycle: ' + str(round(time_high/time_total*100, 2)) + '%')
    duty_cycle = round(time_high/time_total*100, 2)
    print('Frequency: ' + str(round(1/time_total, 2)) + 'Hz')
    print('Periods simulated: ' + str(len(time_list)))
    print()
    
    
    ####  Plot  ####################################################################
    plt.switch_backend('agg')
    figure, axes = plt.subplots(1, figsize=(12, 5))
    # Capacitor voltages
    plt.plot(time_list, cap_list, label='Capacitor')
    # Output (Q) voltages
    plt.plot(time_list, out_list, label='Output')
    plt.xlabel('Time (Seconds)')
    plt.ylabel('Volts')
    plt.ylim(0, vin)
    plt.legend(loc='upper right')
    plt.grid()
    #plt.show()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data, time_high, time_low, duty_cycle

    