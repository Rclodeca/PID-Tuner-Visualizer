'''
Author: Ryan Clode<ryan@theclodes.com>
Last Modified 1/17/2019
Description: This module is a PID Tuner/Visualizer.
'''
import mechos
import time
from pyqtgraph.Qt import QtGui, QtCore
import sys 
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pyqtgraph as pg
import time
import numpy as np
import threading


def listener():
    '''
    A subsriber subscribing to topic "chatter"
    '''

    #initializes a node called listener
    listener_node = mechos.Node("listener")

    #create a subscriber to subscribe to topic chatter
    sub = listener_node.create_subscriber("chatter", chatter_callback)

    while(1):
        #receive available message for subsriber sub
        listener_node.spinOnce(sub)
        time.sleep(0.1)


def chatter_callback(chatter_data):
    '''
    Callback function for subscriber to pass data into.
    Parameters:
        chatter_data: The data recieved over topic chatter from publisher. Each
        time a spinOnce is called, the data being sent from the publisher is
        inserted here.
    '''

    tokens = chatter_data.split()

    #Parse data from publisher
    error = float(tokens[0])
    seconds = int(tokens[1])
    sp = int(tokens[2])

    #Pass SetPoint and Error values to PyQt event loop
    window.signalSP.emit(sp)
    window.signalErr.emit(error)


class Screen(QtGui.QMainWindow):
    '''
    This Class runs a PyQt GUI event loop. 
    Simply graphs PV (Process Variable) vs. Time.
    '''

    #Signals are used to pass data to the event loop from another thread. 
    signalErr = QtCore.Signal(float)
    signalSP = QtCore.Signal(int)

    def __init__(self):
        '''
        Starts GUI by calling initUI()

        Parameters:
            N/A
        Returns:
            N/A
        '''
        super(Screen, self).__init__()
        self.initUI()

    def initUI(self):
        '''
        Draws the Graph on PyQt window. Connects signals (Err, SP) to their
        necessary methods.

        Parameters:
            N/A
        Returns:
            N/A
        '''
        self.x = np.array([])
        self.y = np.array([])
        self.plt = pg.PlotWidget()
        self.plt.setTitle("Process Variable vs. Time")
        self.plt.setLabel('left', "PV")
        self.plt.setLabel('bottom', "Time(s)")
        self.plot = self.plt.plot(self.x, self.y)

        addBtn = QtGui.QPushButton('Stop')
        addBtn.clicked.connect(self.stop)
        addBtn.show()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(addBtn)
        mainLayout.addWidget(self.plt)

        self.mainFrame = QtGui.QWidget()
        self.mainFrame.setLayout(mainLayout)
        self.setCentralWidget(self.mainFrame)

        self.time = 0.0

        self.signalErr.connect(self.addDataToPlot)
        self.signalSP.connect(self.addSetPoint)

        self.sp = 0


    def addSetPoint(self, sp):
        '''
        Updates the current Setpoint and draws it on the graph.

        Parameters:
            sp: The Setpoint as an int
        Returns:
            N/A
        '''
        if sp != self.sp:
            self.sp = sp
            self.plt.addItem(pg.InfiniteLine(pos=sp, angle=0, label='SP'))

    def addDataToPlot(self, toPlot):
        '''
        Updates the graph with a new data point.

        Parameters:
            toPlot: The PV value to be added to the graph. Should be a float.
        Returns:
            N/A
        '''        
        data = {
            'x': self.time,
            'y': toPlot + self.sp
        }
        self.x = np.append(self.x, data['x'])
        self.y = np.append(self.y, data['y'])
        self.plot.setData(self.x, self.y)
        self.time += 0.1

    def stop(self):
        '''
        Stops the PyQt event loop. (Does not close the window)

        Parameters:
            N/A
        Returns:
            N/A
        '''
        app.quit()
            

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    pg.setConfigOptions(antialias = True)
    window = Screen()
    window.setWindowTitle('PID Tuner/Visuaizer')
    window.show()
    
    #creates a new thread to allow listener() and PyQt event loop to run 
    #simultaneously
    t = threading.Thread(target=listener)
    t.start()
    sys.exit(app.exec_())

   


