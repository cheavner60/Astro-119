#Christian Heavner (Mr. Bowtie)
#Anson Einy (Mr. Orange)
#Megan Splettstoesser (Ms. Spletts)
#Danielle Pedroso (Ms. White)
#Gabrielle Aguilar (Ms. Sandwich)

from numpy import *
from matplotlib.pyplot import *
import urllib2
import struct
import scipy.integrate as integ
from astropy.io import ascii

#created a function that retrieves the file
def fetch_file(sy=2010,sd=01,sm=01,ey=2010,ed=01,em=02):
    print('http://lasp.colorado.edu/lisird/tss/sorce_ssi.csv?&time>={:02d}-{:02d}-{:02d}&time<{:02d}-{:02d}-{:02d}'.format(sy,sm,sd,ey,em,ed))
    urlptr=urllib2.urlopen('http://lasp.colorado.edu/lisird/tss/sorce_ssi.csv?&time>={:04d}-{:02d}-{:02d}&time<{:04d}-{:02d}-{:02d}'.format(sy,sm,sd,ey,em,ed))
    rawdata=urlptr.read()
    urlptr.close()
#write it as a txt file
    fp=open('sundata_{}_{}_{}_to_{}_{}_{}.txt'.format(sy,sm,sd,ey,em,ed),'w')
    fp.write(rawdata)
    fp.close()

#1 create a function that downloads a year of data
def hw4(sy=2010,sd=01,sm=01,ey=2011,ed=01,em=01):
#try to open it if not then download    
    try:
        data=ascii.read('sundata_{}_{}_{}_to_{}_{}_{}.txt'.format(sy,sm,sd,ey,em,ed))
    except:
        print("Downloading file")
        fetch_file(sy,sd,sm,ey,ed,em)
        data=ascii.read('sundata_{}_{}_{}_to_{}_{}_{}.txt'.format(sy,sm,sd,ey,em,ed))
#2 get the wavelengths and number of days down to unique days
    d=data['time (days since 2003-01-24)']
    l=data['wavelength (nm)']
    flux=data['irradiance (W/m^2/nm)']
    wl=np.unique(l)
    nwl=wl.shape[0]
    ud=np.unique(d)
    nd=ud.shape[0]
    fluxaray=array(flux).reshape(nd,nwl)
    baddays=[]
 #3 clean the array. sum rows of the x2 if there is a true then the sum will be greater than 1 
    for n in range(nd):
        x2=isnan(fluxaray[n])
        y2=sum(x2)
        if y2>0:
            baddays.append(n)
    cleanflux=delete(fluxaray,baddays,axis=0)
    nd=cleanflux.shape[0]
    l1=wl[wl<=240]
    o_2=[]
#4 integrate
    for n in range(nd):
        cleanflux1=cleanflux[n]
        cleanflux2=cleanflux1[wl<=240]
#the reason we did it this way is because the formula is the flux divided by   the its corresponding lambda and integrate it over the range of the lambda.
        i=integ.simps(cleanflux2*l1,l1)/(6.626e-34*3.00e8)
        o_2.append(i)
    o_2=array(o_2)
#5 The values of o_2 divided by the mean of o_2 and subtract 1
    do_2=(o_2/mean(o_2))-1
#6 not sure if this is correct, clean up what is printed
    mo=mean(o_2)
    p25=percentile(do_2,25)
    p75=percentile(do_2,75)
    print('<Q(o_2)> {:e} photons/s/m^2'.format(mo))
    print('delta(Q(O_2)) 25th percentile = {:e}, 75th percentile = {:e}'.format(p25,p75))

#7 Plots the valus of the delta vs days.
    nda=arange(nd)
    figure()
    plot(nda,do_2)
    fill_between(nda,p25,p75,facecolor='black', alpha=0.5)
    title('{}-{}-{} to {}-{}-{}'.format(sy,sm,sd,ey,em,ed))
    xlabel('day')
    ylabel('$\delta_{Q(O_2)}$')
    draw()
#8 Create a histogram and a cumulative distrabution 
    hist, edges = histogram(do_2,bins=10)
    g666=do_2.shape[0]
    b20=float(max(hist))
    c4=float(g666)
    x9000=arange(g666)/c4
    figure()
    bar(edges[:-1], hist/b20, width=edges[1:]-edges[:-1])
    do_2.sort()
    plot(do_2,x9000, color='k')
    title('{}-{}-{} to {}-{}-{}'.format(sy,sm,sd,ey,em,ed))
    xlabel('$\delta_{Q(O_2)}$')
    ylabel('Relative Frequency')
    draw()
