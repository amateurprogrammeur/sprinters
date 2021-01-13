from code.classes.traject import Traject

import networkx as nx
from matplotlib import pyplot
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

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
        
        # opties: 
        # elk traject andere kleur
        # alleen verbindingen laten zien die in een traject zitten
        # verbinding dikker maken als er een traject overheen gaat, hoe dikker hoe meer trajecten?
        # 
        # 2 trajecten die dezelfde verbinding nemen willen we naast elkaar laten zien
        # tijden aangeven bij elke edge


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
                    G.add_edge(station.name, connection.name, edge_color='red')

        color = nx.get_edge_attributes(G, 'edge_color')
        pos = nx.get_node_attributes(G, 'pos')

        # nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=200, node_color='grey', font_size=8, font_weight='bold', edge_color='red')

        nx.draw_networkx(G, pos, with_labels=True, node_size=200, node_color='grey', font_size=8, font_weight='bold')
        nx.draw_networkx_edges(G, pos, color)

        plt.savefig(f'code/output/graphs/Graph_10.png', format="PNG")
        plt.show()

        pass

    def save_map(self, name):
        
        with open(f'code/output/csvs/{name}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["train", "stations"])
            counter = 1
            for traject in self.trajects:

                station_list = traject.get_stations()
                # print(f"train_{counter}", f"{station_list}")
                writer.writerow([f"train_{counter}", f"{station_list}"])
                counter += 1

            # print("score", self.get_K())
            writer.writerow(["score", self.get_K()])

# train,stations
# train_1,"[Beverwijk, Castricum, Alkmaar, Hoorn, Zaandam]"
# train_2,"[Amsterdam Sloterdijk, Amsterdam Centraal, Amsterdam Amstel, Amsterdam Zuid, Schiphol Airport]"
# train_3,"[Rotterdam Alexander, Gouda, Alphen a/d Rijn, Leiden Centraal, Schiphol Airport, Amsterdam Zuid]"
# score,3819.7142857142853
        
    

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

