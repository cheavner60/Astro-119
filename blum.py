from numpy import *
from pylab import *
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.image as mpimg

def graph():
    img=mpimg.imread('blumenthal.jpeg')
    x=arange(0,350)
    y=arange(0,250)
    xx,yy=meshgrid(x,y,indexing='ij')
    figure('Red Light')
    ax=gcf().add_subplot(111, projection='3d')
    ax.plot_surface(xx,yy,img[:,:,0],linewidth=0,cmap=cm.Reds)
    draw()
    figure('Green Light')
    ax=gcf().add_subplot(111, projection='3d')
    ax.plot_surface(xx,yy,img[:,:,1],linewidth=0,cmap=cm.Greens)
    draw()
    figure('Blue Light')
    ax=gcf().add_subplot(111, projection='3d')
    ax.plot_surface(xx,yy,img[:,:,2],linewidth=0,cmap=cm.Blues)
    draw()
