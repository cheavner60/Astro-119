# UCSC ASTR 119, Winter 2015
# Example solution for homework 1
# Author: Mark Krumholz

# Import the libraries we need
from numpy import *
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import time
from IPython import display

# Define the function and its keyword arguments, giving default values
# of 500 for nsteps, 0.01 for dx, and 0.1 for sigma
def hw1(nsteps=500, dx=0.01, sigma=0.1):

    # Set up the initial arrays
    x = arange(-1, 1, dx)
    y = arange(-1, 1, dx)
    xx, yy = meshgrid(x, y)

    # Initialize the t array
    t = 1.0/(2.0*pi*sigma**2) * exp(-(xx**2 + yy**2)/(2.0*sigma**2))

    # Set the edges to zero
    t[0,:] = 0.0
    t[-1,:] = 0.0
    t[:,0] = 0.0
    t[:,-1] = 0.0

    # Make the initial plot
    fig = figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(xx, yy, t)
    ax.set_zlim([0, 1.0/(2.0*pi*sigma**2)])
    draw()

    # Loop over time
    for n in range(nsteps):

        # Diffuse at this step
        t[1:-1, 1:-1] = 0.2 * (t[1:-1,1:-1] + t[0:-2,1:-1] + 
                               t[2:,1:-1] + t[1:-1,0:-2] + 
                               t[1:-1,2:])

        # Every 10th step display
        if n % 10 == 0:
            surf.remove()
            surf=ax.plot_surface(xx, yy, t)
            display.clear_output(wait=True)
            display.display(fig)
            ax.set_zlim([0, 1.0/(2.0*pi*sigma**2)])
            draw()
            time.sleep(0.1)
