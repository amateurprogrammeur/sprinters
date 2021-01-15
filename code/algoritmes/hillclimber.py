from code.classes.traject import Traject
from code.classes.map import Map
from code.classes.station import Station
from .random_1 import random_1

import copy
import random

class Hillclimber():

    def __init__(self, stations, initial_map, max_trajects, max_time):

        # dict { station_name : station_object }
        self.station_tree = stations

        # list [ traject_object ]
        self.trajects = initial_map.get_trajects()
        self.solution = int(initial_map.get_K())

        self.max_trajects = max_trajects
        self.max_time = max_time

        pass

    def mutate_traject(self):

        random = random_1(self.station_tree, self.max_trajects, self.max_time)
        new_traject = random.make_random_traject()

        return new_traject

    def delete_traject(self):
        pass

    def mutate(self):

        for i in range(self.max_trajects):
            old_traject = self.trajects[i]

            self.trajects[i] = self.mutate_traject()

            new_solution = self.check_solution()

            if new_solution > self.solution:
                self.solution = new_solution

                print(f"Hillclimber: highest_K {new_solution}")
            else:
                self.trajects[i] = old_traject
                continue
        return True

    def check_solution(self):

        new_map = Map(self.station_tree)
        for traject in self.trajects:
            new_map.add_traject(traject)

        return new_map.get_K()

    def run(self, iterations):
        # for traject in self.trajects:
        #     print(f"before mutate: {traject.get_stations()}")

        for i in range(iterations):
            self.mutate()

        # for traject in self.trajects:
        #     print(f"after mutate: {traject.get_stations()}")

        new_map = Map(self.station_tree)
        for traject in self.trajects:
            new_map.add_traject(traject)

        return new_map

pass

# PSEUDOCODE
# kies random state
# herhaal tot na x keer geen verbetering te zien:
    # muteer
    # if beter dan vorige staat
        # state = nieuwe state
    # else (if slechter)
        # ga terug naar vorige state


# class HillClimber(self):
#     """
#     The HillClimber class that changes a random node in the graph to a random valid value. Each improvement or
#     equivalent solution is kept for the next iteration.
#     """
#     def __init__(self, graph, transmitters):
#         if not graph.is_solution():
#             raise Exception("HillClimber requires a complete solution.")

#         self.graph = copy.deepcopy(graph)
#         self.value = graph.calculate_value()

#         self.transmitters = transmitters

#     def mutate_single_node(self, new_graph):
#         """
#         Changes the value of a random node with a random valid value.
#         """
#         random_node = random.choice(list(new_graph.nodes.values()))
#         available_transmitters = random_node.get_possibilities(self.transmitters)
#         random_reconfigure_node(new_graph, random_node, available_transmitters)

#     def mutate_graph(self, new_graph, number_of_nodes=1):
#         """
#         Changes the value of a number of nodes with a random valid value.
#         """
#         for _ in range(number_of_nodes):
#             self.mutate_single_node(new_graph)

#     def check_solution(self, new_graph):
#         """
#         Checks and accepts better solutions than the current solution.
#         """
#         new_value = new_graph.calculate_value()
#         old_value = self.value

#         # We are looking for maps that cost less!
#         if new_value <= old_value:
#             self.graph = new_graph
#             self.value = new_value

#     def run(self, iterations, verbose=False, mutate_nodes_number=1):
#         """
#         Runs the hillclimber algorithm for a specific amount of iterations.
#         """
#         self.iterations = iterations

#         for iteration in range(iterations):
#             # Nice trick to only print if variable is set to True
#             print(f'Iteration {iteration}/{iterations}, current value: {self.value}') if verbose else None

#             # Create a copy of the graph to simulate the change
#             new_graph = copy.deepcopy(self.graph)

#             self.mutate_graph(new_graph, number_of_nodes=mutate_nodes_number)

#             # Accept it if it is better
#             self.check_solution(new_graph)