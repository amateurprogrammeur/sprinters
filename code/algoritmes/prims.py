from code.classes.traject import Traject
from code.classes.map import Map
from code.classes.station import Station

import random
import operator

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

# Maak lege stations en sla op in station_tree dictionary
# Kies random station
# Haal connecties op van random station
# Sorteer connecties van laag naar hoog
# Voeg kortste connectie toe aan leeg station

# while len.stations is not len.station_tree
    # min_connection_time = 999999
    # for station in station_tree
        # connections = station.get_connections
        # for connection in connections
            # if connection not in station_tree:
                # if connections[connection] < min_connection_time
                    # smallest_connection = connection
                    # smallest_connection_station = station
                    # min_connection_time = connections[connection]
            # else:
                # continue

    # station.add_connection(connection, min_connection_time)
    # connection.add_connection(station, min_connection_time)



def prims(stations):

    # dict { name : station_object }
    station_tree = {}

    visited = []

    for station in stations:
        new_station = Station(station)
        coordinates = stations[station].get_coordinates()
        new_station.add_coordinates(coordinates[0], coordinates[1])

        station_tree[station] = new_station

    # print(station_tree)

    random_station = random.choice(list(stations.values()))

    visited.append(random_station.name)
    first_station = station_tree[random_station.name]

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

    while len(visited) is not len(station_tree):
        min_connection_time = 999999
        # print(f"visted: {visited}")
        for station in visited:
            connections = stations[station].get_connections()
            for connection in connections:
                connection_time = connections[connection]
                if connection.name not in visited and connection_time < min_connection_time:
                    smallest_connection = station_tree[connection.name]
                    smallest_connection_station = station_tree[station]
                    min_connection_time = connection_time
                else:
                    continue

        # print(f"new connection: {smallest_connection_station} linked to {smallest_connection} with time {min_connection_time}")
        smallest_connection_station.add_connection(smallest_connection, min_connection_time)
        smallest_connection.add_connection(smallest_connection_station, min_connection_time)

        visited.append(smallest_connection.name)

    # new_map = Map(station_tree)
    # new_map.visualise("Prim_Tree_Test")

    return station_tree
