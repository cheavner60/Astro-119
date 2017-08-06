#Christian Heavner (a.k.a) Mr. Bowtie
from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import curve_fit
import urllib2
import struct
import scipy.integrate as integ

#1 create a function that calls the website and has nsteps
def midterm(nsteps=500,url='https://sites.google.com/a/ucsc.edu/krumholz/teaching-and-courses/ast119_w15/homework-3/hw3.npy'):
#try to load file. If it doesn't load download from internet.
    try:
        data=np.load('midterm.npy')
    except:
        urlptr=urllib2.urlopen(url)
        rawdata=urlptr.read()
        urlptr.close()
        fp=open('midterm.npy','wb')
        fp.write(rawdata)
        fp.close()
        data=np.load('midterm.npy')
#3 create a pair of arrays with the number of elements as the data and make mesh grid        
    xshape=data.shape[0]
    yshape=data.shape[1]
    x=linspace(-1,1,xshape)
    y=linspace(-1,1,yshape)
    xx,yy=meshgrid(x,y)
#4 Rasta plot the bastard
    figure()
    imshow(data,aspect='equal',origin='lower',extent=(-1,1,-1,1),vmin=0,vmax=8)
    colorbar()
#5 put red cirlcles at 2 points. label the graph as Step 0
    markers_x=[x[918],x[740]]
    markers_y=[y[392],y[657]]
    plot(markers_x,markers_y,'ro')
    text(x[918], y[392]+0.07, 'Site 1', horizontalalignment='center',color='y')
    text(x[740], y[657]-0.1, 'Site 2', horizontalalignment='center',color='y')
    title('Step 0')
#6 make contours at 3 locations
    contour(xx, yy, data,levels=[0.5,1,2],colors='k')
    draw()
#7 create arays to store the data
    v_site1=zeros(nsteps+1)
    v_site2=zeros(nsteps+1)
    v_site1[0]=data[392,918]
    v_site2[0]=data[657,740]
#8loop create a loop that starts at 1 and goes 
    for n in range(1,nsteps+1):
#to make sure the same point isn't difused. the size of the shift will vary.
#any particular point will be missed once which is unnoticible due to the scale
        data=roll(data,n,axis=0)
        data=roll(data,n,axis=1)
        data[1:-1,1:-1]=0.2*(data[2:,1:-1]+data[:-2,1:-1]+data[1:-1,2:]+data[1:-1,:-2]+data[1:-1,1:-1])
        data=roll(data,-n,axis=0)
        data=roll(data,-n,axis=1)
#9 record the data at every step
        v_site1[n]=data[392,918]
        v_site2[n]=data[657,740]
#10 every 50th step plot the thing
        if n%50==0 and n>1:
            cla()
            imshow(data,aspect='equal',origin='lower',extent=(-1,1,-1,1),vmin=0,vmax=8)
            markers_x=[x[918],x[740]]
            markers_y=[y[392],y[657]]
            plot(markers_x,markers_y,'ro')
            text(x[918], y[392]+0.07, 'Site 1', horizontalalignment='center',color='y')
            text(x[740], y[657]-0.1, 'Site 2', horizontalalignment='center',color='y')
            contour(xx, yy, data,levels=[0.5,1,2],colors='k')
            title('Step '+str(n))
            draw()
#11 plot
    figure()
    plot(arange(nsteps+1),v_site1)
    plot(arange(nsteps+1),v_site2)
    xlabel('Time')
    ylabel('Data')
    legend(['Site 1','Site 2'])
#12 Integrate values at site 1 and 2
    s1i=integ.simps(v_site1,arange(nsteps+1))/(nsteps+1)
    s2i=integ.simps(v_site2,arange(nsteps+1))/(nsteps+1)
    print('site 1 average value is '+str(s1i))
    print('site 2 average value is '+str(s2i))
