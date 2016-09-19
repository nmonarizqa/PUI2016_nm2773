## Homework 2
This folder contains 5 files:

1. `show_bus_locations_nm2773.py` is a file to monitor location (latitude and longitude) of active buses of a desired bus line. The information is given by MTA through its SIRI API. To run the file, type the following line into your terminal:
  ```
  show_bus_locations_nm2773.py <MTA KEY> <BUS LINE>
  ```

2. `get_bus_info_nm2773.py` is a file to get information about active buses' location, next stop (stop name), and its presentable distance (stop status). The info is then exported to a csv file. To run the file, type this following line into your terminal:
  ```
  get_bus_info_nm2773.py <MTA KEY> <BUS LINE> <BUS LINE>.csv
  ```
  
3. `B52.csv` is an output example from file number (2)

4. `HW2_3_nm2773.ipynb` contains steps on how I work with csv data. The data used is "Get the Demographic Statistics by Zip Code data" from the CUSP Data Facility.

5. `HW2_ExtraCredit_nm2773.ipynb` contains steps on how I work with csv data and `datetype` column.  I used "Traffic volume counts" datafrom CUSP Data Facility.

Upon completion, I worked together with Kaylyn and Xueqi, where I helped them to understand how to dig data from JSON, how to write a python script outside jupyter notebook, how to catch arguments, and how to run them in a terminal. I also helped some other CUSP friends in the other day at CUSP library. It feels nice to be able to help them and I hope this initiative could bridging the technical gap between IT and non-IT folks at CUSP 2017.
