from code.classes.station import Station
from code.classes.traject import Traject
from code.classes.map import Map
from code.algoritmes.algorithm0 import *

from csv import reader
import csv

def load(level):

    # defines files corresponding with level
    if level == "HL":
        f1 = 'data/ConnectiesHolland.csv'
        f2 = 'data/StationsHolland.csv'

    elif level == "NL":
        f1 = 'data/ConnectiesNationaal.csv'
        f2 = 'data/StationsNationaal.csv'
        
    else:
        return False

    # dictionary {station name : station object}
    load.stations = {}

    # opens csv file, creates station objects and adds connections to stations
    with open(f1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:

            # skips the header
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1

                station_1 = row[0]
                station_2 = row[1]
                time = row[2]

                # creates new station object if station of this name does not already exist
                if station_1 not in load.stations:
                    new_station = Station(station_1)
                    load.stations[station_1] = new_station
                
                if station_2 not in load.stations:
                    new_station = Station(station_2)
                    load.stations[station_2] = new_station

                # adds connection to both stations
                station_1 = load.stations[station_1]
                station_1.add_connection(station_2, time)
                
                station_2 = load.stations[station_2]
                station_2.add_connection(station_1, time)

    # opens csv file, loads station object and adds coordinates to station
    with open(f2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # skips header
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1

                # retrieves station and adds x,y coordinates
                station = load.stations[row[0]]
                station.add_coordinates(row[1], row[2])
                
                # print(f"{station} with coordinates {station.get_coordinates()}")
    # print(stations)    

    return True
   


if __name__ == '__main__':
    load("HL")

    new_map = Map(load.stations)

    new_map.visualise()

    # algorithm0(7)
    


