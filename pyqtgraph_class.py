from pyqtgraph.Qt import QtGui, QtCore
import numpy
import pyqtgraph
import sys


class Plot2D(object):
    def __init__(self):
        self.traces = dict()

        self.phase = 0

        # x-axis
        self.t = numpy.arange(0, 3.0, 0.01) 

        pyqtgraph.setConfigOptions(antialias = True)
        self.app = QtGui.QApplication(sys.argv)
        self.win = pyqtgraph.GraphicsWindow(title = "PID Tuner/Visualizor")
        self.win.resize(1000, 600)
        self.win.setWindowTitle("PID Tuner/Visualizer")
        self.canvas = self.win.addPlot(title = "Plot #1")

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def trace(self,name,dataset_x,dataset_y):
        if name in self.traces:
            self.traces[name].setData(dataset_x,dataset_y)
        else:
            self.traces[name] = self.canvas.plot(pen='y')

    def update(self):
        s = numpy.sin(2 * numpy.pi * self.t + self.phase)
        c = numpy.cos(2 * numpy.pi * self.t + self.phase)
        self.trace("sin", self.t, s)
        self.trace("cos", self.t, c)
        self.phase += 0.1

    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(30)
        self.start()


if __name__ == '__main__':
    p = Plot2D()
    p.animation()