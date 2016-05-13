'''
The GUI

Currently in the progress of testing plotting with PyQtGraph

Code is kind of messy for now, we will move to a more organized
object-oriented approach soon.
'''

import sys
from PyQt4 import QtGui, QtCore
from btiplottestv2 import Ui_MainWindow
import bti
import pyqtgraph as pg
#import numpy as np
#from collections import deque
import datetime  # for text data outputs
import atexit

GRAPH_POINT_LIMIT = 100
app = None
ui = None
win = None
p_battery = None
p_array = None
time = None
radio = None
x1 = [] # battery values 
y1 = []

x2 = []
y2 = [] # variable naming will improve in the future when we start using objects lol 

def makeUI():  # this method is so jank it hurts my soul
    global app, ui, win, p, time

    app = QtGui.QApplication(sys.argv)  # QtGui object

    # Setting up window stuff
    win = QtGui.QMainWindow()
    win.setWindowTitle('pyqtgraph example: ScatterPlotSpeedTest')
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()

    # setup actual plot
    p = ui.plot
    p.setLabel('left', 'Avg Module Voltage', units='V')
    p.setLabel('bottom', 'Time', units='s')

    button = ui.pushButton
    button.clicked.connect(start_listening)

    # start_listening(radio)
    QtGui.QApplication.instance().exec_()


def start_listening():
    global radio, time
    # start timer
    time = QtCore.QTime()
    time.start()

    # connect to radio
    if radio:
        radio.enabled = False
        radio.ser.close()
        radio = None
        return

    radio = bti.serial_device(bti.RADIO_PORT)
    radio.open_port()
    if radio.enabled:
        radio.enabled = False
    elif radio.ser.read(1):
        radio.enabled = True
    else:
        radio.enabled = False
        print("No data received from serial port")

    try:
        while radio.enabled:
            update(radio)
            QtCore.QCoreApplication.processEvents()
    except KeyboardInterrupt:
        # Close radio serial port.
        radio.enabled = False
        radio.ser.close()


def update(radio):
    global x, y, p, time
    data = bti.get_value_dict(bti.get_radio_dict(radio))
    if "Avg Module Voltage (V)" in data:
        while(len(x) >= GRAPH_POINT_LIMIT):
            x = x[1:]
            y = y[1:]
        x.append(time.elapsed())
        y.append(data["Avg Module Voltage (V)"])

        p.plot(x, y)


def file_output(input_dict, output_name):
    '''
    Prints the input dictionary out to a text file.
    Current format is
    YYYY-MM-DD HH:MM:SS || Key: Value | Key: Value ...
    '''
    output_file = open(output_name, "a")
    output_file.write("%s|| " % datetime.datetime.now())
    for key in input_dict.keys():
        output_file.write("%s: %s | " % (key, input_dict[key]))
    output_file.write("\n")


def goodbye():
    global radio
    if radio:
        radio.enabled = False
        radio.ser.close()
        radio = None

if __name__ == '__main__':
    makeUI()
