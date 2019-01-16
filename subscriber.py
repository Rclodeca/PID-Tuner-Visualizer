import mechos
import time
#import test2
from pyqtgraph.Qt import QtGui, QtCore
import sys 
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pyqtgraph as pg
import time
import numpy as np
import threading



print("started3")

def listener():
            print("started2")
            '''
            Example of a subsriber subscribing to topic "chatter"
            '''

            #initializes a node called listener
            listener_node = mechos.Node("listener")

            #create a subscriber to subscribe to topic chatter
            sub = listener_node.create_subscriber("chatter", chatter_callback)

            #window.signal.emit(33)
            while(1):
                #receive available message for subsriber sub
                listener_node.spinOnce(sub)
                time.sleep(0.1)

def chatter_callback(chatter_data):
            print("chatter works")
            '''
            Callback function for subscriber to pass data into.
            Parameters:
                chatter_data: The data recieved over topic chatter from publisher. Each
                time a spinOnce is called, the data being sent from the publisher is
                inserted here.
            '''
            #print(chatter_data)
            tokens = chatter_data.split()
            error = float(tokens[0])
            seconds = tokens[1]
            print(str(error) + ", " + str(seconds))
            window.signal.emit(error)


    




class Screen(QtGui.QMainWindow):
        signal = QtCore.Signal(float)


        def __init__(self):
            super(Screen, self).__init__()
            self.initUI()

        def initUI(self):
            
            self.x = np.array([])
            self.y = np.array([])
            self.plt = pg.PlotWidget()
            self.plot = self.plt.plot(self.x, self.y)
            self.plt.addItem(pg.InfiniteLine(pos=2, angle=0, label='Setpoint'))

            addBtn = QtGui.QPushButton('Stop')
            addBtn.clicked.connect(self.stop)
            addBtn.show()

            mainLayout = QtGui.QVBoxLayout()
            mainLayout.addWidget(addBtn)
            mainLayout.addWidget(self.plt)

            self.mainFrame = QtGui.QWidget()
            self.mainFrame.setLayout(mainLayout)
            self.setCentralWidget(self.mainFrame)

            self.time = 5

            self.signal.connect(self.addDataToPlot)

        def addDataToPlot(self, toPlot):
            print("hi")
            
            data = {
                'x': self.time,
                'y': toPlot
            }
            self.x = np.append(self.x, data['x'])
            self.y = np.append(self.y, data['y'])
            self.plot.setData(self.x, self.y)
            self.time += 1

        def stop(self):
            app.quit()
            

if __name__ == "__main__":
    print("started1")

    
    #def update():
    #  window.addDataToPlot(200)
    #   print("hello there")




    app = QtGui.QApplication(sys.argv)
    window = Screen()
    window.show()
    t = threading.Thread(target=listener)
    t.start()
    sys.exit(app.exec_())

   


