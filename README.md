# BTI (WORK IN PROGRESS)

##### What is this?
This program reads and displays information sent to a computer's serial port from our solar car's radio. This allows us to view and store valuable information about the car's conditions during a race. 

##### Dependencies
* PySerial
* PyQt4 
* PyQtGraph

### Contributing

Git:
[Quick Git Tutorial if anyone needs it](https://try.github.io/). There are also lots of resources available online if you need help, or ask in the group chat.

##### Getting Started
Python 3 will be used. A virtual environment manager like [conda](http://conda.pydata.org/docs/download.html) may be helpful.

###### On Windows, you can install [WinPython](http://winpython.github.io/), which will include all of the required modules.
1. Clone the repository:  `git clone https://github.com/BlueSkySolar/BTI.git`
2. Install PySerial: `pip install pyserial`
3. Install PyQt4 (The steps vary depending on operating system) (if using conda `conda install pyqt`)
4. Install PyQtGraph `pip install pyqtgraph`

### How to run (temporary)
1. Run main.py
2. Press the button to start/stop receiving data while the radio is connected
(Executables coming soon)
##### How BTI works

The serial data sent to us from the radio on the car is received in the format displayed in [this format](radio_data.txt). The code in bti.py is able to parse this data into a dictionary as seen in [radio_example](radio_example.txt), but we still need to match all of the hex values with their corresponding data type by looking at the [workspace file](legacy_workspace_file.txt) in the old BTI program. We should then be able to display real-time data with proper labeling in the GUI.

### Status

##### Completed Features:
* Connect to a serial device and read the output
* Parse the output from the radio (currently stored in a dictionary)
* Saving parsed radio output dictionary to a text file or CSV file. (Formatting may change)
* Structure and basic display functionality of the GUI

##### Currently Working on:
* Completing the GUI
* Fixing bugs with regards to how to deal with received non-float values
