from numpy import *
from datetime import datetime
import matplotlib.pyplot as plt






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
def Calculations(x,f,magn,tau):
    # prepare matrix for output results
    W=zeros((x.shape[0],f.shape[0]))
    
    # cycle on number
    
    for n in xrange(x.shape[0]):
        
        # cycle on frequency
        
        for fr in xrange(f.shape[0]):
            s=0
            c=0
            t=2*pi*fr*tau
            
            # cycle on bit
            
            for i in xrange(x.shape[1]):
                
                #calculate C(f) and S(f)
                
                s=s+x[n][i]*sin(t)
                c=c+x[n][i]*cos(t)
                
            # calculte B(f) and G(f)
                
            B=(magn*sqrt(2*(1-cos(t))))/(t)
            G=B*sqrt(c*c+s*s)
            
            # Calculate W(f) and store in output array
            
            W[n][fr]=G*G
    return W


def main():
    ''' Line Codes Spectrum Calculation'''
    
    #--- Constants for calculations
    
    tauimp=1e-3
    taubit=1e-3
    magn=1

    #--- Start calculations 

    t1=datetime.today()
    print 'Start in : ', t1.strftime('%H:%M')


    #--- Create Frequency array , input signals and calculate spectrum
    
    Freq=arange(0,1000/(taubit),0.2/(tauimp))
    Signal=FillDigitalArray(8)
    Spectrum=Calculations(Signal,Freq,magn,taubit)
    
    #--- Print time, used to perform calculations
    
    t2=datetime.today()
    print 'End in : ',t2.strftime('%H:%M')
    print 'Calculation time :',t2-t1
    raw_input('Press any key')
    
    # --- Plot Graph
    
    plt.ioff()
    for n in xrange(Spectrum.shape[0]):
        plt.plot(Freq,Spectrum[n])
    plt.ion()
    plt.draw()
    plt.show()
    
    # --- Bye
    
    print 'Bye'
    return 0

if __name__=='__main__':
    main()
