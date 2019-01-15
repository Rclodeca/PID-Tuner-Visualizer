import mechos
import time

def talker():
    '''
    Example of publishing continuous data to topic "chatter"
    '''
    #initializes a node called talker
    talker_node = mechos.Node("talker")

    #create a publisher to publish to topic chatter
    pub = talker_node.create_publisher("chatter")

    while(1):

        #publish message to chatter (must be encoded as string)
        pub.publish("Hello World")
        time.sleep(0.01)

if __name__ == "__main__":
    talker()