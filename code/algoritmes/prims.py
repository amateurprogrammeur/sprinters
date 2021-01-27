# Celine Diks, Chris Bernsen & Julia Ham

from code.classes.traject import Traject
from code.classes.map import Map
from code.classes.station import Station

import random
import operator

class Prims():
    """
    Algorithm that creates a tree with shortest connections.
    Returns the created tree.
    """

    def __init__(self, stations):

        # dict { station_name : station_object }
        self.stations = stations
        self.prims_tree = {}

    def make_tree(self):
        """
        Creates tree with shortest connections.
        Returns dictionary as the created tree.
        """

        # list [station_name]
        visited = []

        # creates empty station object for each station and adds coordinates
        for station in self.stations:
            new_station = Station(station)
            coordinates = self.stations[station].get_coordinates()
            new_station.add_coordinates(coordinates[0], coordinates[1])

            # saves station in prims_tree dictionary
            self.prims_tree[station] = new_station

        # choose random beginning station
        random_station = random.choice(list(self.stations.values()))

        # sort station connections and retrieve shortest
        station_connections = random_station.get_connections()
        station_connections = sorted(station_connections.items(), key=operator.itemgetter(1))
        new_connection = station_connections.pop(0)
        new_station = new_connection[0]
        new_time = new_connection[1]

        # retrieve empty stations from prims_tree dictionary
        first_station = self.prims_tree[random_station.name]
        new_station = self.prims_tree[new_station.name]

        # add shortest connection to stations
        first_station.add_connection(new_station, new_time)
        new_station.add_connection(first_station, new_time)

        # add stations to visited
        visited.append(first_station.name)
        visited.append(new_station.name)

        # runs until all stations are visited
        while len(visited) is not len(self.prims_tree):
            # starts as arbitrarily high number
            min_connection_time = 9999

            # get connections of visited stations
            for station in visited:
                connections = self.stations[station].get_connections()

                # get time of connections
                for connection in connections:
                    connection_time = connections[connection]

                    # save smallest connection if time is smallest and station is not visited
                    if connection.name not in visited and connection_time < min_connection_time:
                        smallest_connection = self.prims_tree[connection.name]
                        smallest_connection_station = self.prims_tree[station]
                        min_connection_time = connection_time
                    else:
                        continue

            # add smallest connection to station in prims_tree dictionary
            smallest_connection_station.add_connection(smallest_connection, min_connection_time)
            smallest_connection.add_connection(smallest_connection_station, min_connection_time)

            # add new connection to visited list
            visited.append(smallest_connection.name)

        return self.prims_tree
