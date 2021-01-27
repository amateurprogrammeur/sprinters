# Celine Diks, Chris Bernsen & Julia Ham

# classes
from code.classes.traject import Traject
from code.classes.map import Map
from code.classes.station import Station
from .random import Random

# libraries
import copy
import random

class Hillclimber():
    """
    Class for Hill Climber algorithm.
    """

    def __init__(self, stations, initial_map, max_trajects, max_time):

        # dict { station_name : station_object }
        self.station_tree = stations

        # list [ traject_object ]
        self.trajects = initial_map.get_trajects()
        self.solution = int(initial_map.get_K())

        self.max_trajects = max_trajects
        self.max_time = max_time


    def new_random_traject(self):
        """
        Creates a random traject according to random algorithm
        """

        # creates new random traject
        random = Random(self.station_tree, self.max_trajects, self.max_time)
        new_traject = random.make_random_traject()

        return new_traject


    def delete_traject(self):
        """
        Deletes whole traject if K value is higher in that case.
        """

        # iterates over all trajects
        for i in range(len(self.trajects)-1):
            old_traject = self.trajects.pop(0)

            new_solution = self.check_solution()

            # checks and shows highest k value
            if new_solution > self.solution:
                self.solution = new_solution
                print(f"Hillclimber: highest_K {new_solution}")
            
            # adds old traject again if k value did not increase
            else:
                self.trajects.append(old_traject)


    def mutate(self):
        """
        Mutates a traject and checks if K value increases.
        """
        # iterates over all trajects
        for i in range(len(self.trajects)-1):
            old_traject = self.trajects[i]

            self.trajects[i] = self.new_random_traject()

            new_solution = self.check_solution()

            # checks and shows highest k value
            if new_solution > self.solution:
                self.solution = new_solution

                print(f"Hillclimber: highest_K {new_solution}")

            # adds old traject again if k value did not increase
            else:
                self.trajects[i] = old_traject


    def check_solution(self):
        """
        Checks if K value is higher with new traject list.
        Returns the map with the highest K value.
        """
        new_map = Map(self.station_tree)
        new_map.add_traject_list(self.trajects)

        return new_map.get_K()


    def run(self, iterations):
        """
        Runs the Hill Climber algorithm as many times as the user wants.
        Expects an integer as iterations.
        Returns a map as visualisation.
        """

        # runs hillclimber by mutating trajects if needed
        for i in range(iterations):
            self.delete_traject()
            self.mutate()

        # adds traject to new map visualisation
        new_map = Map(self.station_tree)
        for traject in self.trajects:
            new_map.add_traject(traject)

        return new_map