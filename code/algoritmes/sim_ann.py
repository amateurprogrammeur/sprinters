# Celine Diks, Chris Bernsen & Julia Ham

# classes
from code.classes.traject import Traject
from code.classes.map import Map
from code.classes.station import Station
from .random_1 import Random_1

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
        self.solution = int(initial_map.get_K())

        self.max_trajects = max_trajects
        self.max_time = max_time

        self.data_list = []
        self.chances_list = []

        self.highest_map = Map(self.station_tree)
        self.highest_solution = 0
        pass

    def mutate_traject(self):
        """
        Deletes traject when K value is higher in that case.
        Creates a new traject object.
        Returns the updates traject object.
        """
        
        # creates new random traject
        random = Random_1(self.station_tree, self.max_trajects, self.max_time)
        new_traject = random.make_random_traject()

        return new_traject

    def delete_traject(self, temperature):
        """
        Deletes whole traject if K value is higher in new solution
        Returns Boolean True if succesfull.
        """

        # iterates over all trajects
        for i in range(len(self.trajects)-1):
            old_traject = self.trajects.pop(0)

            new_solution = self.check_solution()

            if new_solution > self.solution:
                self.solution = new_solution
            else:
                chance =  np.exp(-(self.solution - new_solution) / temperature)
                # print(f"delete_chance: {chance}, old_solution: {self.solution}, new_solution {new_solution}, temperature: {temperature}")

                if random.random() < chance:
                    # print(f"delete_chance: {chance}, old_solution: {self.solution}, new_solution {new_solution}")
                    self.solution = new_solution
                    # print(f"Simulated Annealing: new_K {new_solution}")
                
                # adds old traject again if k value did not increase
                else:
                    self.trajects.append(old_traject)
        return True

    def add_traject(self, temperature):
        trajects_amount = len(self.trajects)
        
        for i in range(trajects_amount):
            if trajects_amount < 20:
                new_traject = self.mutate_traject()
                self.trajects.append(new_traject)

                new_solution = self.check_solution()

                if new_solution > self.solution:
                    self.solution = new_solution
                else:
                    chance =  np.exp(-(self.solution - new_solution) / temperature)
                    if random.random() < chance:
                        # print(f"add_chance: {chance}, old_solution: {self.solution}, new_solution {new_solution}")
                        self.solution = new_solution
                        # print(f"Simulated Annealing: new_K {new_solution}")
                    
                    # adds old traject again if k value did not increase
                    else:
                        self.trajects.pop()

        return True


    def mutate(self, temperature):
        """
        Mutates a traject and checks if K value increases.
        Returns True if succesfull.
        """

        # iterates over all trajects
        for i in range(len(self.trajects)-1):
            old_traject = self.trajects[i]

            self.trajects[i] = self.mutate_traject()

            new_solution = self.check_solution()
            # print(f"old_solution: {self.solution}, new_solution {new_solution}")


            # if solution is better: always accept
            # if solution is worse: calculate chance to accept or decline

            if new_solution > self.solution:
                self.solution = new_solution
            else:
                # checks and shows highest k value
                chance =  np.exp(-(self.solution - new_solution) / temperature)
                # print(f"mutate_chance: {chance}, old_solution: {self.solution}, new_solution {new_solution}, temperature {temperature}")

                # self.chances_list.append(chance)
                # print(chance)
                if random.random() < chance:
                    # print(f"mutate_chance: {chance}, old_solution: {self.solution}, new_solution {new_solution}")
                    self.solution = new_solution

                # adds old traject again if k value did not increase
                else:
                    self.trajects[i] = old_traject

            # print(f"Simulated Annealing: new_K {new_solution}")

            # self.data_list.append(new_solution)
        return True

    def check_solution(self):
        """
        Checks if K value is higher with new traject list.
        Returns the map with the highest K value.
        """
        new_map = Map(self.station_tree)
        new_map.add_traject_list(self.trajects)
        new_K = new_map.get_K()

        if new_K > self.highest_solution:
            self.highest_map = copy.deepcopy(new_map)
            self.highest_solution = new_K
            print(f"Highest_K: {self.highest_solution}")

        return new_K

    def run(self, iterations):
        """
        Runs the Hill Climber algorithm as many times as the user wants.
        Expects an integer as iterations.
        Returns a map as visualisation.
        """

        max_temperature = 250

        # runs simulated annealing by mutating trajects if needed
        for i in range(iterations):
            # straight line
            temperature = max_temperature - (( max_temperature / iterations) * i)
            # print(temperature)
            # temperature = temperature * 0.95

            self.delete_traject(temperature)
            self.mutate(temperature)
            self.add_traject(temperature)

        # adds traject to new map visualisation
        # new_map = Map(self.station_tree)
        # new_map.add_traject_list(self.trajects)

        self.check_solution()

        print(f"{self.highest_map.get_trajects()} Final K: {self.highest_map.get_K()}")

        # for traject in self.trajects:
        #     new_map.add_traject(traject)

        # x = list(range(0,iterations))
        # y = self.data_list

        # plt.plot(x, y, 'o', color='black')
        # plt.show

        # x = list(range(0,iterations))
        # y = self.chances_list

        # plt.plot(x, y, 'o', color='black')
        # plt.show

        return self.highest_map

#Herhaal:
    #Kies een random start state
    #Kies start waarde
    #Herhaal N iteraties: 
        #Doe een kleine random aanpassing
        #Als random( ) > kans(oud, nieuw, waarde): 
            #Maak de aanpassing ongedaan
        #Verlaag waarde


# Kans 2^(oude score - nieuwe score)/temperatuur