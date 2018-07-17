from numpy import *
from datetime import datetime
import time
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
        
        
#        
#void encode_ami()
#{
# unsigned int i ;             // counter
# unsigned int y = ONE_MINUS_LEVEL; // temporary value
# unsigned int z = ONE_MINUS_LEVEL;
# 
# 
# for (i=0;i<SEQUENCE_LEN;i++)
# {
#   switch (inp_sequence[i])
#   {               
#    case '1': 
#               if (z=ONE_PLUS_LEVEL) 
#                   {
#                     y=ONE_MINUS_LEVEL;
#                     z=ONE_MINUS_LEVEL;
#                   }
#               else 
#                  {
#                     y=ONE_PLUS_LEVEL;
#                     z=ONE_PLUS_LEVEL;
#                   };
#               break;              
#    case '0':
#               y=ZERO_LEVEL;
#               break;             
#   }
#   line_sequence[2*i]=y;
#   line_sequence[2*i+1]=ZERO_LEVEL;
#    
# }
#
#}        
        
        
        
        
        
def EncodeAmi(inp):
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
                
                if i!=0:
                    s=s+x[n][i]*sin(t*i)
                c=c+x[n][i]*cos(t*i)
                
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
#    PrintArray(Signal)    
    Ami=EncodeAmi(Signal)
#    PrintArray(Ami)
    Spectrum=Calculations(Signal,Freq,magn,taubit)
    
    #--- Print time, used to perform calculations
    
    t2=datetime.today()
    print 'End in : ',t2.strftime('%H:%M')
    print 'Calculation time :',t2-t1
    z=raw_input('Press any key')
    
    # --- Plot Graph
    
    
    for n in xrange(Spectrum.shape[0]):
#        plt.ioff()
        plt.plot(Freq,Spectrum[n])
#        plt.ion()        
#        plt.draw()
        plt.show()
        time.sleep(10)
#        raw_input('Press any key')
        plt.close()
    
    # --- Bye
    
    print 'Bye'
    return 0

if __name__=='__main__':
    main()
