from code.classes.traject import Traject

import networkx as nx
from matplotlib import pyplot
import matplotlib.pyplot as plt
import pandas as pd

import os

class Map():

    def __init__(self, stations):
        self.trajects = []
        self.stations = stations
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
        edges = []
        nodes = []

        for key in self.stations:
            station = self.stations[key]
            connections = station.get_connections()

            station_coordinates = station.get_coordinates()

            if station not in nodes:
                G.add_node(station.name, pos=(float(station_coordinates[1]), float(station_coordinates[0])))
                nodes.append(station)

                for connection in connections:
                    if connection not in nodes:
                        print(connection)
                        G.add_edge(station.name, connection)

            #print(f'Station: {station}. Connections:')
            # for connection in connections:
                # print(f'{connection} Time: {connections[connection]}')
                # edge = (station.name, connection)

                # edges.append(edge)

                # print(station.name)
                # print(connection)
                # G.add_edge(station.name, connection, weight=10)

        # G.add_edges_from(edges)
        # G.add_edge_from(station1, station2)

        # print(nx.get_node_attributes(G, 'pos'))
        # nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=200, node_color='grey', font_size=8, font_weight='bold')
        # plt.tight_layout()

        # nx.draw(G)
        # plt.savefig(f'code/visualisatie/tests/Graph_3.png', format="PNG")
        # plt.show()


        # pos = nx.get_node_attributes(G, 'pos')

        weight = nx.get_edge_attributes(G, 'weight')
        pos = nx.spring_layout(G)
        
        nx.draw_networkx(G, pos)
        nx.draw_networkx_edges(G, pos)

        # pyplot.gca().invert_yaxis()
        pyplot.gca().invert_xaxis()

        plt.savefig(f'code/visualisatie/tests/Graph_7.png', format="PNG")
        plt.show()

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

