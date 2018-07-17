import sys

def LetterFrequency(fname):
    Freq=[]
    for i in xrange(256):
        Freq.append(0.0)
    while True:
        try:
            b=fname.read(1)
#            print b
            
#            Freq[ord(b)]=Freq[ord(b)]+1
        except EOFError:
            break
        
        #print b, ord(b) 
        if len(b)!=0:
            Freq[ord(b)]=Freq[ord(b)]+1
        else:
            break    
    return Freq
def Sum(list):
    s=0
    for i in xrange(len(list)):
        s=s+list[i]
    
    return s

def PrintResult(list,sum,stream):
    for i in xrange(len(list)):
        print >> stream,i,'[',chr(i),']=',list[i]/sum 
    


def main():
    
    f=open(sys.argv[1])
    Freq=LetterFrequency(f)    
    total=Sum(Freq)
    PrintResult(Freq,total,sys.stdout)    
    return
    
if __name__=='__main__':
    main()