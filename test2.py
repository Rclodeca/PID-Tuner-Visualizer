from pyqtgraph.Qt import QtGui, QtCore
import sys 
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pyqtgraph as pg
import time
import numpy as np




class Screen(QtGui.QMainWindow):
    def __init__(self):
        super(Screen, self).__init__()
        self.initUI()

    def initUI(self):
        self.x = np.array([1,2,3,4])
        self.y = np.array([1,4,9,16])
        self.plt = pg.PlotWidget()
        self.plot = self.plt.plot(self.x, self.y)

        addBtn = QtGui.QPushButton('Add Datapoint')
        addBtn.clicked.connect(self.addDataToPlot)
        addBtn.show()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(addBtn)
        mainLayout.addWidget(self.plt)

        self.mainFrame = QtGui.QWidget()
        self.mainFrame.setLayout(mainLayout)
        self.setCentralWidget(self.mainFrame)

        self.time = 5

    def addDataToPlot(self, toPlot):
        data = {
            'x': self.time,
            'y': toPlot
        }
        self.x = np.append(self.x, data['x'])
        self.y =np.append(self.y, data['y'])
        self.plot.setData(self.x, self.y)
        self.time += 1


app = QtGui.QApplication(sys.argv)
window = Screen()

def update():
    window.addDataToPlot(200)
    print("hello there")




if __name__ == "__main__":
    
    window.show()
    sys.exit(app.exec_())