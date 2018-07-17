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

def AMIEnergySpectrum(x,f,magn,tau):
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
                
            B=(2*magn*abs(sin(t/2)))/(2*pi*f[fr])
            G=B*sqrt(c*c+s*s)
            
            # Calculate W(f) and store in output array
            
            W[n][fr]=G*G

    return W

def UnipolarEnergySpectrum(x,f,magn,tau):
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
                
            B=(2*magn*abs(sin(t/2)))/(2*pi*f[fr])
            G=B*sqrt(c*c+s*s)
            
            # Calculate W(f) and store in output array
            
            W[n][fr]=G*G

    return W

def BipolarEnergySpectrum(x,f,magn,tau):
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
                
                
            B=(2*magn*abs(sin(t/2)))/(2*pi*f[fr])
            G=B*sqrt(c*c+s*s)
            
            # Calculate W(f) and store in output array
            
            W[n][fr]=G*G
    return W



def B2Q1EnergySpectrum(x,f,magn,tau):
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
                
                s=s+(x[n][i])*sin(2*i*t)
                c=c+(x[n][i])*cos(2*i*t)
                
            # calculte B(f) and G(f)
                
                
            B=(2*magn*abs(sin(t)))/(2*pi*f[fr])
            G=B*sqrt(c*c+s*s)
            
            # Calculate W(f) and store in output array
            
            W[n][fr]=G*G
    return W

def EncodeAmi2(inp):
    '''
    AMI encoding.
    Output matrix have doubled number of columns
    '''
    ONE_PLUS_LEVEL=1.0
    ZERO_LEVEL=0.0
    ONE_MINUS_LEVEL=-1.0
    x=ONE_MINUS_LEVEL
    z=ONE_MINUS_LEVEL
    outp=zeros((inp.shape[0],inp.shape[1]*2))
    for i in xrange(inp.shape[0]):
        for j in xrange(inp.shape[1]):
            if inp[i][j]==0:
                if z==ONE_PLUS_LEVEL:
                    y=ONE_MINUS_LEVEL
                    z=ONE_MINUS_LEVEL
                else:
                    y=ONE_PLUS_LEVEL
                    z=ONE_PLUS_LEVEL 
            else:
                y=ZERO_LEVEL
            outp[i][2*j]=y
            outp[i][2*j+1]=ZERO_LEVEL 
            
    return outp

def EncodeAmi1(inp):
    '''
    AMI encoding.
    Output matrix have same size as input
    '''
    ONE_PLUS_LEVEL=1.0
    ZERO_LEVEL=0.0
    ONE_MINUS_LEVEL=-1.0
    x=ONE_MINUS_LEVEL
    z=ONE_MINUS_LEVEL
    outp=zeros((inp.shape[0],inp.shape[1]))
    for i in xrange(inp.shape[0]):
        for j in xrange(inp.shape[1]):
            if inp[i][j]==0:
                if z==ONE_PLUS_LEVEL:
                    y=ONE_MINUS_LEVEL
                    z=ONE_MINUS_LEVEL
                else:
                    y=ONE_PLUS_LEVEL
                    z=ONE_PLUS_LEVEL 
            else:
                y=ZERO_LEVEL
            outp[i][j]=y      
    return outp

def EncodeB2Q1(inp):
    '''
    2BQ1 encoding
    '''
    TWO_PLUS_LEVEL=3.0
    ONE_PLUS_LEVEL=1.0
    ZERO_LEVEL=0.0
    ONE_MINUS_LEVEL=-1.0
    TWO_MINUS_LEVEL=-3.0
    y=ONE_MINUS_LEVEL
    outp=zeros((inp.shape[0],inp.shape[1]/2))
    for i in xrange(inp.shape[0]):
           
        for j in xrange(outp.shape[1]):
            if inp[i][2*j]==1:
                if inp[i][2*j+1]:
                    y=ONE_PLUS_LEVEL
                else:
                    y=TWO_PLUS_LEVEL 
                pass
            else:
                if inp[i][2*j+1]==1:
                    y=ONE_MINUS_LEVEL
                else:
                    y=TWO_MINUS_LEVEL
            outp[i][j]=y
    
    
    return outp


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
    # special frequences for 2BQ1 code
    Freq1=arange(1,2/(taubit*2),0.01/(tauimp*2))
    #print Freq
    #Signal=FillDigitalArray(8)
    AMISignal=EncodeAmi1(UkLetterCodes)
    B2Q1Signal=EncodeB2Q1(UkLetterCodes)
    AMISpectrum=AMIEnergySpectrum(AMISignal,Freq,magn,tauimp)
    B2Q1Spectrum=B2Q1EnergySpectrum(B2Q1Signal,Freq,magn,tauimp)
    RZSpectrum=RZEnergySpectrum(UkLetterCodes,Freq,magn,tauimp)
    ManchesterSpectrum=Manchester2EnergySpectrum(UkLetterCodes,Freq,magn,tauimp)
    UnipolarSpectrum=UnipolarEnergySpectrum(UkLetterCodes,Freq,magn,tauimp)
    BipolarSpectrum=BipolarEnergySpectrum(UkLetterCodes,Freq,magn,tauimp)
    TotalRZ=UsageFrequency(RZSpectrum,UkLetterFreq)
    TotalManchester=UsageFrequency(ManchesterSpectrum,UkLetterFreq)
    TotalAMI=UsageFrequency(AMISpectrum,UkLetterFreq)
    TotalB2Q1=UsageFrequency(B2Q1Spectrum,UkLetterFreq)
    TotalUnipolar=UsageFrequency(UnipolarSpectrum,UkLetterFreq)
    TotalBipolar=UsageFrequency(BipolarSpectrum,UkLetterFreq)
    #--- Print time, used to perform calculations
    
    t2=datetime.today()
    print 'End in : ',t2.strftime('%H:%M')
    print 'Calculation time :',t2-t1
    


   
    # --- Plot Graph 
    plt.figure(1)
#    plt.subplot(221)
    plt.subplot(321)
    plt.plot(Freq*taubit,TotalRZ)
    plt.grid(True)
    plt.xlabel(r'$f  \cdot \tau_i $')
    plt.ylabel(r'$W_{RZ}$')
#    plt.title('Energy Spectrum of Cyrillic letter RZE, encoded by RZ code')
    
    # --- Plot Graph
#    plt.subplot(222)
    plt.subplot(322)
    plt.plot(Freq*taubit,TotalManchester)
    plt.grid(True)
    plt.xlabel(r'$f  \cdot \tau_i $')
    plt.ylabel(r'$W_{MCH}$')
    
    # --- Plot Graph
#    plt.subplot(222)
    plt.subplot(323)
    plt.plot(Freq*taubit,TotalAMI)
    plt.grid(True)
    plt.xlabel(r'$f  \cdot \tau_i $')
    plt.ylabel(r'$W_{AMI}$')
    # --- Plot Graph
#    plt.subplot(222)
    plt.subplot(324)
    plt.plot(Freq*taubit,TotalB2Q1)
    plt.grid(True)
    plt.xlabel(r'$f  \cdot \tau_i $')
    plt.ylabel(r'$W_{2BQ1}$')    

    # --- Plot Graph
#    plt.subplot(222)
    plt.subplot(325)
    plt.plot(Freq*taubit,TotalUnipolar)
    plt.grid(True)
    plt.xlabel(r'$f  \cdot \tau_i $')
    plt.ylabel(r'$W_{Unipolar}$')    
    # --- Plot Graph
#    plt.subplot(222)
    plt.subplot(326)
    plt.plot(Freq*taubit,TotalBipolar)
    plt.grid(True)
    plt.xlabel(r'$f  \cdot \tau_i $')
    plt.ylabel(r'$W_{Bipolar}$')        
#           
    
    
    
#    plt.title('Energy Spectrum of Cyrillic letter RZE, encoded by Manchester II     code')
    
##    plt.subplot(223)
#    plt.subplot(121)
#    plt.plot(Freq,TotalRZ)
#    plt.grid(True)
#    plt.xlabel('f, Hz.')
#    plt.ylabel(r'$W_{RZ}$')
#        
##    plt.title('Energy Spectrum of Cyrillic text, encoded by RZ code')
#
##    plt.subplot(224)
#    plt.subplot(122)
#    plt.plot(Freq,TotalManchester)
#    plt.grid(True)
#    plt.xlabel('f, Hz.')
#    plt.ylabel(r'$W_{MCH}$')
        
 #   plt.title('Energy Spectrum of Cyrillic text, encoded by Manchester II code')
    plt.show()
    
    raw_input('Press any key')
    # --- Bye
    
    print 'Bye'
    return 0

if __name__=='__main__':
    main()
