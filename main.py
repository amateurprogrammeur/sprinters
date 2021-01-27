############################################################################
# Celine Diks, Chris Bernsen & Julia Ham
# Minor Programming - Programmeer theorie - RailNL
# main.py
#
# Manages and runs algorithms and saves output
#
############################################################################

# classes
from code.classes.station import Station
from code.classes.traject import Traject
from code.classes.map import Map

# algorithms
from code.algoritmes.random import Random
from code.algoritmes.prims import Prims
from code.algoritmes.kruskals import Kruskals
from code.algoritmes.hillclimber import Hillclimber
from code.algoritmes.depth_first import DepthFirst
from code.algoritmes.sim_ann import Sim_Ann
from code.algoritmes.chance import Chance

# libraries
from csv import reader
import csv

# misc
from code.constants import *
from load import load
from load_advanced import load_advanced

   
def main():
    """
    Checks which level and which algorithm the user wants to run.
    Checks how many times the user wants to run the algorithm.
    Runs the desired algorithm as many times as the user wants.
    """
    
    # chooses level and changes variables accordingly
    level = ""
    while level != "NL" and level != "HL" and level != "AD":

        # asks which level to load
        level = input("Holland (HL) or Netherlands (NL) or Advanced (AD)? \n")
        level = level.upper()

        # loads stations corresponding to level
        if level == "NL":
            stations = load(level)

            trajects = NL_TRAJECT_LIMIT
            time = LONG_TRAJECT
            prim_algorithm = ""

        elif level == "HL":
            stations = load(level)

            trajects = HL_TRAJECT_LIMIT
            time = SHORT_TRAJECT
            prim_algorithm = ""

        elif level == "AD":
            stations = False
            while stations == False:
                station_name = input("Remove a station [station name] or three random connections [connections] \n")
                stations = load_advanced(station_name)

            trajects = NL_TRAJECT_LIMIT
            time = LONG_TRAJECT

            # prevents being asked to run prims
            prim_algorithm = "n"

    tree = stations
    # applies prims algorithm to connection tree when asked
    while prim_algorithm != "y" and prim_algorithm != "n":

        prim_algorithm = input("Use Prim's algorithm [y/n]? \n")

        if prim_algorithm == "y":
            tree = Prims(stations).make_tree()

    # runs the desired algorithm
    first_algorithm = ""
    while first_algorithm != "random" and first_algorithm != "chance":

        # asks which algorithm to run
        first_algorithm = input("Choose first algorithm: [Random] or [Chance]? \n")
        first_algorithm = first_algorithm.lower()

        if first_algorithm == "random":
            first_algorithm_class = Random(tree, trajects, time)

        elif first_algorithm == "chance":
            first_algorithm_class = Chance(tree, trajects, time)


    # runs algorithm as many times as user asks for 
    first_iterations = 0
    while first_iterations < 1:

        # asks how many times to run algorithm
        first_iterations = int(input("How many iterations [integer]? \n"))
        
        new_K = 0
        highest_K = 0
        lowest_K = 99999

        for i in range(first_iterations):

            # runs algorithm class object
            result_map = first_algorithm_class.run()
            new_K = result_map.get_K()

            # checks for new higher k value
            if new_K > highest_K:
                highest_K = new_K
                highest_map = result_map
                print(f"Highest K: {highest_K}")

            # checks for new lower k value
            elif new_K < lowest_K:
                lowest_K = new_K
                lowest_map = result_map

        # saves and visualises highest_K output
        print(f"{first_algorithm}: Highest_K: {highest_K}")
        highest_map.save_map(f"{level}_{prim_algorithm}ayPrims_{first_algorithm}_{first_iterations}_Highest_K")
        highest_map.visualise_trajects(f"{level}_{prim_algorithm}ayPrims_{first_algorithm}_{first_iterations}_Trajects")
                
    # applies second algorithm if asked for
    second_algorithm = ""
    while second_algorithm != "HC" and second_algorithm != "SA" and second_algorithm != "N":

        # asks whether to use what second algorithm to run
        second_algorithm = input("Apply hillclimber [HC], Simulated Annealing [SA] or None [N]? \n")
        second_algorithm = second_algorithm.upper()

        if second_algorithm == "N":
            return True

        elif second_algorithm == "HC":
            second_algorithm_class = Hillclimber(tree, highest_map, trajects, time)

        elif second_algorithm == "SA":
            second_algorithm_class = Sim_Ann(tree, highest_map, trajects, time)

    # runs hillclimber as many times as user asks for
    second_iterations = 0
    while second_iterations < 1:

        # asks how often to run hillclimber
        second_iterations = int(input("How many iterations? \n"))

        result_map = second_algorithm_class.run(second_iterations)

        # saves and visualises highest_K output
        result_map.save_map(f"{level}_{prim_algorithm}ayPrims_{first_algorithm}_{first_iterations}_{second_algorithm}_{second_iterations}_Highest_K")
        result_map.visualise_trajects(f"{level}_{prim_algorithm}ayPrims_{first_algorithm}_{first_iterations}_{second_algorithm}_{second_iterations}_Trajects")


if __name__ == '__main__':

    main()   