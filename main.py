from code.classes.map import Map
from code.classes.station import Station
from code.classes.traject import Traject
from code.algoritmes.algorithm0 import *

from csv import reader
import csv

def load():
    
    stations = {}
    f1 = 'data/ConnectiesHolland.csv'
    f2 = 'data/StationsHolland.csv'

    #loads stations and add connections to station objects
    with open(f1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1

                station_1 = row[0]
                station_2 = row[1]
                time = row[2]

                if station_1 not in stations:
                    new_station = Station(station_1)
                    stations[station_1] = new_station
                
                if station_2 not in stations:
                    new_station = Station(station_2)
                    stations[station_2] = new_station


                station_1 = stations[station_1]
                station_1.add_connection(station_2, time)
                
                station_2 = stations[station_2]
                station_2.add_connection(station_1, time)

    with open(f2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1

                station = stations[row[0]]
                station.add_coordinates(row[1], row[2])
                
                # print(f"{station} with coordinates {station.get_coordinates()}")
    # print(stations)    

    return True
   


if __name__ == '__main__':
    load()
    algorithm0(7)
    


