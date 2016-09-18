'''
    File name: get_bus_info_nm2773
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
    out_file = sys.argv[3]

    bus = getbusdata(key,bus_route)
    res = getresult(bus)
    res.to_csv(out_file,index = False)

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

def getstopname(df,i):
    stopname = df["MonitoredVehicleJourney"][i]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
    if stopname <> "":
        return stopname
    else:
        return "N/A"

def getstopstatus(df,i):
    stopstatus = df["MonitoredVehicleJourney"][i]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
    if stopstatus <> "":
        return stopstatus
    else:
        return "N/A"

def getresult(df):
    res = {"Latitude":[],
           "Longitude":[],
           "Stop Name":[],
            "Stop Status":[]}
    for i in range(len(df)):
        res["Latitude"].append(getlat(df,i))
        res["Longitude"].append(getlong(df,i))
        res["Stop Name"].append(getstopname(df,i))
        res["Stop Status"].append(getstopstatus(df,i))
    res = pd.DataFrame(res, columns = ["Latitude","Longitude","Stop Name","Stop Status"])
    return res

if __name__ == '__main__':
    main()
