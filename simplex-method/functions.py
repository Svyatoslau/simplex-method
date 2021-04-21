from data import *

def checkData():
    if countClusters<=0 or countStations<=0 or totalVolume<=0:
        print("Number shoud be greater then zero")
        raise SystemExit
    for x in clastorsRestrictions:
        if x<=0:
            print("Clastor can't be negative or zero")
            raise SystemExit
    for x in processingTimes:
        if x<=0:
            print("Processing times can't be negative or zero")
            raise SystemExit
    for x in stationRestrictions:
        if x<=0:
            print("Station restrictions can't be negative or zero")
            raise SystemExit
    if countClusters!=clastorsRestrictions.shape[0] or countClusters!=stationsInClastors.shape[0]:
        print("Incorrect information clastors")
        raise SystemExit
    if countStations!=processingTimes.shape[0] or countStations!=stationRestrictions.shape[0]:
        print("Incorrect information station")
        raise SystemExit
    