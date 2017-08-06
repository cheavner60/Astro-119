#Team Unicorn Crew                                                            
#Christian Heavner (aka Mr. Bowtie)                                           
#Danielle Pedroso (aka Ms. White)                                              
#Anson Einy (aka Mr. Orange)                                                   
#Megan Splettsoesser (aka Ms. Spletts)                                        
#Gabriella Aguilar (aka Ms. Sandwich)  

from numpy import *
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import time
from IPython import display
from matplotlib.pyplot import *


#1 Define function hw6
def hw6(length=1.0,ncell=200,trun=500.0,tplot=20.0,heatradius=0.25,heatrate=2.0,theat=100.0,kappa=1.0e-4):
#2 define dx and dt
    dx=length/ncell
    dt=dx**2/(4*kappa)
#3 create an ncell by ncell array of zeroes
    t=zeros((ncell,ncell))
#4 use stuff from online then set up heating array
#put the heating function in step 5
    x=linspace(-length/2+dx/2, length/2-dx/2, ncell)
    y=linspace(-length/2+dx/2, length/2-dx/2, ncell)
    xx,yy=meshgrid(x, y, indexing='ij')
    r=sqrt(xx**2 + yy**2)
    for i in range(ncell):
        for j in range(ncell):
            if r[i,j]>heatradius:
                r[i,j]=0
            else:
                r[i,j]=1

# set the edges equa to zero and difuse over time.
    # total time divided by size of each step gives size of each step
    nts=int(trun/dt)
    nhs=int(theat/dt)
    r2d2=[]
    if dt>dx**2/(4*kappa):
        raise ValueError('stop this shit')
    for m in range(nts+1):
        t[0,:]=0
        t[:,0]=0
        t[-1,:]=0
        t[:,-1]=0
#if the time is when the heat is on use this 
        if m<=nhs:
            t[1:-1, 1:-1]=t[1:-1,1:-1]+(kappa*dt/(dx)**2)*(t[0:-2,1:-1]+t[2:,1:-1]+t[1:-1,0:-2]+t[1:-1,2:]-4*t[1:-1,1:-1])+dt*heatrate*length**2*r[1:-1,1:-1]
#if the heat is off then it will switch to this equation        
        else:
            t[1:-1, 1:-1]=t[1:-1, 1:-1]+(kappa*dt/(dx**2))*(t[0:-2,1:-1]+t[2:,1:-1]+t[1:-1,0:-2]+t[1:-1,2:]-4*t[1:-1, 1:-1])
        mt=amax(t)
        r2d2.append(mt)
#6 plot the max heat at every step
    ntsa=arange(nts+1)
    r2d2=array(r2d2)
    figure()
    plot(ntsa,r2d2)
    xlabel('Time')
    ylabel('Maximum Temperature')
    
#7 Make a roster plot of the temperature reset to zero
    om=max(r2d2)
    t[:,:]=0
    figure()
    imshow(t,aspect='equal',origin='lower',extent=(-length/2,length/2,-length/2,length/2),vmin=0,vmax=om)
    colorbar()
    xlabel('X')
    ylabel('Y')
    title('Time=0 sec')
    draw()
    time.sleep(0.1)
#8 repeat step five this time ploting every once and ahwile as defined by tplot
#every tplot seconds erase and redraw
    for m in range(nts+1):
        t[0,:]=0
        t[:,0]=0
        t[-1,:]=0
        t[:,-1]=0
        if m<=nhs:
            t[1:-1, 1:-1]= t[1:-1, 1:-1]+kappa*dt/dx**2*(t[0:-2,1:-1]+t[2:,1:-1]+t[1:-1,0:-2]+t[1:-1,2:]-4*t[1:-1, 1:-1])+dt*heatrate*length**2*r[1:-1,1:-1]
        else:
            t[1:-1, 1:-1]=t[1:-1, 1:-1]+(kappa*dt/(dx**2))*(t[0:-2,1:-1]+t[2:,1:-1]+t[1:-1,0:-2]+t[1:-1,2:]-4*t[1:-1, 1:-1])
        if m%tplot==0:
            cla()
            imshow(t,aspect='equal',origin='lower',extent=(-length/2,length/2,-length/2,length/2),vmin=0,vmax=om)
            xlabel('X')
            ylabel('Y')
            title('Time='+str(m*dt)+' sec')
            draw()
            time.sleep(0.1)
#Q.E.D.
