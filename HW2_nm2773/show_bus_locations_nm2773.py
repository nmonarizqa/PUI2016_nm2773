'''
    File name: show_bus_locations_nm2773
    Author: Nurvirta Monarizqa
    Date created: 9/15/2016
    Date last modified: 9/16/2016
    Python Version: 2.7
'''

import urllib2
import json
import pandas as pd
import sys

def main():
    key = sys.argv[1]
    bus_route = sys.argv[2]

    bus = getbusdata(key,bus_route)
    printresult(bus,bus_route)

def getbusdata(key,bus_route):
    base = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json'
    param = 'VehicleMonitoringDetailLevel=calls'
    url = base + '?key=' + key + '&' + param + '&LineRef=' + bus_route
    response = urllib2.urlopen(url)
    data = pd.read_json(response)
    df = pd.DataFrame(data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])
    return df

def getlat(df,i):
    return df["MonitoredVehicleJourney"][i]["VehicleLocation"]["Latitude"]
def getlong(df,i):
    return df["MonitoredVehicleJourney"][i]["VehicleLocation"]["Longitude"]

def printresult(df,bus_route):
    print "Bus Line : %s" %(bus_route)
    print "Number of Active Buses : %i" %(len(df))
    for i in range(len(df)):
        print "Bus %i is at latitude %s and longitude %s" %(i,getlat(df,i),getlong(df,i))

if __name__ == '__main__':
    main()
