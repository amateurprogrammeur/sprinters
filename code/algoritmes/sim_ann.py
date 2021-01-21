# Celine Diks, Chris Bernsen & Julia Ham

# classes
from code.classes.traject import Traject
from code.classes.map import Map
from code.classes.station import Station
from .random_1 import random_1

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
        pass

    def mutate_traject(self):
        """
        Deletes traject when K value is higher in that case.
        Creates a new traject object.
        Returns the updates traject object.
        """
        
        # creates new random traject
        random = random_1(self.station_tree, self.max_trajects, self.max_time)
        new_traject = random.make_random_traject()

        return new_traject

    def delete_traject(self, temperature):
        """
        Deletes whole traject if K value is higher in that case.
        Returns Boolean True if succesfull.
        """

        # iterates over all trajects
        for i in range(len(self.trajects)-1):
            old_traject = self.trajects.pop(0)

            new_solution = self.check_solution()


            chance =  np.exp((-new_solution - self.solution) / temperature)
            if random.random() < chance:
                self.solution = new_solution
                # print(f"Simulated Annealing: new_K {new_solution}")
            
            # adds old traject again if k value did not increase
            else:
                self.trajects.append(old_traject)
                continue
        return True

    def add_traject(self, temperature):
        
        if len(self.trajects) < 20:
            new_traject = self.mutate_traject()
            self.trajects.append(new_traject)

            new_solution = self.check_solution()

            chance =  np.exp((-new_solution - self.solution) / temperature)
            if random.random() < chance:
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

            # checks and shows highest k value
            chance =  np.exp((new_solution - self.solution) / temperature)
            # print(chance)
            if random.random() < chance:
                self.solution = new_solution

            # adds old traject again if k value did not increase
            else:
                self.trajects[i] = old_traject
                continue

        print(f"Simulated Annealing: new_K {new_solution}")

        self.data_list.append(new_solution)
        return True

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

        temperature = 1000

        # runs hillclimber by mutating trajects if needed
        for i in range(iterations):
            # straight line
            # temperature = temperature - ((1000 / iterations) * i)
            temperature = temperature * 0.95

            self.delete_traject(temperature)
            self.mutate(temperature)
            self.add_traject(temperature)

        # adds traject to new map visualisation
        new_map = Map(self.station_tree)
        for traject in self.trajects:
            new_map.add_traject(traject)

        x = list(range(0,iterations))
        y = self.data_list

        

        plt.plot(x, y, 'o', color='black')
        plt.show

        return new_map

pass

#Herhaal:
    #Kies een random start state
    #Kies start waarde
    #Herhaal N iteraties: 
        #Doe een kleine random aanpassing
        #Als random( ) > kans(oud, nieuw, waarde): 
            #Maak de aanpassing ongedaan
        #Verlaag waarde


# Kans 2^(oude score - nieuwe score)/temperatuur