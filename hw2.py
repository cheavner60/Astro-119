#import libraries
from numpy import *
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import struct

#1 Make data function that takes to arguments with defults
def make_data(filename='hw2.dat',ngrid=100):
    #2 checks parity to ensure even. if not even then subtract 1
    if ngrid%2!=0:
        ngrid=ngrid-1
#3 create two arays that run from -2pi to 2 pi with exactly 1pp elements
    x=np.linspace(-2*pi,2*pi,ngrid)
    y=np.linspace(-2*pi,2*pi,ngrid)
    #4, creating arrays and bianary file. copied from homework
    xx, yy = meshgrid(x, y)
    r = sqrt(xx**2 + yy**2)
    z = sin(r) / r

    fp=open(filename,'wb')
    fp.write(array(ngrid))
    fp.write(x)
    fp.write(y)
    fp.write(z)
    fp.close()

#1 create function
def hw2(filename='hw2.dat',ngrid=100):
    #2 function calls make_data
    make_data(filename,ngrid)
#3 copied from web page
    fp=open(filename,'rb')
    ngrid_raw = fp.read(8)
    ngrid = struct.unpack('l', ngrid_raw)[0]
    xraw=fp.read(ngrid*8)
    x=array(struct.unpack('d'*ngrid,xraw))
    yraw=fp.read(ngrid*8)
    y=array(struct.unpack('d'*ngrid,yraw))
    zraw=fp.read(ngrid**2*8)
    z=array(struct.unpack('d'*ngrid**2,zraw))
    #4 copied from hw
    struct.unpack
    z=reshape(z, (ngrid, ngrid))
    #5 close file
    fp.close()
    #6 make plot of z copied from hw
    xx, yy = meshgrid(x, y)
    fig = figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(xx, yy, z)
    draw()

