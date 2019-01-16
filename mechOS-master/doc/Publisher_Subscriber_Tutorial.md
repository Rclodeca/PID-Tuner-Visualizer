# 1 Writing Publisher and Subscriber Nodes in MechOS
In MechOS, nodes are scripts that contain a single or multiple MechOS node objects. Each MechOS node object has the ability to contain multiple suscribers and pulishers. 

## 1.1 Publishers
A Publisher publishes (or emitts) data to a topic in the form of an ASCII string. Any Subscribers that subscribe to a topic that publisher is emitting two will be able to pick up that message.

## 1.2 Subscribers
Subscribers subscribe to a topic receiving from an emitting publisher.

# 2 Code-Writing a Publisher
The code below is an example of script containing a single MechOS node named "talker" with a single publisher that publishes to topic "chatter".

```python
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
```

## 2.1 The Code Explained

Lets break down the code.
```python
import mechos
```
MechOS must be imported to use its AMAZING communication abilities (HINT: How to become a Ninja).
```python
talker_node = mechos.Node("talker")
pub = talker_node.create_publisher("chatter")
```
To begin any sort of communication with publishers and subscribers, a MechOS node must be declared with a unique name provided (Be sure other nodes communicating in the same network do not have the same node names, or else really really bad destructive things can happen).

```python
    while(1):

        #publish message to chatter (must be encoded as string)
        pub.publish("Hello World")
        time.sleep(0.01)
```
Continually publish the message "Hello World" to the topic "chatter". Note that the data being should be in ASCII format (you are welcome C/C++ programmers).

# 3 Code-Writing a Subscriber

The code below is an example of a MechOS node name "listener" that has a subscriber listening to topic "chatter". 
```python
import mechos
import time

def chatter_callback(chatter_data):
    '''
    Callback function for subscriber to pass data into.

    Parameters:
        chatter_data: The data recieved over topic chatter from publisher. Each
        time a spinOnce is called, the data being sent from the publisher is
        inserted here.
    '''
    print(chatter_data)


def listener():
    '''
    Example of a subsriber subscribing to topic "chatter"
    '''
    #initializes a node called listener
    listener_node = mechos.Node("listener")

    #create a subscriber to subscribe to topic chatter
    sub = listener_node.create_subscriber("chatter", chatter_callback)

    while(1):
        #receive available message for subsriber sub
        listener_node.spinOnce(sub)
        time.sleep(0.5)

if __name__ == "__main__":
    listener()
```
## 3.1 The Code Explained
```python
def chatter_callback(chatter_data):
    print(chatter_data)
```
Subscribers use callback functions to route data when it is read from the master communication node MechOSCore. The data always be passed as the first parameter. In this example, the data received is simply printed out.

```python
listener_node = mechos.Node("listener")
sub = listener_node.create_subscriber("chatter", chatter_callback)
```

Declare a MechOS node named listener. Create on subscriber to topic "chatter" and place the data as the first parameter to the function chatter_callback.

```python
while(1):
        #receive available message for subsriber sub
        listener_node.spinOnce(sub)
        time.sleep(0.5)
```
To actually poll the message received to the subscriber, call the nodes spinOnce function. If the subscribers object is passed as a parameter, then only a message for that subsriber will be polled. If no parameters are passed, then all subscribers will be polled for messages.

# 4 Running your First MechOS Program!

To acutally run a MechOS program, the `mechoscore.py` script needs to be running in its own process to let nodes communicate with each other. Simply open up a terminal and execute this scripts. 

```
Terminal 1:

python mechoscore.py
```
```
Terminal 2:

python example_subscriber.py
```
```
Terminal 3:

python example_publisher.py
```
And there you have it, you have just completed your first MechOS program!!!
