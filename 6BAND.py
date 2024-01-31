#coding=utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os


kpoints = []
klabels = []
kvales = []

with open('KLABELS', 'r', encoding='utf-8') as f:
    kpoints = f.readlines()[1:-3]

		 
for i in range(len(kpoints)):
    while kpoints[i][0]==' ':
        kpoints[i] = kpoints[i][1:]
    kpoints[i] = kpoints[i].rstrip('\n')


for point in kpoints:
    x = point.split(' ')    
    klabels.append(x[0])
    kvales.append(eval(x[-1]))

lines = []
with open('BAND.dat', 'r') as f:
    with open('BAND2.dat', 'w') as f2:
        for line in f.readlines():
            if line[0] == '\n' or line[0] == '#' or line == ' \n':
                line = ''
            f2.write(line)

with open('BAND2.dat', 'rt') as f:
    for line in f.readlines():
        line = line.lstrip(' ')
        line = line.rstrip('\n')
        lines.append(line)

os.remove('BAND2.dat')           
length = len(lines)


for i in range(length):
    lines[i] = lines[i].split('    ')
    lines[i][0] = eval(lines[i][0])
    lines[i][1] = eval(lines[i][1])
    
    
x = []
y = []

for line in lines:
    x.append(line[0])
    y.append(line[1])


y_lim = 8

fig, ax = plt.subplots()
ax.plot(x, y, color='r', linewidth=1)

ax.set_title("Band")
ax.set_xlabel("Wave Vector")
ax.set_ylabel("Energy (eV)")
ax.set_xlim(0, kvales[-1])
ax.set_ylim(-y_lim, y_lim)
ax.set_xticks(kvales)
ax.set_xticklabels(klabels)
ax.tick_params(direction='in')
ax.grid(color='black', axis='x')
plt.axhline(0, color='b', linewidth=0.5, linestyle='--')
fig.tight_layout()
fig.savefig('BAND.pdf')
