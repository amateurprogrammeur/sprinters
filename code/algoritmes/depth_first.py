#########################################################
# Celine Diks, Chris Bernsen & Julia Ham
#
# Tried algorithm depth first but not succeeded. 
######################################################### 


# classes
from code.classes.traject import Traject
from code.classes.map import Map
from code.classes.station import Station

# libraries
import copy
import random

"""
Doodlopende_stations: [ station_object ]
depth = x
voor elk station
	pak connecties
	kies station met 1 connectie (len(connections) == 1)
	voeg toe aan lijst doodlopende stations


while len(doodlopende_stations) > 0:
begin_station = pop station uit lijst doodlopende_stations
new_traject = Traject
voeg begin_station toe aan new_traject
if depth < 3 (getal kan veranderen)
	for connection in connections
		child_traject = deepcopy new_traject
		if child_traject < 3 uur
			voeg connectie toe aan child_traject
		voeg child to aan map
		bereken K waarde
		if hoogste K waarde
			sla child_traject op als beste_child
		delete child van map (moeten we nieuwe map functie voor schrijven)
sla beste_child op in map
als stations in beste_child in doodlopende_stations zit, haal dit station eruit
depth ++


for station in doodlopende_stations:
	pas depthfirst toe 
	met depth = 3 
	sla op in new_traject
"""

class DepthFirst():

    def __init__(self, stations, max_trajects, max_time):

        # dict { station_name : station_object }
        self.station_tree = stations

        self.max_trajects = max_trajects
        self.max_time = max_time
        pass

    def deadend_stations(self):

        deadend_stations = []

        for station in self.station_tree:
            station = self.station_tree[station]
            connections = station.get_connections()
            if len(connections) == 1:
                deadend_stations.append(station)

        return deadend_stations


    def depthfirst(self, depth, iterations):
        deadend_stations = self.deadend_stations()
        children = []
        test_map = Map(self.station_tree)
        visited = []
        best_children = []

        while len(deadend_stations) > 0:

            first_station = deadend_stations.pop(0)
            new_traject = Traject()
            new_traject.add_station(first_station, 0)
            children.append(new_traject)

            current_depth = 0
            highest_K = 0
            # while current_depth < depth:
            for i in range(iterations):
                for child_traject in children:
                    if current_depth < depth:
                        if child_traject.get_time() < self.max_time:
                            connections = child_traject.get_last_station().get_connections()
                            for connection in connections:
                                
                                # if connection.name not in visited:
                                time = connections[connection]

                                new_child_traject = copy.deepcopy(child_traject)
                                children.append(new_child_traject)
                                new_child_traject.add_station(connection, time)

                                # print(f"station {connection} added")

                                # if connection in deadend_stations:
                                #     deadend_stations.remove(connection)
                                #     print(f"REMOVED: {connection}")

                                test_map.add_traject(new_child_traject)
                                new_K = test_map.get_K()

                                if new_K > highest_K:
                                    highest_child_traject = new_child_traject
                                    highest_K = new_K

                                test_map.delete_last_traject()

                                    # visited.append(connection.name)

                            current_depth += 1
                        else:
                            continue
                    else:
                        children.clear()
        
                children.clear()
                test_map.add_traject(highest_child_traject)
                children.append(highest_child_traject)
        return test_map


    def run(self, depth, iterations):

        test_map = self.depthfirst(depth, iterations)
        return test_map