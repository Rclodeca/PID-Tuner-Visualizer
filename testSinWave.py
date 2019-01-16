import time
import numpy as np

def talker():
    
    x = np.linspace(-np.pi, np.pi, 201)
    s = np.sin(x)

    print(s)
    i = 0
    #for i in s:
    while(1):
        print(s[i])
        #time.sleep(0.01)
        i+=1

       

if __name__ == "__main__":
    talker()