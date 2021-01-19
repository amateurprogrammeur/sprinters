from code.classes.traject import Traject
from code.classes.map import Map
from code.classes.station import Station

import random
import operator


class kruskals():
    """
    Class for Kruskals algorithm.
    """
    def __init__(self, stations):
        
        # dict { station_name : station_object }
        self.stations = stations
        self.kruskals_tree = {}

    def make_tree(self):
        """
        Creates a tree with station objects to choose from.
        Returns a dictionary as the tree.
        """
        # list [ station_name ]
        visited = []

        # {(station1, station2) : time}
        all_connections = {}

        for station in self.stations:
            if station not in visited:
                connections = self.stations[station].get_connections()
                for connection in connections:
                    connection_time = connections[connection]
                    all_connections[(self.stations[station].name, connection.name)] = connection_time
                    visited.append(connection.name)


            new_station = Station(station)
            coordinates = self.stations[station].get_coordinates()
            new_station.add_coordinates(coordinates[0], coordinates[1])
            self.kruskals_tree[station] = new_station

        all_connections = dict(sorted(all_connections.items(), key=operator.itemgetter(1)))

        visited.clear()

        while len(visited) is not len(self.kruskals_tree):

            min_connection_time = 9999

            for connection in all_connections:
                station_name = connection[0]
                connection_name = connection[1]
                connection_time = all_connections[connection]

                if connection_time < min_connection_time and (station_name not in visited or connection_name not in visited):
                    smallest_connection = self.kruskals_tree[connection_name]
                    smallest_connection_station = self.kruskals_tree[station_name]
                    min_connection_time = connection_time

            print(min_connection_time)
            smallest_connection_station.add_connection(smallest_connection, min_connection_time)
            smallest_connection.add_connection(smallest_connection_station, min_connection_time)

            if smallest_connection_station.name not in visited:
                visited.append(smallest_connection_station.name)
            if smallest_connection.name not in visited:
                visited.append(smallest_connection.name)

        new_map = Map(self.kruskals_tree)
        new_map.visualise("Kruskals_Tree_Test")

        return self.kruskals_tree