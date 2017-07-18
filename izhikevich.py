from brian2 import *

""" All values and equations were taken from https://www.izhikevich.org/publications/spikes.pdf
unless otherwise specified """


a = 0.02 # Dimensionless
b = 0.2 # Dimensionless
c = -65*mV # Voltage to reset to after peak

eqs = '''
dv/dt = 0.04 * (v**2) + 5 * v + 140 - u + I : 1
du/dt = a * (b * v - u) : 1
'''
