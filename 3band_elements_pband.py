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
# 绘制fat-band类型的元素投影能带
#pband_fig = BSPlotterProjected(bs=bs_data)
#pband_fig = pband_fig.get_elt_projected_plots(zero_to_efermi=True, ylim=None, vbm_cbm_marker=False)
#plt.savefig('pband_fat_fig.png',img_format='png')


# 绘制color depends类型的元素投影能带
pband_fig = BSPlotterProjected(bs=bs_data)
pband_fig = pband_fig.get_elt_projected_plots_color()
plt.savefig('pband_color_fig.png',img_format='png')
