from code.classes.traject import Traject
from code.classes.map import Map
from code.classes.station import Station

import random
import operator

class prims():
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
        Creates tree with shortest connections and returns it.
        """

        # list [station_name]
        visited = []

        for station in self.stations:
            new_station = Station(station)
            coordinates = self.stations[station].get_coordinates()
            new_station.add_coordinates(coordinates[0], coordinates[1])

            self.prims_tree[station] = new_station

        # print(self.prims_tree)

        random_station = random.choice(list(self.stations.values()))

        visited.append(random_station.name)
        first_station = self.prims_tree[random_station.name]

        # print(f"begin_station: {random_station}")

        station_connections = random_station.get_connections()

        # print(f"unsorted connections: {station_connections}")
        station_connections = sorted(station_connections.items(), key=operator.itemgetter(1))
        # print(f"sorted connections: {station_connections}")

        new_connection = station_connections.pop(0)
        new_station = new_connection[0]
        new_time = new_connection[1]

        first_station.add_connection(new_station, new_time)
        new_station.add_connection(first_station, new_time)

        visited.append(new_station.name)

        # print(f"new connection: {first_station} linked to {new_station} time: {new_time}")

        while len(visited) is not len(self.prims_tree):
            min_connection_time = 999999
            # print(f"visted: {visited}")
            for station in visited:
                connections = self.stations[station].get_connections()
                for connection in connections:
                    connection_time = connections[connection]
                    if connection.name not in visited and connection_time < min_connection_time:
                        smallest_connection = self.prims_tree[connection.name]
                        smallest_connection_station = self.prims_tree[station]
                        min_connection_time = connection_time
                    else:
                        continue

            # print(f"new connection: {smallest_connection_station} linked to {smallest_connection} with time {min_connection_time}")
            smallest_connection_station.add_connection(smallest_connection, min_connection_time)
            smallest_connection.add_connection(smallest_connection_station, min_connection_time)

            visited.append(smallest_connection.name)

        # new_map = Map(self.prims_tree)
        # new_map.visualise("Prim_Tree_Test")

        return self.prims_tree



# kies een willekeurige knoop (1e bezochte knoop)
# kies de kant met de laagste waarde verbonden met deze knoop
# neem de knoop aan de andere zijde van de kant op in je verzameling met bezochte knopen
# kies de kant met de laagste waarde vanuit je verzameling bezochte knopen naar een knoop die nog niet bezocht werd, en voeg deze kant aan de minimaal opspannende boom toe
# neem de nieuwe bereikte knoop op in je verzameling
# ga door tot alle knopen van de graaf bezocht zijn.

### PSEUDOCODE:

# maak tree lijst
# kies random station (Run meerdere keren met ander begin station)
# voeg station toe aan visited lijst
# check connecties van station
# sorteer connecties van laag naar hoog
# kies de kortste
# voeg station toe aan visited lijst

# while len.stations is not len.visited lijst
    # voeg connecties van alle stations in visited lijst toe aan connecties lijst
    # sorteer connecties van laag naar hoog
    # for connectie in connecties
    #       if connectie not in visited lijst
    #           voeg toe aan station
    #           continue
    #       else
    #           continue

## PSEUDOCODE 2:

# Maak lege stations en sla op in prims_tree dictionary
# Kies random station
# Haal connecties op van random station
# Sorteer connecties van laag naar hoog
# Voeg kortste connectie toe aan leeg station

# while len.stations is not len.prims_tree
    # min_connection_time = 999999
    # for station in prims_tree
        # connections = station.get_connections
        # for connection in connections
            # if connection not in prims_tree:
                # if connections[connection] < min_connection_time
                    # smallest_connection = connection
                    # smallest_connection_station = station
                    # min_connection_time = connections[connection]
            # else:
                # continue

    # station.add_connection(connection, min_connection_time)
    # connection.add_connection(station, min_connection_time)
