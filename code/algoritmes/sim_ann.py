# Celine Diks, Chris Bernsen & Julia Ham

# classes
from code.classes.traject import Traject
from code.classes.map import Map
from code.classes.station import Station
from .random import Random

# libraries
import copy
import random
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

class Sim_Ann():
    """
    Class for Hill Climber algorithm.
    """

    def __init__(self, stations, initial_map, max_trajects, max_time):

        # dict { station_name : station_object }
        self.station_tree = stations

        # list [ traject_object ]
        self.trajects = initial_map.get_trajects()

        self.old_solution = int(initial_map.get_K())

        self.max_trajects = max_trajects
        self.max_time = max_time

        self.highest_map = Map(self.station_tree)
        self.highest_solution = 0


    def new_random_traject(self):
        """
        Creates a new traject object according to random_1 algorithm
        Returns traject object.
        """
        
        # creates new random traject
        random = Random(self.station_tree, self.max_trajects, self.max_time)
        new_traject = random.make_random_traject()

        return new_traject

    def delete_traject(self, temperature):
        """
        Deletes all trajects one by one
        Checks solution and accepts change or not
        """
        # iterates over all trajects
        for i in range(len(self.trajects)-1):
            # deletes a traject
            old_traject = self.trajects.pop(0)

            # checks if change should be accepted and reverts when needed
            accept = self.check_solution(temperature)
            if not accept:
                self.trajects.append(old_traject)


    def add_traject(self, temperature):
        """
        Adds trajects
        Checks solution and accepts change or not
        """
        trajects_amount = self.max_trajects - len(self.trajects)
        
        # makes trajects until total equals max trajects
        for i in range(trajects_amount - 1):

            # creates new traject and adds to trajects list
            new_traject = self.new_random_traject()
            self.trajects.append(new_traject)

            # checks if change should be accepted and reverts when needed
            accept = self.check_solution(temperature)
            if not accept:
                    self.trajects.pop()


    def mutate(self, temperature):
        """
        Mutates all trajects one by one
        Checks solution and accepts change or not
        """
        # iterates over all trajects
        for i in range(len(self.trajects) - 1):
            # saves original traject
            old_traject = self.trajects[i]

            # mutates traject
            self.trajects[i] = self.new_random_traject()

            # checks if change should be accepted and reverts when needed
            accept = self.check_solution(temperature)
            if accept == False:
                self.trajects[i] = old_traject


    def check_solution(self, temperature):
        """
        Checks if K value is higher with new traject list.
        Returns Boolean True if chance is met.
        """
        
        # creates empty map, adds traject list to map, calculates K value
        new_map = Map(self.station_tree)
        new_map.add_traject_list(self.trajects)
        new_solution = new_map.get_K()

        # saves the highest solution
        if new_solution > self.highest_solution:
            self.highest_map = copy.deepcopy(new_map)
            self.highest_solution = new_solution
            print(f"Highest_K: {self.highest_solution}")

        # accept change if solution is higher
        if new_solution > self.old_solution:
            self.old_solution = new_solution
            return True

        # calculate chance to accept wrong solution
        chance =  np.exp( - (self.old_solution - new_solution) / temperature)

        # returns true if chance is met, false if not
        if random.random() < chance:
            self.old_solution = new_solution
            return True

        return False


    def run(self, iterations):
        """
        Runs the Hill Climber algorithm as many times as the user wants.
        Expects an integer as iterations.
        Returns a map with highest K value as visualisation.
        """

        max_temperature = 250

        # runs simulated annealing by mutating trajects if needed
        for i in range(iterations):

            # calculates temperature
            temperature = max_temperature - (( max_temperature / iterations) * i)

            # does all mutations with temperature in one iteration
            self.delete_traject(temperature)
            self.mutate(temperature)
            self.add_traject(temperature)

        # check solution is called one last time in case mutations are made after check solution is called in previous functions
        self.check_solution(temperature)

        return self.highest_map
