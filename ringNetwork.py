from brian2 import *
import matplotlib.pyplot as plt
import time

t0 = time.time()

tau = 10*ms

# Typical equations
eqs = '''
dv/dt = (1 - v)/tau : 1
I : 1
'''

ncell = 20
G = NeuronGroup(ncell, eqs, threshold='v>1', reset="v = 0") #temp threshold and reset
G.I = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # could also use np.zeros but, eh

S = Synapses(G, G, 'w : 1', on_pre='v=v')

M = StateMonitor(G, 'v', record=True)

itr = 0
# Connect cell 0->1, 1->2, etc. up to 18->19
while itr < ncell-1:
	S.connect(i=itr, j=itr+1)
	S.w = '0.2'
	S.delay = '1*ms'
	#print("%d -> %d" % (itr, itr+1))
	itr += 1

S.connect(i=19, j=0) # Finally, connect 19->0 to complete the ring
S.delay = '1*ms'

run(100*ms)

t1 = time.time()
print(t1-t0)

plt.plot(M.t/ms, M.v[0])
plt.xlabel("time (ms)")
plt.ylabel("v")
plt.show()
