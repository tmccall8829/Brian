from brian2 import *
import matplotlib.pyplot as plt

tau = 10*ms

eqs = '''
dv/dt = (1-v)/tau : 1
'''

G = NeuronGroup(10, eqs)
H = NeuronGroup(10, eqs)
S = Synapses(G, G)
S.connect(condition="i!=j", p=0.2)

def visualize_connectivity(S):
	Ns = len(S.source)
	Nt = len(S.target)
	plt.figure(figsize=(10, 4))
	plt.subplot(111)
	plt.plot(zeros(Ns), arange(Ns), 'ok', ms=10)
	plt.plot(ones(Nt), arange(Nt), 'ok', ms=10)
	for i, j in zip(S.i, S.j):
        	plt.plot([0, 1], [i, j], '-k')

	plt.xticks([0, 1], ['Source', 'Target'])
	plt.ylabel('Neuron index')
	plt.xlim(-0.1, 1.1)
	plt.ylim(-1, max(Ns, Nt))
	plt.xlabel('Source neuron index')
	plt.ylabel('Target neuron index')
	plt.show()

visualize_connectivity(S)
