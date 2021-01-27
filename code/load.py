#########################################################
# Celine Diks, Chris Bernsen & Julia Ham
# Minor Programming - Programmeer theorie - RailNL
# load.py
#
# Loads csv data into station class objects
# Adds connections and coordinates
# For main assignment
#########################################################

# classes
from code.classes.station import Station
from code.classes.traject import Traject
from code.classes.map import Map

# libraries
from csv import reader
import csv

# misc
from code.constants import *


def load(level):
    """
    Checks if user wants to load HL or NL csv file.
    Loads all station data from the requested csv file.
    """
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

    # opens csv file, creates station object and adds coordinates to station
    with open(f2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # skips header
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1

                # creates station and adds x,y coordinates
                new_station = Station(row[0])
                load.stations[row[0]] = new_station
                new_station.add_coordinates(row[1], row[2])

    # opens csv file, loads station objects and adds connections to stations
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
                time = int(row[2])

                # creates connections between stations
                station_1 = load.stations[station_1]
                station_2 = load.stations[station_2]

                station_1.add_connection(station_2, time)
                station_2.add_connection(station_1, time)

    return load.stations