#set up
from numpy import *
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import time
from IPython import display


#defining function with defult steps then aranging x and y
def hw1(nsteps=500, dx=0.01, sigma=0.1):
    x=arange(-1,1,dx)
    y=arange(-1,1,dx)

#copied from web page
    xx,yy=meshgrid(x, y)
    t = 1.0 / (2.0*pi*sigma**2) * exp(-(xx**2 + yy**2) / (2.0*sigma**2))

#Setting all 4 edges of the grid equal to zero
    t[0,:]=0
    t[:,0]=0
    t[-1,:]=0
    t[:,-1]=0

#copied from the web hw

    fig = figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(xx, yy, t)
    ax.set_zlim([0, 1.0/(2.0*pi*sigma**2)])
    draw()
    
    
    t[1:-1, 1:-1] = 0.2 * (t[1:-1,1:-1] + t[0:-2,1:-1] + 
                       t[2:,1:-1] + t[1:-1,0:-2] + 
                       t[1:-1,2:])

    surf.remove()
    surf=ax.plot_surface(xx, yy, t)
    display.clear_output(wait=True)
    display.display(fig)
    ax.set_zlim([0, 1.0/(2.0*pi*sigma**2)])
    draw()
    time.sleep(0.1)

