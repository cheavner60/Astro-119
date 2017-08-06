#Christian Heavner
#Danielle Pedroso
#Anson Einy
#Megan Splettstoesser
#Gabriella Aguilar

from numpy import *
from matplotlib.pyplot import *
import urllib2
import struct

#1 created a function that takes two optional inputs
def fetch_file(url="https://sites.google.com/a/ucsc.edu/krumholz/teaching-and-courses/ast119_w15/homework-3/hw3.npy",localfile='hw3.npy'):
    #2 download file
    urlptr=urllib2.urlopen(url)
    rawdata=urlptr.read()
    urlptr.close()
    fp=open(localfile,'wb')
    fp.write(rawdata)
    fp.close()
#1 created a file that takes two optional inputs
def hw3(url="https://sites.google.com/a/ucsc.edu/krumholz/teaching-and-c\
ourses/ast119_w15/homework-3/hw3.npy",localfile='hw3.npy'):
# try to open if it doesnt then it downloads the file
    try:
        data=np.load(localfile)
    except:
        print("Warning: file hw3.npy not found; retrieving from the web")
        fetch_file(url,localfile)
        data=np.load(localfile)
#2 determine the size of the of each potion of the 2d array then uses it for the number of elements for the x and y array
    xshape=data.shape[0]
    yshape=data.shape[1]
    x=np.linspace(-1,1,xshape)
    y=np.linspace(-1,1,yshape)
#3 created a rasta graph of the data aded a color bar and saved the file
    imshow(data,aspect='equal',origin='lower',extent=(-1,1,-1,1))
    xlabel('x')
    ylabel('y')
    colorbar()
    draw()
    savefig('hw3a.png')
#4 take the mean of each axis
    rmean=mean(data, axis=1)
    cmean=mean(data, axis=0)
    xmax=max(rmean)
    ymax=max(cmean)
    mx=max(array([xmax,ymax]))
#5 make two new figures
    figure(figsize=(10,7))
#6 create the first subplot and plot x vs y mean then labled the axis and added a legend
    subplot(2,1,1)
    plot(x,cmean,lw=3)
    ylim([0,1.5*mx])
    xlabel('x')
    legend(('y mean',))
    ylabel('Density')
#created the  second sub plot and did that same thing as the last note
    subplot(2,1,2)
    plot(y,rmean,'r',lw=3,)
    ylim([0,1.5*mx])
    legend(('x mean',))
    xlabel('y')
    ylabel('Density')
    subplots_adjust(wspace=2)
    draw()
#7 save the second figure
    savefig('hw3b.png')
