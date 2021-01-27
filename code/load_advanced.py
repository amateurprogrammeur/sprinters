################################################################################
# Celine Diks, Chris Bernsen & Julia Ham
# Minor Programming - Programmeer theorie - RailNL
# advanced.py
#
# Loads csv data into station class objects
# Adds connections and coordinates
# For Advanced assignment
################################################################################

# classes
from code.classes.station import Station
from code.classes.traject import Traject
from code.classes.map import Map

# libraries
from csv import reader
import csv
import random

# misc
from code.constants import *


def load_advanced(command):
    """
    Checks which station user does not want to load.
    Only loads the remaining stations.
    Returns a list of loaded stations
    """

    # defines files
    f1 = 'data/ConnectiesNationaal.csv'
    f2 = 'data/StationsNationaal.csv'

    # dictionary {station name : station object}
    load_advanced.stations = {}
    all_stations = []

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

                new_station_name = row[0]

                all_stations.append(new_station_name)

                # retrieves station and adds x,y coordinates
                if row[0] != command:

                    new_station = Station(new_station_name)
                    load_advanced.stations[new_station_name] = new_station

                    new_station.add_coordinates(row[1], row[2])

    # when these conditions are met, the wrong command was typed
    if command not in all_stations and command != "connections":
        return False


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

                if station_1 != command and station_2 != command:

                    station_1 = load_advanced.stations[station_1]
                    station_2 = load_advanced.stations[station_2]

                    station_1.add_connection(station_2, time)
                    station_2.add_connection(station_1, time)

    # choose three random stations from station list and delete connection of station 
    if command == "connections":
        for i in range(3):
            random_station_1 = random.choice(list(load_advanced.stations.values()))
            random_station_2 = random.choice(list(random_station_1.connections.keys()))

            random_station_1.remove_connection(random_station_2)
            random_station_2.remove_connection(random_station_1)

    return load_advanced.stations