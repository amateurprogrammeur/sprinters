from code.classes.traject import Traject

import networkx as nx
from matplotlib import pyplot
import matplotlib.pyplot as plt

import os

class Map():

    def __init__(self, stations):
        self.trajects = []
        self.stations = stations
        self.counter = 0
        pass

    # adds traject object to trajects list
    def add_traject(self, traject):
        self.trajects.append(traject)
        return True
    
    # returns list of traject objects
    def get_trajects(self):
        return self.trajects

    # makes visualisations of trajects data
    def visualise(self):
        # make html file

        # for each station, make node with station.get_coordinates()

        # for each traject
        #       for each station
        #           create line between stations

        # matplotlib?

        # experimental code from stack overflow, not sure if this works yet
        G = nx.Graph()

        for key in self.stations:
            station = self.stations[key]
            
            station_coordinates = station.get_coordinates()

            G.add_node(station.name, pos=(station_coordinates[0], station_coordinates[1]))

            # G.add_edge_from(station1, station2)

        # pyplot.gca().invert_yaxis()
        # pyplot.gca().invert_xaxis()

        nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=1000, node_color='blue', font_size=8, font_weight='bold')

        # plt.tight_layout()

        plt.savefig(f'code/visualisatie/tests/Graph_{self.counter}.png', format="PNG")
        plt.show()

        self.counter += 1
        pass
    
    # calculates p value (ratio stations covered by trajects to total amount stations)
    def get_p(self):
        stations = []

        #save stations from trajects in stations list (runs 7x)
        for traject in self.trajects:
            traject_stations = traject.get_stations()
            stations.extend(traject_stations)

        #remove duplicates
        stations = list(dict.fromkeys(stations))

        p = len(stations) / len(self.stations)
        return p


    # calculates T value (total amount of trajects)
    def get_T(self):
        T = len(self.trajects)
        return T


    # calculates Min value (total amount of minutes of all trajects)
    def get_Min(self):

        Min = 0

        #sums total minutes of each traject (runs 7x)
        for traject in self.trajects:
            Min += traject.total_minutes

        return Min
        pass


    # calculates K value (quality score of all trajects)
    def get_K(self):
        p = self.get_p()
        T = self.get_T()
        Min = self.get_Min()

        K = p*10000 - (T*100 + Min)

        return K

