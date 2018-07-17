'''
Created on 1 Jun 2009

@author: abench
'''
from numpy import *
from datetime import datetime
import matplotlib.pyplot as plt

UkLetterFreq=array([0.072,
                    0.017,
                    0.052,
                    0.016,
                    0.035,
                    0.017,
                    0.008,
                    0.009,
                    0.023,
                    0.061,
                    0.057,
                    0.006,
                    0.008,
                    0.035,
                    0.036,
                    0.031,
                    0.065,
                    0.094,
                    0.029,
                    0.047,
                    0.041,
                    0.055,
                    0.04,
                    0.001,
                    0.012,
                    0.006,
                    0.018,
                    0.012,
                    0.001,
                    0.004,
                    0.029,
                    0.029,
                    0.034])




UkLetterCodes=array([[1,1,1,0,0,0,0,0],
                [1,1,1,0,0,0,0,1],
                [1,1,1,0,0,0,1,0],
                [1,1,1,0,0,0,1,1],
                [1,1,1,0,0,1,0,0],
                [1,1,1,0,0,1,0,1],
                [1,0,1,1,1,0,1,0],
                [1,1,1,0,0,1,1,0],
                [1,1,1,0,0,1,1,1],
                [1,1,1,0,1,0,0,0],
                [1,0,1,1,0,0,1,1],
                [1,0,1,1,1,1,1,1],
                [1,1,1,0,1,0,0,1],
                [1,1,1,0,1,0,1,0],
                [1,1,1,0,1,0,1,1],
                [1,1,1,0,1,1,0,0],
                [1,1,1,0,1,1,0,1],
                [1,1,1,0,1,1,1,0],
                [1,1,1,0,1,1,1,1],
                [1,1,1,1,0,0,0,0],
                [1,1,1,1,0,0,0,1],
                [1,1,1,1,0,0,1,0],
                [1,1,1,1,0,0,1,1],
                [1,1,1,1,0,1,0,0],
                [1,1,1,1,0,1,0,1],
                [1,1,1,1,0,1,1,0],
                [1,1,1,1,0,1,1,1],
                [1,1,1,1,1,0,0,0],
                [1,1,1,1,1,0,0,1],
                [1,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,0,0],
                [0,0,1,0,0,0,0,0]])


def DigitalBits(row,col):
    return 1
def FillDigitalArray(size):
    result=zeros((power(2,size),size))
    #cycle on each digit
    for d in xrange(size):
        i=0
        #cycle on each combination
        while i<power(2,size):
            #write zeros
            for j in xrange(power(2,d)):
                result[i,d]=0
                i=i+1 
                
            #write ones
            for j in xrange(power(2,d)):
                result[i,d]=1
                i=i+1
                
    return result

def PrintArray(ar):
    for i in xrange(ar.shape[0]):
        for j in xrange(ar.shape[1]):
            print ar[i,j],
        print
def RZEnergySpectrum(x,f,magn,tau):
    # prepare matrix for output results
    W=zeros((x.shape[0],f.shape[0]))
    
    # cycle on number
    
    for n in xrange(x.shape[0]):
        
        # cycle on frequency
        
        for fr in xrange(f.shape[0]):
            s=0
            c=0
            t=2*pi*f[fr]*tau
            
            # cycle on bit
            
            for i in xrange(x.shape[1]):
                
                #calculate C(f) and S(f)
                
                s=s+x[n][i]*sin(i*t)
                c=c+x[n][i]*cos(i*t)
                
            # calculte B(f) and G(f)
                
            B=(2*magn*abs(sin(t/4)))/(2*pi*f[fr])
            G=B*sqrt(c*c+s*s)
            
            # Calculate W(f) and store in output array
            
            W[n][fr]=G*G
    return W

def Manchester2EnergySpectrum(x,f,magn,tau):
    # prepare matrix for output results
    W=zeros((x.shape[0],f.shape[0]))
    
    # cycle on number
    
    for n in xrange(x.shape[0]):
        
        # cycle on frequency
        
        for fr in xrange(f.shape[0]):
            s=0
            c=0
            t=2*pi*f[fr]*tau
            
            # cycle on bit
            
            for i in xrange(x.shape[1]):
                
                #calculate C(f) and S(f)
                
                s=s+(2*x[n][i]-1)*sin(i*t)
                c=c+(2*x[n][i]-1)*cos(i*t)
                
            # calculte B(f) and G(f)
                
                
            B=(magn*sqrt(square(1-2*cos(t/2)+cos(t))+square(2*sin(t/2)-sin(t))))/(2*pi*f[fr])
            G=B*sqrt(c*c+s*s)
            
            # Calculate W(f) and store in output array
            
            W[n][fr]=G*G
    return W



def UsageFrequency(x,fr):
    # prepare matrix for output results
    W=zeros(x.shape[1])
    for n in xrange(x.shape[0]):
        for i in xrange(x.shape[1]):
            W[i]=W[i]+(x[n][i]*fr[n])
    return W
    



def main():
    ''' Ukrainian Letter Spectrum Calculation'''
    
    #--- Constants for calculations
    
    tauimp=1e-6
    taubit=1e-6
    magn=1

    #--- Start calculations 

    t1=datetime.today()
    print 'Start in : ', t1.strftime('%H:%M')
    #print UkLetterCodes.shape[0],'x',UkLetterCodes.shape[1]


    #--- Create Frequency array , input signals and calculate spectrum
    
    Freq=arange(1,2/(taubit),0.01/(tauimp))
    #print Freq
    #Signal=FillDigitalArray(8)
    RZSpectrum=RZEnergySpectrum(UkLetterCodes,Freq,magn,tauimp)
    ManchesterSpectrum=Manchester2EnergySpectrum(UkLetterCodes,Freq,magn,tauimp)
    TotalRZ=UsageFrequency(RZSpectrum,UkLetterFreq)
    TotalManchester=UsageFrequency(ManchesterSpectrum,UkLetterFreq)
    #--- Print time, used to perform calculations
    
    t2=datetime.today()
    print 'End in : ',t2.strftime('%H:%M')
    print 'Calculation time :',t2-t1
    
    
    # --- Plot Graph 
    #plt.figure(1)
    for i in xrange(UkLetterCodes.shape[0]):
        # --- Plot letter shape
        #print i

#        plt.subplot(UkLetterCodes.shape[0]+1,3,i*3+1)
#        plt.plot(UkLetterCodes[i])
#        plt.subplot(UkLetterCodes.shape[0]+1,3,i*3+2)
#        plt.plot(Freq,RZSpectrum[i])
#        plt.subplot(UkLetterCodes.shape[0]+1,3,i*3+3)
#        plt.plot(Freq,ManchesterSpectrum[i])
        
        plt.figure(i)             
        plt.subplot(1,3,1)
        
        plt.step(arange(0,UkLetterCodes.shape[1]+1,1),append(UkLetterCodes[i],0),where='post')
        plt.ylim(ymax=2)
        plt.subplot(1,3,2)
        plt.plot(Freq,RZSpectrum[i])
        plt.subplot(1,3,3)
        plt.plot(Freq,ManchesterSpectrum[i])
        plt.show()        
        
#    plt.subplot(221)
#    plt.plot(Freq,RZSpectrum[29])
#    plt.title('Energy Spectrum of Cyrillic letter RZE, encoded by RZ code')
#    
#    # --- Plot Graph
#    plt.subplot(222)
#    plt.plot(Freq,ManchesterSpectrum[29])
#    plt.title('Energy Spectrum of Cyrillic letter RZE, encoded by Manchester II     code')
#    
#    plt.subplot(223)
#    plt.plot(Freq,TotalRZ)
#    plt.title('Energy Spectrum of Cyrillic text, encoded by RZ code')
#
#    plt.subplot(224)
#    plt.plot(Freq,TotalManchester)
#    plt.title('Energy Spectrum of Cyrillic text, encoded by Manchester II code')
#    plt.show()
    
    raw_input('Press any key')
    # --- Bye
    
    print 'Bye'
    return 0

if __name__=='__main__':
    main()
