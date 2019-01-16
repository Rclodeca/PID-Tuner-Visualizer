import mechos
import time
import numpy as np

def talker():
    print("started")
    '''
    Example of publishing continuous data to topic "chatter"
    '''
    #initializes a node called talker
    talker_node = mechos.Node("talker")

    #create a publisher to publish to topic chatter
    pub = talker_node.create_publisher("chatter")

    seconds = 0.0
    
    x = np.linspace(-np.pi, np.pi, 201)
    s = np.sin(x)

    i = 0

    while(1):

       
        pub.publish(str(s[i]) + " " + str(seconds))

        time.sleep(0.01)
        i += 1
        if i > 199:
            i = 0
       
       

if __name__ == "__main__":
    talker()