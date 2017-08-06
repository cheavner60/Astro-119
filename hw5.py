#Team Unicorn Crew
#Christian Heavner (aka Mr. Bowtie)
#Danielle Pedroso (aka Ms. White)
#Anson Einy (aka Mr. Orange)
#Megan Splettsoesser (aka Ms. Spletts)
#Gabriella Aguilar (aka Ms. Sandwich)

from numpy import *
from matplotlib.pyplot import *
import urllib2
import struct
import scipy.integrate as integ
from astropy.io import ascii
from random import randint


#the derivative function
def derivs(rv,t,g,m1,m2):
#equations taken from class
    x1=rv[0]
    y1=rv[1]
    vx1=rv[2]
    vy1=rv[3]
    x2=rv[4]
    y2=rv[5]
    vx2=rv[6]
    vy2=rv[7]
    r12=sqrt((y2-y1)**2+(x2-x1)**2)
    dx1dt=vx1
    dy1dt=vy1
    dx2dt=vx2
    dy2dt=vy2
    dvx1dt=((g*m2/r12**2)*((x2-x1)/r12))
    dvy1dt=((g*m2/r12**2)*((y2-y1)/r12))
    dvx2dt=((g*m1/r12**2)*((x1-x2)/r12))
    dvy2dt=((g*m1/r12**2)*((y1-y2)/r12))
    return([dx1dt,dy1dt,dvx1dt,dvy1dt,dx2dt,dy2dt,dvx2dt,dvy2dt])

#created a function with 5 manditory values a= semi major axis and e is ecentricity. 
def hw5(m1,m2,a,e,tmax,tstep=1e-3,tplot=0.025,method='leapfrog'):
#fun error messages to display if wrong input is entered
    msg=['Mayonaise Low','Feed me a cat','Im sick of your shit Jeff!','You done goofed', 'Fish is not a valid input','The beatings will continue until morale improves','You do speak english right? This isnt that complex.']
#Place realistic conditions on the values. 
    if m1<=0 or m2<=0 or a<=0 or e<0 or e>=1:
        raise(ValueError((msg[randint(0,6)])))
#define variables in terms of what we have
    q=m1/m2
    tm=m1+m2
    g=6.673e-11
    ro=((1-e)/(1+q))*a
    vo=(sqrt((1+e)/(1-e))*sqrt(g*tm/a))/(1+q)
    rv=(ro,0,0,vo,-q*ro,0,0,-q*vo)
    tau=sqrt((4*pi**2*a**3)/(g*tm))
#number of steps
    nsteps=tmax/tstep
    dt=tau*tstep
    print tau
    print dt
    plot(rv[0], rv[1], 'bo')
    plot(rv[4], rv[5], 'go')
#value of every 40th step
    x9000=1/tstep/40
#axes labels, limits
    xlim([-2*ro,2*ro])
    ylim([-2*ro,2*ro])
    draw()
#created an if statement that only accepts  leapfrog method and odeint all others will raise error message.
    if method=='leapfrog':
        x1=rv[0]
        y1=rv[1]
        vx1=rv[2]
        vy1=rv[3]
        x2=rv[4]
        y2=rv[5]
        vx2=rv[6]
        vy2=rv[7]
        r12=sqrt((y2-y1)**2+(x2-x1)**2)
        for n in range(int(nsteps)):
           x1=x1+dt*vx1
           y1=y1+dt*vy1
           x2=x2+dt*vx2
           y2=y2+dt*vy2
           vx1=vx1+dt*((g*m2/r12**2)*((x2-x1)/r12))
           vy1=vy1+dt*((g*m2/r12**2)*((y2-y1)/r12))
           vx2=vx2+dt*((g*m1/r12**2)*((x1-x2)/r12))
           vy2=vy2+dt*((g*m1/r12**2)*((y1-y2)/r12))
           r12=sqrt((y2-y1)**2+(x2-x1)**2)
#every 40th of the total orbit it will plot the new positions of the objects
           if n%x9000==0:
               cla()
               xlim([-1.5*ro,1.5*ro])
               ylim([-1.5*ro,1.5*ro])
               plot(x1,y1,'bo')
               plot(x2,y2,'go')
               draw()
#plots the final output of the for loop
        cla()
        xlim([-1.5*ro,1.5*ro])
        ylim([-1.5*ro,1.5*ro])
        plot(x1,y1,'bo')
        plot(x2,y2,'go')
        draw()
#odeint method
    elif method=='odeint':
#range of calculation
        t=(0,dt)
        for n in range(int(nsteps)): 
#calls function defined above
            value=integ.odeint(derivs,rv,t,args=(g,m1,m2))
            rv=value[1]
#every 40th of an orbit plot the position
            if n%x9000==0:
               cla()
               xlim([-1.5*ro,1.5*ro])
               ylim([-1.5*ro,1.5*ro])
               plot(rv[0],rv[1],'bo')
               plot(rv[4],rv[5],'go')
               draw()
#plots the final output of the for loop
        cla()
        xlim([-1.5*ro,1.5*ro])
        ylim([-1.5*ro,1.5*ro])
        plot(rv[0],rv[1],'bo')
        plot(rv[4],rv[5],'go')
        draw()

    else:
        raise ValueError(msg[randint(0,6)])
