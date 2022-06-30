from distutils.log import error
from operator import inv
from django.shortcuts import render
import matplotlib.pyplot as plt
from io import StringIO

import experiments.simulation1 as S1
import experiments.simulation2 as S2
import experiments.simulation3 as S3
import experiments.simulation4 as S4
import experiments.simulation5 as S5
import experiments.simulation6 as S6
import experiments.simulation8 as S8
import experiments.simulation7 as S7
import experiments.simulation9 as S9

import experiments.validators as Verify

experiments_list = [
    {
        'id': '1',
        'name': 'To experimentally study the performance of Invertingand Non-inverting amplifier using op-amps',
        'theory_list': [
            {
                'texts': [
                    'An inverting amplifirer using op-amp is a type of amplifier where the output waveform is phase opposite to the input waveform. The input waveform will be amplified by the factor Av in magnitude and its phase will be inverted. In the inverting amplifier circuit, the signal to be amplified is applied to the inverting input of the op-amp through the input resistance R1. Rf is the feedback resistance. Rf and RI together determine the gain of the amplifier. Inverting operational amplifier can be expressed using the equation',
                    'Av = -( Rf / R1) ',
                    'Negative sign implies that the output signal is negated. The circuit diagram of a basic inverting amplifier using op-amp is shown below.'
                ],
                'images':[
                    'experiments/images/inverting_amplifier_ckt.png',
                    'experiments/images/non_inverting_amplifier_waveform.png'
                ],
            },
            {
                'texts': [
                    'Non-Inverting Amplifier: - A non-inverting amplifier is a special case of the differential amplifier in which inverting input V1 is grounded and non-inverting input V2 is connected to Vin.',
                    'Vout = (1+Rf/R1) Vin',
                    'Feedback of control of the non-inverting amplifier is achieved by applying a small part of the output voltage signal back to the inverting output terminal through a Rf voltage divider network again producing negative feedback. This closed loop configuration produce a non-inverting amplifier circuit with a very good stability.',
                ],
                'images':[
                    'experiments/images/non_inverting_amplifier_ckt.png',
                    'experiments/images/non_inverting_amplifier_waveform.png'
                ],
                'simulation': '1'
            }
        ],
        # 'procedure': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap floato electronic typesetting, remaining essentially unchanged",
        #     "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy"
        # ],
        # 'summary': [
        #     'Inverting amplifier amplifies the input signal but the output signal phase get inverted by 180o And the Non – Inverting amplifier amplifies the input signal but the phase of the output signal remains in phase',
        #     'Hence,',
        #     'The Gain of the Inverting Amplifier is given by:',
        #     'Ad = - ( Rf  /  R1) ',
        #     'The Gain of the Non - Inverting Amplifier is given by:',
        #     'Ad =  (1 + ( Rf  /  R1 ) )'
        # ]
    },
    {
        'id': '2',
        'name': 'To experimentally verify the performance of an OP-AMP as a summing scaling and averaging amplifier',
        'theory_list': [
            {
                'texts': [
                    "The OP-AMP can act as summing, scaling and averaging amplifier depending upon the different values of resisters used.",
                ],
            },
            {
                'texts': [
                    "SUMMING: The output of OP-AMP with multiple inverting input is:",
                    "Vout = -RF [V₁/R₁+V₂/R₂+ V3/R3+….]",
                    "If Rf = R₁= R₂= R3 .... Then Vout = - [V₁ + V₂+ V3+......]",
                    "Thus direct voltage addition can also be obtained when all resistors are equal.",
                ],
                'images':[
                    'experiments/images/naruto.jpg',
                    'experiments/images/naruto.jpg'
                ],
                'simulation': '2'
            },
            {
                'texts': [
                    "SCALING: The output of OP-AMP with multiple inverting input is:",
                    "Vout = -RF [V₁/R₁+V₂/R₂+ V3/R3+…...]",
                    "Thus, voltage scaling is also obtained when all resistors are not equal",
                ],
                'images':[
                    'experiments/images/naruto.jpg',
                    'experiments/images/naruto.jpg'
                ],
                # 'simulation': '2'
            },
            {
                'texts': [
                    "AVERAGING: The output of OP-AMP with N inverting inputs is:",
                    "Vout = -RF [V₁/R₁+V₂/R₂+ V3/R3+…...]",
                    "If RF =R₁ /N= R₂/N= R3/N=....Then Vout= [V₁ + V2+ V3+.......] /N",
                    "Thus, voltage average is also obtained.",
                    "For two inputs N=2",
                    "RF =R₁/3= R₂/3=R3/3",
                    "Vout = - [V1+ V₂+V3]/3",
                ],
                'images':[
                    'experiments/images/naruto.jpg',
                    'experiments/images/naruto.jpg'
                ],
                # 'simulation': '2'
            }
        ],
        # 'procedure': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        # ],
        # 'summary': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",

        # ],
    },
    {
        'id': '3',
        'name': 'To demonstrate working of an op-amp as integrator and differentiator.',
        'theory_list': [
            {
                'texts': [
                    "The op-amp as an integrator is an operational amplifier circuit that performs mathematical operation of integration, i.e., we can cause the output to respond to changes to the input voltages over time as the op-amp integrator produces an output which is proportional to the integral of the input voltage.",    
                ],
                # 'images':[
                #     'experiments/images/naruto.jpg',
                #     'experiments/images/naruto.jpg'
                # ],
            },
            {
                'texts': [
                "A differentiator circuit is one in which output voltage is directly proportional to the rate of change of input voltage w.r.t. time. The greater the change, the higher is the output. For the square wave input, only short spikes should be seen. The spikes will be limited by the slope of edge of the input waveform and also the maximum output of the circuit. The op amp differentiator has resistive element in the feedback from the output to the inverting input. This gives it DC stability. The voltage output for the op amp differentiator is v0 = -Rf C dVin/dt.",
                ],
                # 'images':[
                #     'experiments/images/naruto.jpg',
                #     'experiments/images/naruto.jpg'
                # ],
                'simulation': '3'
            }
        ],
        # 'procedure': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        # ],
        # 'summary': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",

        # ],
    },
    {
        'id': '4',
        'name': 'To analyse Function generator using operational amplifier (sine, triangular and square wave)',
        'theory_list': [
            {
                'texts': [
                    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
                    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
                    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
                ],
                'images':[
                    'experiments/images/naruto.jpg',
                    'experiments/images/naruto.jpg'
                ],
            },
            {
                'texts': [
                    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
                    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
                ],
                'images':[
                    'experiments/images/naruto.jpg',
                    'experiments/images/naruto.jpg'
                ],
                'simulation': '4'
            }
        ],
        'procedure': [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        ],
        'summary': [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",

        ],
    },
    {
        'id': '5',
        'name': 'To demonstrate working of an op-amp as a low pass filter',
        'theory_list': [
            {
                'texts': [
                    "OP Amp can be used as a low pass filter when connections are done according to given figure. In this connection, filter will allow to pass low frequency signal and stop high frequencies. Ideally, low pass filter allows low frequency signal and passes infinite attenuation for frequency above cut off frequency but practically OP Amp will pass frequency till the gain is 707 Amax (Amax-Max gain) of OP Amp when frequency of input signal tending zero.",
                    "The output of non-inverting amplifier is",
                    "Vo=(1+Rf/R1) Vin",
                    "Vin is voltage across capacitor at non inverting amplifier is",
                    "Vo = Xc /(R+Xc)=1/jwc(R+jwc)",
                    "Wc = -1/RC       fc = 1/2 pi*RC",
                    "Vo/Vin = (1+Rf/R1) (1/1+jwCR)",
                ],
                'images':[
                    'experiments/images/low_pass_filter.jpeg',
                    # 'experiments/images/naruto.jpg',
                    # 'experiments/images/naruto.jpg'
                ],
                'simulation': '5'
            },
            # {
            #     'texts': [
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #     ],
            #     'images':[
            #         'experiments/images/naruto.jpg',
            #         'experiments/images/naruto.jpg'
            #     ],
            #     'simulation': '5'
            # }
        ],
        # 'procedure': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        # ],
        # 'summary': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        # ],
    },
    {
        'id': '6',
        'name': 'To demonstrate working of an op-amp as a high pass filter',
        'theory_list': [
            # {
            #     'texts': [
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #     ],
            #     'images':[
            #         'experiments/images/naruto.jpg',
            #         'experiments/images/naruto.jpg'
            #     ],
            # },
            {
                'texts': [
                    "A high-pass filter is an electronic filter that passes signals with a frequency higher than a certain cut-off frequency and attenuates signals with frequencies lower than the cut-off frequency. The amount of attenuation for each frequency depends on the filter design. A high pass filter is usually modelled as a linear time-invariant system. It is sometimes called a low-cut er or bass-cut filter. High-pass filters have many uses, such blocking DC from circuitry sensitive to non-zero average voltages or radio frequency devices. They can also be used in conjunction with a low-pass filter to produce a bandpass filter.",
                ],
                # 'images':[
                #     'experiments/images/naruto.jpg',
                #     'experiments/images/naruto.jpg'
                # ],
                'simulation': '6'
            }
        ],
        # 'procedure': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        # ],
        # 'summary': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",

        # ],
    },
    {
        'id': '7',
        'name': 'To demonstrate op-amp as Schmitt trigger',
        'theory_list': [
            # {
            #     'texts': [
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #     ],
            #     'images':[
            #         'experiments/images/naruto.jpg',
            #         'experiments/images/naruto.jpg'
            #     ],
            # },
            {
                'texts': [
                    "A Schmitt Trigger is a comparator circuit with hysteresis implemented by applying positive feedback to the noninverting input of a comparator or differential amplifier. A Schmitt Trigger uses two input different threshold voltage level to avoid noise  in the  input  signal. The  action from this dual-threshold is known as hysteresis.",
                    "The Schmitt trigger  gives  proper  results  even if the  input  signal is noisy. It uses two threshold voltages; one is the upper threshold voltage (VUT) and the second is lower threshold voltage (VLT).",
                    "The output of the Schmitt trigger remains low until the input signal crosses VUT. Once the input signal cross this limit VUT, the output signal of the Schmitt trigger remains high until the input signal is below the level of VLT.",
                    "The Schmitt trigger circuit uses positive feedback. Therefore, this circuit is also known as the regenerative comparator circuit. The Schmitt trigger circuit can be designed using Op-Amp in two ways. If the input signal is connected at the inverting point of Op-Amp, it is known as Inverting Schmitt Trigger. And if the input signal is connected at the non- inverting point of Op-Amp, it is known as Non-inverting Schmitt Trigger.",
                ],
                # 'images':[
                #     'experiments/images/naruto.jpg',
                #     'experiments/images/naruto.jpg'
                # ],
                'simulation': '7'
            }
        ],
        # 'procedure': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        # ],
        # 'summary': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",

        # ],
    },
    {
        'id': '8',
        'name': 'To demonstrate the operation of a 555 timer as monostable multivibrator',
        'theory_list': [
            # {
            #     'texts': [
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #     ],
            #     'images':[
            #         'experiments/images/naruto.jpg',
            #         'experiments/images/naruto.jpg'
            #     ],
            # },
            {
                'texts': [
                    "A Mono-stable multi-vibrator (MMV) often called a one-shot multi- vibrator, is a pulse generator circuit in which the duration of the pulse is determined by the R-C network, connected externally to  the  555 timer. In such a vibrator, one state of output is stable while the other is quasi-stable (unstable). For auto-triggering of output from quasi-stable state to stable state energy is stored by an externally connected capacitor C to a reference level. The time taken in storage determines the pulse width. The transition of output from stable state to quasi-stable state is accomplished by external triggering. The schematic of a 555 timer in mono-stable mode of operation is shown in figure:",
                ],
                # 'images':[
                #     'experiments/images/naruto.jpg',
                #     'experiments/images/naruto.jpg'
                # ],
                'simulation': '8'
            }
        ],
        # 'procedure': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        # ],
        # 'summary': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",

        # ],
    },
    {
        'id': '9',
        'name': 'To demonstrate the operation of a 555 timer as astable multivibrator',
        'theory_list': [
            # {
            #     'texts': [
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
            #     ],
            #     'images':[
            #         'experiments/images/naruto.jpg',
            #         'experiments/images/naruto.jpg'
            #     ],
            # },
            {
                'texts': [
                    "Astable Multivibrator mode  of  555  timer  IC  is  also  called Free running or self-triggering mode. Unlike Monostable Multivibrator mode it doesn’t have any stable state, it has two quasi stable state (HIGH and LOW). No external triggering is required in Astable mode, it automatically interchange its two states on a particular interval, hence generates a rectangular waveform. This time duration of HIGH and LOW output has been determined by the external resistors (R1 and R2) and a capacitor(C1). Astable mode works as a oscillator circuit, in which output oscillate at a particular frequency and generate pulses in rectangular wave form.",
                ],
                # 'images':[
                #     'experiments/images/naruto.jpg',
                #     'experiments/images/naruto.jpg'
                # ],
                'simulation': '9'
            }
        ],
        # 'procedure': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        # ],
        # 'summary': [
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged",

        # ],
    }
]


def experiments(request):
    context = {'experiments': experiments_list}
    return render(request, 'experiments/experiments.html', context)


def experiment(request, arg):
    experiment = {}
    for exp in experiments_list:
        if exp['id'] == arg:
            experiment = exp
    context = {'experiment': experiment}
    return render(request, 'experiments/experiment.html', context)


def empty_graph(log_graph=False):
    plt.switch_backend('agg')
    figure, axe = plt.subplots(figsize=(12, 4))
    plt.grid()
    if log_graph:
        plt.xscale('log')
        plt.xlim(0.01, 10e3)
    plt.tight_layout()
    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def simulation(request, arg):
    print(arg)
    graph = ''
    if arg == '1a':
        amp = 1
        freq = 1
        R1_val = 10
        R2_val = 90
        Load = 10
        limit_op_amp = 15
        errors = {}
        if request.method == "POST":
            invalid = 0

            amp, amp_err, check = Verify.int_check(request.POST['amp'], 1, 10)
            invalid |= check
            errors["amp_err"] = amp_err
            freq, freq_err, check = Verify.int_check(
                request.POST['freq'], 1, 10)
            invalid |= check
            errors["freq_err"] = freq_err
            R1_val, R1_val_err, check = Verify.int_check(
                request.POST['R1_val'], 10, 100)
            invalid |= check
            errors["R1_val"] = R1_val_err
            R2_val, R2_val_err, check = Verify.int_check(
                request.POST['R2_val'], 10, 100)
            invalid |= check
            errors["R2_val"] = R2_val_err
            Load, Load_err, check = Verify.int_check(
                request.POST['Load'], 10, 100)
            invalid |= check
            errors["Load_err"] = Load_err
            limit_op_amp, limit_op_amp_err, check = Verify.int_check(
                request.POST['limit_op_amp'], 10, 15)
            invalid |= check
            errors["limit_op_amp_err"] = limit_op_amp_err

            if invalid:
                graph = empty_graph()
            else:
                graph = S1.non_inverting(amp=amp, freq=freq, R1_val=R1_val,
                                         R2_val=R2_val, Load=Load, limit_op_amp=limit_op_amp)
        elif request.method == 'GET':
            graph = empty_graph()
        context = {
            'amp': amp,
            'freq': freq,
            'R1_val': R1_val,
            'R2_val': R2_val,
            'Load': Load,
            'limit_op_amp': limit_op_amp,
            'arg': arg,
            'graph': graph,
            'errors': errors,
        }
    elif arg == '1b':
        print('1b')
        amp = 1
        freq = 1
        R1_val = 10
        R2_val = 90
        Load = 10
        limit_op_amp = 15
        errors = {}
        if request.method == "POST":
            invalid = 0

            amp, amp_err, check = Verify.int_check(request.POST['amp'], 1, 10)
            invalid |= check
            errors["amp_err"] = amp_err
            freq, freq_err, check = Verify.int_check(
                request.POST['freq'], 1, 10)
            invalid |= check
            errors["freq_err"] = freq_err
            R1_val, R1_val_err, check = Verify.int_check(
                request.POST['R1_val'], 10, 100)
            invalid |= check
            errors["R1_val"] = R1_val_err
            R2_val, R2_val_err, check = Verify.int_check(
                request.POST['R2_val'], 10, 100)
            invalid |= check
            errors["R2_val"] = R2_val_err
            Load, Load_err, check = Verify.int_check(
                request.POST['Load'], 10, 100)
            invalid |= check
            errors["Load_err"] = Load_err
            limit_op_amp, limit_op_amp_err, check = Verify.int_check(
                request.POST['limit_op_amp'], 10, 15)
            invalid |= check
            errors["limit_op_amp_err"] = limit_op_amp_err

            if invalid:
                graph = empty_graph()
            else:
                graph = S1.inverting(amp=amp, freq=freq, R1_val=R1_val,
                                     R2_val=R2_val, Load=Load, limit_op_amp=limit_op_amp)
        elif request.method == 'GET':
            graph = empty_graph()
        context = {
            'amp': amp,
            'freq': freq,
            'R1_val': R1_val,
            'R2_val': R2_val,
            'Load': Load,
            'limit_op_amp': limit_op_amp,
            'arg': arg,
            'graph': graph,
            'errors': errors,
        }
    elif arg == '2':
        Rf = 10
        R1 = 10
        R2 = 10
        R3 = 10
        A1 = 10
        A2 = 10
        A3 = 10
        freq1 = 1  # range between 1- 10
        freq2 = 1
        freq3 = 1
        errors = {}
        type = ['sin', 'square']
        choice1 = type[1]
        choice2 = type[0]
        choice3 = type[0]
        if request.method == "POST":
            print(request.POST)
            invalid = 0

            Rf, Rf_err, check = Verify.int_check(request.POST['rf'], 1, 50)
            invalid |= check
            errors["Rf_err"] = Rf_err

            R1, R1_err, check = Verify.int_check(request.POST['r1'], 1, 50)
            invalid |= check
            errors["R1_err"] = R1_err

            R2, R2_err, check = Verify.int_check(request.POST['r2'], 1, 50)
            invalid |= check
            errors["R2_err"] = R2_err

            R3, R3_err, check = Verify.int_check(request.POST['r3'], 1, 50)
            invalid |= check
            errors["R3_err"] = R3_err

            A1, A1_err, check = Verify.int_check(request.POST['a1'], 1, 50)
            invalid |= check
            errors["A1_err"] = A1_err

            A2, A2_err, check = Verify.int_check(request.POST['a2'], 1, 50)
            invalid |= check
            errors["A2_err"] = A2_err

            A3, A3_err, check = Verify.int_check(request.POST['a3'], 1, 50)
            invalid |= check
            errors["A3_err"] = A3_err

            freq1, freq1_err, check = Verify.int_check(
                request.POST['freq1'], 1, 50)
            invalid |= check
            errors["freq1_err"] = freq1_err

            freq2, freq2_err, check = Verify.int_check(
                request.POST['freq2'], 1, 50)
            invalid |= check
            errors["freq2_err"] = freq2_err

            freq3, freq3_err, check = Verify.int_check(
                request.POST['freq3'], 1, 50)
            invalid |= check
            errors["freq3_err"] = freq3_err

            choice1, choice1_err, check = Verify.choice_check(
                request.POST['choice1'], type)
            invalid |= check
            errors["choice1_err"] = choice1_err

            choice2, choice2_err, check = Verify.choice_check(
                request.POST['choice2'], type)
            invalid |= check
            errors["choice2_err"] = choice2_err

            choice3, choice3_err, check = Verify.choice_check(
                request.POST['choice3'], type)
            invalid |= check
            errors["choice3_err"] = choice3_err

            if invalid:
                graph = empty_graph()
            else:
                graph = S2.result(Rf=Rf, R=(R1, R2, R3), A=(A1, A2, A3), freq=(
                    freq1, freq2, freq3), type=(choice1, choice2, choice3))
        else:
            graph = empty_graph(True)
        context = {
            'graph': graph,
            'Rf': Rf,
            'R1': R1,
            'R2': R2,
            'R3': R3,
            'A1': A1,
            'A2': A2,
            'A3': A3,
            'freq1': freq1,
            'freq2': freq2,
            'freq3': freq3,
            'choice1': choice1,
            'choice2': choice2,
            'choice3': choice3,
            'errors': errors,
        }
    elif arg == '3a':
        R = 1
        C = 2
        freq = 1
        type = ['Sin', 'Square']
        choice = type[0]
        invalid = 0
        errors = {}
        if request.method == "POST":
            print(request.POST)
            R, R_err, check = Verify.int_check(request.POST['R'], 1, 50)
            invalid |= check
            errors["R_err"] = R_err

            C, C_err, check = Verify.float_check(request.POST['C'], 1, 10)
            invalid |= check
            errors["C_err"] = C_err

            freq, freq_err, check = Verify.int_check(
                request.POST['freq'], 1, 10)
            invalid |= check
            errors["freq_err"] = freq_err

            choice, choice_err, check = Verify.choice_check(
                request.POST['choice'], type)
            invalid |= check
            errors["choice_err"] = choice_err
            if invalid:
                graph = empty_graph()
            else:
                if choice == 'Sin':
                    graph = S3.integration_sin(R=R, C=C, freq=freq)
                elif choice == 'Square':
                    graph = S3.integration_pulse(R=R, C=C, freq=freq)
        else:
            graph = empty_graph(True)
        context = {
            'freq': freq,
            'R': R,
            'C': C,
            'arg': arg,
            'graph': graph,
            'errors': errors
        }
    elif arg == '3b':
        R = 1
        C = 2
        freq = 1
        type = ['Sin', 'Square']
        choice = type[0]
        invalid = 0
        errors = {}
        if request.method == "POST":
            print(request.POST)
            R, R_err, check = Verify.int_check(request.POST['R'], 1, 50)
            invalid |= check
            errors["R_err"] = R_err

            C, C_err, check = float(request.POST['C'], 1, 10)
            invalid |= check
            errors["C_err"] = C_err

            freq, freq_err, check = Verify.int_check(
                request.POST['freq'], 1, 10)
            invalid |= check
            errors["freq_err"] = freq_err

            choice, choice_err, check = Verify.choice_check(
                request.POST['choice'], type)
            invalid |= check
            errors["choice_err"] = choice_err
            if invalid:
                graph = empty_graph()
            else:
                if choice == 'Sin':
                    graph = S3.diff_sin(R=R, C=C, freq=freq)
                elif choice == 'Square':
                    graph = S3.diff_pulse(R=R, C=C, freq=freq)
        else:
            graph = empty_graph(True)
        context = {
            'freq': freq,
            'R': R,
            'C': C,
            'arg': arg,
            'graph': graph,
        }
    elif arg == '4':
        graph = S4.function_gen()
        context = {
            'graph': graph
        }
    elif arg == '5':
        R1_val = 1
        C1_val = 1
        R3_val = 9
        R2_val = 1
        invalid = 0
        errors = {}
        if request.method == "POST":
            print(request.POST)
            form_value = request.POST.copy()
            t1 = form_value.getlist('table')
            table = []
            i = 0
            while(i < len(t1)):
                table.append([t1[i], t1[i+1], t1[i+2], t1[i+3], t1[i+4]])
                i += 5
            R1_val, R1_val_err, check = Verify.float_check(
                request.POST['r1'], 1, 30)
            invalid |= check
            errors["R1_val_err"] = R1_val_err

            C1_val, C1_val_err, check = Verify.float_check(
                request.POST['c1'], 0.1, 5)
            invalid |= check
            errors["C1_val_err"] = C1_val_err

            R2_val, R2_val_err, check = Verify.int_check(
                request.POST['r2'], 1, 100)
            invalid |= check
            errors["R2_val_err"] = R2_val_err

            R3_val, R3_val_err, check = Verify.int_check(
                request.POST['r3'], 1, 100)
            invalid |= check
            errors["R3_val_err"] = R3_val_err
            if invalid:
                graph = empty_graph(True)
            else:
                graph, break_frequency = S5.graph(
                    R1_val=R1_val, R2_val=R2_val, R3_val=R3_val, C1_val=C1_val)
                if [str(C1_val), str(R1_val), str(R2_val), str(R3_val), str(break_frequency)] not in table:
                    table.append(
                        [C1_val, R1_val, R2_val, R3_val, break_frequency])
        else:
            graph = empty_graph(True)
            table = [['C1', 'R1', 'R2', 'R3', 'break_frequency']]

        context = {
            'R1_val': R1_val,
            'R2_val': R2_val,
            'R3_val': R3_val,
            'C1_val': C1_val,
            'arg': arg,
            'graph': graph,
            'table': table,
            'errors': errors,
        }
    elif arg == '6':
        R1_val = 1
        C1_val = 1
        R3_val = 9
        R2_val = 1
        invalid = 0
        errors = {}
        if request.method == "POST":
            print(request.POST)
            form_value = request.POST.copy()
            t1 = form_value.getlist('table')
            table = []
            i = 0
            while(i < len(t1)):
                table.append([t1[i], t1[i+1], t1[i+2], t1[i+3], t1[i+4]])
                i += 5
            R1_val, R1_val_err, check = Verify.float_check(
                request.POST['r1'], 1, 30)
            invalid |= check
            errors["R1_val_err"] = R1_val_err

            C1_val, C1_val_err, check = Verify.float_check(
                request.POST['c1'], 0.1, 5)
            invalid |= check
            errors["C1_val_err"] = C1_val_err

            R2_val, R2_val_err, check = Verify.int_check(
                request.POST['r2'], 1, 100)
            invalid |= check
            errors["R2_val_err"] = R2_val_err

            R3_val, R3_val_err, check = Verify.int_check(
                request.POST['r3'], 1, 100)
            invalid |= check
            errors["R3_val_err"] = R3_val_err
            if invalid:
                graph = empty_graph(True)
            else:
                graph, break_frequency = S6.graph(
                    R1_val=R1_val, R2_val=R2_val, R3_val=R3_val, C1_val=C1_val)
                if [str(C1_val), str(R1_val), str(R2_val), str(R3_val), str(break_frequency)] not in table:
                    table.append(
                        [C1_val, R1_val, R2_val, R3_val, break_frequency])
        else:
            graph = empty_graph(True)
            table = [['C1', 'R1', 'R2', 'R3', 'break_frequency']]
        context = {
            'R1_val': R1_val,
            'R2_val': R2_val,
            'R3_val': R3_val,
            'C1_val': C1_val,
            'arg': arg,
            'graph': graph,
            'table': table,
            'errors': errors,
        }
    elif arg == '7':
        amp = 2
        freq = 1
        R1_val = 1
        R2_val = 2
        limit_op_amp = 15
        invalid = 0
        errors = {}
        if request.method == "POST":
            print(request.POST)
            form_value = request.POST.copy()
            t1 = form_value.getlist('table')
            table = []
            i = 0
            print(len(t1))
            while(i < len(t1)):
                table.append([t1[i], t1[i+1], t1[i+2], t1[i+3],
                             t1[i+4], t1[i+5], t1[i+6], t1[i+7]])
                i += 8
            amp, amp_err, check = Verify.int_check(request.POST['amp'], 1, 10)
            invalid |= check
            errors["amp_err"] = amp_err

            freq, freq_err, check = Verify.int_check(
                request.POST['freq'], 1, 10)
            invalid |= check
            errors["freq_err"] = freq_err

            R1_val, R1_val_err, check = Verify.int_check(
                request.POST['R1_val'], 1, 50)
            invalid |= check
            errors["R1_val_err"] = R1_val_err

            R2_val, R2_val_err, check = Verify.int_check(
                request.POST['R2_val'], 1, 50)
            invalid |= check
            errors["R2_val_err"] = R2_val_err

            limit_op_amp, limit_op_amp_err, check = Verify.int_check(
                request.POST['limit_op_amp'], 10, 15)
            invalid |= check
            errors["limit_op_amp_err"] = limit_op_amp_err
            if invalid:
                graph = empty_graph()
            else:
                graph, Vut, Vlt, Vhysteresis = S7.schmit(
                    amp=amp, freq=freq, R1_val=R1_val, R2_val=R2_val, limit_op_amp=limit_op_amp)
                if [str(amp), str(freq), str(R1_val), str(R2_val), str(limit_op_amp), str(Vut), str(Vlt), str(Vhysteresis)] not in table:
                    table.append([amp, freq, R1_val, R2_val,
                                 limit_op_amp, Vut, Vlt, Vhysteresis])
        else:
            graph = empty_graph(True)
            table = [['amp', 'freq', 'R1_val', 'R2_val',
                      'limit_op_amp', 'Vut', 'Vlt', 'Vhysteresis']]
        context = {
            'graph': graph,
            'amp': amp,
            'freq': freq,
            'R1_val': R1_val,
            'R2_val': R2_val,
            'limit_op_amp': limit_op_amp,
            'table': table,
            'errors': errors,
        }
    elif arg == '8':
        vin = 5
        C_val = 10
        ohms = 50
        sim_time = 3
        invalid = 0
        errors = {}
        if request.method == "POST":
            print(request.POST)
            form_value = request.POST.copy()
            t1 = form_value.getlist('table')
            table = []
            i = 0
            while(i < len(t1)):
                table.append([t1[i], t1[i+1], t1[i+2], t1[i+3]])
                i += 4
            vin, vin_err, check = Verify.int_check(request.POST['Vin'], 1, 10)
            invalid |= check
            errors["vin_err"] = vin_err

            C_val, C_val_err, check = Verify.float_check(
                request.POST['Cval'], 10, 30)
            invalid |= check
            errors["C_val_err"] = C_val_err

            ohms, ohms_err, check = Verify.int_check(
                request.POST['ohms'], 50, 500)
            invalid |= check
            errors["ohms_err"] = ohms_err

            sim_time, sim_time_err, check = Verify.int_check(
                request.POST['time'], 1, 20)
            invalid |= check
            errors["sim_time_err"] = sim_time_err

            if invalid:
                graph = empty_graph()
            else:
                graph, time_high = S8.graph(
                    vin=vin, farads=C_val, ohms=ohms, sim_time=sim_time)
                if [str(vin), str(C_val), str(ohms), str(time_high)] not in table:
                    table.append([vin, C_val, ohms, time_high])
        else:
            graph = empty_graph()
            table = [['vin', 'c_val', 'ohms', 'time_high']]
        context = {
            'vin': vin,
            'C_val': C_val,
            'ohms': ohms,
            'sim_time': sim_time,
            'arg': arg,
            'graph': graph,
            'table': table,
            'errors': errors,
        }
    elif arg == '9':
        vin = 5
        C_val = 10
        ohms_a = 10
        ohms_b = 10
        sim_time = 1
        invalid = 0
        errors = {}
        if request.method == "POST":
            print(request.POST)
            form_value = request.POST.copy()
            t1 = form_value.getlist('table')
            table = []
            i = 0
            while(i < len(t1)):
                table.append([t1[i], t1[i+1], t1[i+2], t1[i+3],
                             t1[i+4], t1[i+5], t1[i+6]])
                i += 7
            vin, vin_err, check = Verify.int_check(request.POST['Vin'], 1, 10)
            invalid |= check
            errors["vin_err"] = vin_err

            C_val, C_val_err, check = Verify.float_check(
                request.POST['Cval'], 10, 20)
            invalid |= check
            errors["C_val_err"] = C_val_err

            ohms_a, ohms_a_err, check = Verify.int_check(
                request.POST['ohms_a'], 10, 100)
            invalid |= check
            errors["ohms_a_err"] = ohms_a_err

            ohms_b, ohms_b_err, check = Verify.int_check(
                request.POST['ohms_b'], 10, 100)
            invalid |= check
            errors["ohms_b_err"] = ohms_b_err

            sim_time, sim_time_err, check = Verify.int_check(
                request.POST['time'], 1, 10)
            invalid |= check
            errors["sim_time_err"] = sim_time_err
            if invalid:
                graph = empty_graph()
            else:
                graph, time_high, time_low, duty_cycle = S9.graph(
                    vin=vin, farads=C_val, ohms_a=ohms_a, ohms_b=ohms_b, sim_time=sim_time)
                if [str(vin), str(C_val), str(ohms_a), str(ohms_b), str(time_high), str(time_low), str(duty_cycle)] not in table:
                    table.append([vin, C_val, ohms_a, ohms_b,
                                 time_high, time_low, duty_cycle])
        else:
            graph = empty_graph()
            table = [['vin', 'c_val', 'ohms_a', 'ohms_b',
                      'time_high', 'time_low', 'duty_cycle']]
        context = {
            'vin': vin,
            'C_val': C_val,
            'ohms_a': ohms_a,
            'ohms_b': ohms_b,
            'sim_time': sim_time,
            'arg': arg,
            'graph': graph,
            'table': table,
            'errors': errors,
        }
    else:
        print('else')
        context = {
            'experiments': experiments_list,
            'arg': arg,
            'graph': graph,
        }
    return render(request, 'simulations/simulation{}.html'.format(arg), context)

def home(request):
    return render(request, 'experiments/home.html')