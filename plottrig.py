# This module plots user-specified trig functions

# Import all the definitions from the numpy and plotting libraries
from numpy import *
from matplotlib.pyplot import *

# Define the plotting function
def makeplot(funcname, wavelength=[2*pi], a=1, p=0):

    # Define the x array
    x=arange(0, 2*pi, 0.01)

    #turn wavelengths into a list
    try:
        for w in wavelength:
            pass
    except TypeError:
            wavelenght=[wavelenght]

#loop over wave lengths
    for w in wavelength:

    # Check if the user entered the sin, cos, or tan function
        if funcname=='sin':
            plot(x, a*sin(x*2*pi/w+p))
        elif funcname=='cos':
            plot(x, a*cos(x*2*pi/w+p))
        elif funcname=='tan':
            plot(x, a*tan(x*2*pi/w+p))
        else:
            print("Unrecognized function "+str(funcname))
            return
