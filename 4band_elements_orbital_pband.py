import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Agg')
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter,\
BSPlotter,BSPlotterProjected,DosPlotter
 
# read vasprun.xml，get band and dos information
bs_vasprun = Vasprun("vasprun.xml",parse_projected_eigen=True)
bs_data = bs_vasprun.get_band_structure(line_mode=True)
 
dos_vasprun=Vasprun("vasprun.xml")
dos_data=dos_vasprun.complete_dos
 
# set figure parameters, draw figure
# 绘制投影到指定元素的指定轨道上的能带，用字典规定投影的轨道
# 轨道顺序：s、p、d、f
pband_fig = BSPlotterProjected(bs=bs_data)
pband_fig = pband_fig.get_projected_plots_dots({'Mo':['s','p','d'],'Si':['p','s'],'N':['p','s']})
plt.savefig('pband_orbital_fig.png',img_format='png')

