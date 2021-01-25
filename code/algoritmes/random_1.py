# Celine Diks, Chris Bernsen & Julia Ham

from code.classes.traject import Traject
from code.classes.map import Map
import random

class Random_1():
    """
    Takes a random station and creates a random traject.
    Expects stations, maximum amount of trajects and maximum amount of time.
    Returns a new map with created trajectories.
    """

    def __init__(self, stations, max_trajects, max_time):
        self.stations = stations
        self.max_trajects = max_trajects
        self.max_time = max_time

        pass


    def make_random_traject(self):
        """
        Creates a random traject object and returns it.
        """

        new_traject = Traject()
        
        # add random station to traject
        random_station = random.choice(list(self.stations.values()))

        new_traject.add_station(random_station, 0)

        # check connections of station
        connections = random_station.get_connections()

        x = True
        while x == True:

            station = random.choice(list(connections.keys()))

            # checks if all connections are already in traject
            if new_traject.has_station(station):
                list_1 = list(connections.keys())
                list_2 = new_traject.get_stations()

                check = all(item in list_2 for item in list_1)

                if check:
                    if random.random() < 0.50:
                        x = False
                else:
                    continue
            else:
                
                # add connection with station and time as traject to new_traject
                time = connections[station]
                last_station = station
                last_time = connections[station]
                connections = last_station.get_connections()
                new_traject.add_station(station, time)

                if new_traject.get_time() > self.max_time:
                    x = False

        if new_traject.get_time() > self.max_time:
            new_traject.remove_station(last_station, last_time)

        return new_traject


    def run(self):
        """
        Runs the random algorithm.
        Returns a map as visualisation.
        """
        
        new_map = Map(self.stations)

        # adds new_traject to new_map untill maximum is reached
        for i in range(self.max_trajects):
            new_traject = self.make_random_traject()
            new_map.add_traject(new_traject)

        return new_map

































































































































































































































































































































































































































































































