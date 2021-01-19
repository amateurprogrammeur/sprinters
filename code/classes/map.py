from code.classes.traject import Traject

import networkx as nx
from matplotlib import pyplot
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

import random

import os

class Map():
    """
    Class for visualisation of the outcome of the algorithm.
    Also calculates the K value of the saved map.
    """
    
    def __init__(self, stations):
        self.trajects = []
        self.stations = stations

        self.colours = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black', 'grey', 'brown', 'pink',
            'olive', 'lightcoral', 'maroon', 'aqua', 'plum', 'skyblue', 'chocolate', 'lime', 'slategrey',
            'navy', 'papayawhip', 'hotpink']
        pass

    def add_traject(self, traject):
        """
        Makes it possible to add a traject to the trajects list.
        Expects an object as traject and returns a boolean True if succesfull.
        """
        
        self.trajects.append(traject)
        return True

    def add_traject_list(self, traject_list):
        """
        Makes it possible to add multiple trajects to a list.
        Expects a list as traject_list and returns a boolean True if succesfull.
        """
        self.trajects = traject_list
        return True
    
    def get_trajects(self):
        """
        Makes it possible to retrieve a list of all traject objects.
        Returns this list.
        """
        return self.trajects

    def visualise(self, name):
        """
        Visualises all the given traject data.
        Expects a string as name.
        """
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

        nx.draw_networkx(G, pos, with_labels=True, node_size=40, node_color='grey', font_size=4, font_weight='bold')
        nx.draw_networkx_edges(G, pos)

        plt.savefig(f'code/output/graphs/{name}.png', format="PNG")
        plt.show()

        pass

    def visualise_trajects(self, name):
        """
        Makes a visualisation of all the outputted trajects of the algorithm.
        Expects a string as name.
        """
        # print(colours)
        
        G = nx.DiGraph()
        edges = []
        nodes = []

        for key in self.stations:
            station = self.stations[key]

            station_coordinates = station.get_coordinates()

            if station not in nodes:
                G.add_node(station.name, pos=(float(station_coordinates[1]), float(station_coordinates[0])))
                nodes.append(station)

        counter = 0
        for traject in self.trajects:
            new_colour = self.colours.pop(0)
            counter += 1

            connections = traject.get_stations()
            for i in range(len(connections)-1):
                station = connections[i]
                connection = connections[i+1]

                G.add_edge(station.name, connection.name, color=new_colour, weight=1.5)

        edges = G.edges()
        colors = [G[u][v]['color'] for u,v in edges]
        weights = [G[u][v]['weight'] for u,v in edges]
        labels = nx.get_edge_attributes(G, 'edge_labels')
        pos = nx.get_node_attributes(G, 'pos')

        # fig, ax = plt.subplots(figsize = (8,8))

        # nx.draw(G, pos, edge_color=colors, width=weights, with_labels=True, node_size=60, node_color='grey', font_size=4, font_weight='bold', connectionstyle='arc3, rad = 0.1', ax=ax)

        nx.draw(G, pos, edge_color=colors, width=weights, with_labels=True, node_size=60, node_color='grey', font_size=4, font_weight='bold', connectionstyle='arc3, rad = 0.1')


        # nx.draw_networkx(G, pos, with_labels=True, node_size=40, node_color='grey', font_size=4, font_weight='bold')
        # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        # nx.draw_networkx_edges(G, pos, color)

        # df = pd.read_csv("C:/.. …/SpatialDataSet.txt")

        # BBox = ((3.019, 7.398, 53.836, 50.680))
        # # > (46.5691,46.8398, 24.6128, 24.8256)

        # ruh_m = plt.imread('docs/KaartNederland2-01.png')

        # ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

        # # ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
        # ax.set_title('OpenStreetMap test')
        # ax.set_xlim(BBox[0],BBox[1])
        # ax.set_ylim(BBox[2],BBox[3])
        # ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')

        # pyplot.gca().invert_yaxis()
        # # pyplot.gca().invert_xaxis()

        plt.savefig(f'code/output/graphs/{name}.png', format="PNG")
        plt.show()



    def save_map(self, name):
        """
        Saves the created visualisation of the trajects.
        Expects a string as name.
        """
        with open(f'code/output/csvs/{name}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["train", "stations"])
            counter = 1
            for traject in self.trajects:
                station_list = traject.get_stations()
                # print(f"train_{counter}", f"{station_list}")
                writer.writerow([f"train_{counter}", f"{station_list}"])

            # print("score", self.get_K())
            writer.writerow(["score", self.get_K()])

    def get_p(self):
        """
        Calculates the ratio stations covered by trajects to total amount stations as p.
        Returns integer or float as p.
        """
        covered_stations = []

        #save stations from trajects in stations list (runs 7x)
        for traject in self.trajects:
            traject_stations = traject.get_stations()
            for station in traject_stations:
                if station.name not in covered_stations:
                    covered_stations.append(station.name)

        # print(f"covered stations: {covered_stations}")

        p = len(covered_stations) / len(self.stations)
        

        # print(f"p: {len(covered_stations)} / {len(self.stations)} = {p}")

        return p


    def get_T(self):
        """
        Calculates the amount of trajects used.
        Returns an integer as T.
        """
        T = len(self.trajects)

        # print(f"T: {T}")

        return T


    def get_Min(self):
        """
        Calculates the amount of minutes used in all trajects.
        Returns an integer as Min.
        """
        Min = 0

        #sums total minutes of each traject (runs 7x)
        for traject in self.trajects:
            Min += traject.total_minutes

        # print(f"Min: {Min}")

        return Min


    def get_K(self):
        """
        Calculates the quality score of all trajects the K value.
        Returns a float as K.
        """
        p = self.get_p()
        T = self.get_T()
        Min = self.get_Min()

        K = p*10000 - (T*100 + Min)

        return K

