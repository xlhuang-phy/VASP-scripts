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
# 绘制投影到不同原子的不同轨道，可以具体到磁量子数。
# dictio:设置原子的磁量子数对应的轨道;
# dictpa:表示原子信息,对应于POSCAR中的原子顺序;
# sum_atoms:相似原子的总和投影,不用此功能,只需设置sum_atoms=None将其关闭,只有一个原子时，原子求和不用写;
# sum_morbs:相似原子的单个轨道的总和投影在一起,不用此功能,只需设置sum_morbs=None将其关闭;
# w_h_size:这个变量帮助你控制图的宽度和高度的。默认情况下,宽度=12和高度=8(英寸)。宽高比保持不变对于子图，每个子图的大小取决于绘制了多少个子图;
# num_column:控制子图的列数,该值应该是整数。默认情况下,num_column=None和子图是在2列中对齐。
# 详情浏览https://pymatgen.org/_modules/pymatgen/electronic_structure/plotter.html
# 轨道：s、px、py、pz、dxy、dxz、dyz、dx2(=dx2-y2)、dz2
pband_fig = BSPlotterProjected(bs=bs_data)
pband_fig = pband_fig.get_projected_plots_dots_patom_pmorb(dictio={'Mo':['dxy','dyz','dz2','dxz','dx2'],'N':['px','py','pz']},\
dictpa={'Mo':[1],'N':[2,3,4,5]},\
sum_atoms={'N':[2,3,4,5]},\
sum_morbs={'Mo':['dz2'],'Mo':['dx2','dxy'],'Mo':['dxz','dyz'],'N':['pz'],'N':['px','py']},\
w_h_size=(12,12),\
num_column=3)
# Main X and Y Labels
plt.xlabel(r'$\mathrm{Wave\ Vector}$', fontsize=30)
zero_to_efermi = True
ylabel = r'$\mathrm{E\ -\ E_f\ (eV)}$' if zero_to_efermi \
    else r'$\mathrm{Energy\ (eV)}$'
plt.ylabel(ylabel, fontsize=30)
plt.ylim(-6,2)
# plt.axhline(0, linewidth=0.5, color='k') # y=0处画线，费米能级
plt.savefig('pband_porbital_fig.png',format='png')

