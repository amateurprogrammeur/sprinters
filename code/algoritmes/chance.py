# Celine Diks, Chris Bernsen & Julia Ham

from code.classes.traject import Traject
from code.classes.map import Map
import random

class Chance():
    """
    Takes a random station and creates a random traject.
    Expects stations, maximum amount of trajects and maximum amount of time.
    Returns a new map with created trajectories.
    """

    def __init__(self, stations, max_trajects, max_time):
        self.stations = stations
        self.max_trajects = max_trajects
        self.max_time = max_time


    def deadend_stations(self):
        """
        Makes list of all deadend stations out stations list.
        """

        deadend_stations = []

        for station in self.stations:
            station = self.stations[station]
            connections = station.get_connections()
            if len(connections) == 1:
                deadend_stations.append(station)

        return deadend_stations


    def make_chance_trajects(self):
        """
        Creates a traject object according to our chance algorithm and returns it.
        """

        deadend_stations = self.deadend_stations()
        connection_chance_list = []
        visited = []
        traject_list = []

        while len(deadend_stations) > 0:
            new_traject = Traject()

            # add random station to traject
            first_station = deadend_stations.pop()

            if first_station.name not in visited:
                new_traject.add_station(first_station, 0)
                visited.append(first_station.name)

                # check connections of station
                connections = first_station.get_connections()
            else:
                continue

            x = True
            while x == True:
                total_time_connections = sum(connections.values())
                for connection in connections:
                    connection_time = connections[connection]
                    connection_chance = 1 / (connection_time / total_time_connections)
                    if connection.name in visited:
                        connection_chance = connection_chance / 2
                    if connection_chance <= 0.0:
                        connection_chance = 1
                    connection_chance_list.append(connection_chance)
                
                station = random.choices(list(connections.keys()), weights=connection_chance_list, k=1)[0]

                connection_chance_list.clear()

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

                    visited.append(station.name)

                    if new_traject.get_time() > self.max_time:
                        x = False

            if new_traject.get_time() > self.max_time:
                new_traject.remove_station(last_station, last_time)

            traject_list.append(new_traject)

        return traject_list


    def run(self):
        """
        Runs the chance algorithm.
        Returns a map as visualisation.
        """

        new_map = Map(self.stations)

        trajects = self.make_chance_trajects()
        new_map.add_traject_list(trajects)

        return new_map