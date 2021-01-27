# # Celine Diks, Chris Bernsen & Julia Ham

# classes
from code.classes.traject import Traject

# libraries
import networkx as nx
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import csv
import random

class Map():
    """
    Class for visualisation of the outcome of the algorithm.
    Also calculates the K value of the saved map.
    """
    
    def __init__(self, stations):
        self.trajects = []
        self.stations = stations


    def add_traject(self, traject):
        """
        Makes it possible to add a traject to the trajects list.
        Expects an object as traject.
        """
        self.trajects.append(traject)


    def add_traject_list(self, traject_list):
        """
        Makes it possible to add multiple trajects to a list.
        Expects a list as traject_list.
        """
        self.trajects = traject_list
    

    def get_trajects(self):
        """
        Makes it possible to retrieve a list of all traject objects.
        Returns this list.
        """
        return self.trajects


    def visualise(self, name):
        """
        Visualises all the given traject data into a graph.
        Expects a string as name.
        """
        # creates graph
        G = nx.Graph()
        nodes = []

        # gets coordinates and connections of each station
        for key in self.stations:
            station = self.stations[key]
            connections = station.get_connections()

            station_coordinates = station.get_coordinates()

            # creates node to each station with coordinates 
            if station not in nodes:
                G.add_node(station.name, pos=(float(station_coordinates[1]), float(station_coordinates[0])))
                nodes.append(station)

                # converts connections into edges between nodes
                for connection in connections:
                    G.add_edge(station.name, connection.name)

        pos = nx.get_node_attributes(G, 'pos')

        nx.draw_networkx(G, pos, with_labels=True, node_size=60, node_color='grey', font_size=4, font_weight='bold')
        nx.draw_networkx_edges(G, pos)

        plt.savefig(f'code/output/graphs/{name}.png', format="PNG")
        plt.show()


    def visualise_trajects(self, name):
        """
        Makes a visualisation of all the outputted trajects of the algorithm.
        Expects a string as name.
        """
        # create list of colours for trajects
        colours = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black', 'grey', 'brown', 'pink',
            'olive', 'lightcoral', 'maroon', 'aqua', 'plum', 'skyblue', 'chocolate', 'lime', 'slategrey',
            'navy', 'papayawhip', 'hotpink']

        # creates empty graph
        G = nx.DiGraph()
        nodes = []

        # gets coordinates and connections of each station
        for key in self.stations:
            station = self.stations[key]

            station_coordinates = station.get_coordinates()

            # creates node of each station with coordinates
            if station not in nodes:
                G.add_node(station.name, pos=(float(station_coordinates[1]), float(station_coordinates[0])))
                nodes.append(station)

        # creates edges with distinct colour for each traject
        for traject in self.trajects:

            # retrieves colour from colours list
            new_colour = colours.pop(0)

            # adds edge for each connection
            connections = traject.get_stations()
            for i in range(len(connections)-1):
                station = connections[i]
                connection = connections[i+1]

                G.add_edge(station.name, connection.name, color=new_colour, weight=1.5)

        edges = G.edges()
        pos = nx.get_node_attributes(G, 'pos')
        colors = [G[u][v]['color'] for u,v in edges]
        weights = [G[u][v]['weight'] for u,v in edges]

        # draws graph with nodes and edges
        nx.draw(G, pos, edge_color=colors, width=weights, with_labels=True, node_size=60, node_color='grey', font_size=4, font_weight='bold', connectionstyle='arc3, rad = 0.1')

        # saves graph as file
        plt.savefig(f'code/output/graphs/{name}.png', format="PNG")
        plt.show()


    def save_map(self, name):
        """
        Saves the created visualisation of the trajects.
        Expects a string as name.
        """

        # writes an output csv file with created trajects
        with open(f'code/output/csvs/{name}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["train", "stations"])
            counter = 1
            for traject in self.trajects:
                station_list = traject.get_stations()

                writer.writerow([f"train_{counter}", f"{station_list}"])
                counter += 1

            writer.writerow(["score", self.get_K()])


    def get_p(self):
        """
        Calculates the ratio stations covered by trajects to total amount stations as p.
        Returns integer or float as p.
        """

        # creates list for already used stations
        covered_stations = []

        # save stations from trajects in stations list (runs 7x)
        for traject in self.trajects:
            traject_stations = traject.get_stations()
            for station in traject_stations:
                if station.name not in covered_stations:
                    covered_stations.append(station.name)

        p = len(covered_stations) / len(self.stations)

        return p


    def get_T(self):
        """
        Calculates the amount of trajects used.
        Returns an integer as T.
        """
        T = len(self.trajects)

        return T


    def get_Min(self):
        """
        Calculates the amount of minutes used in all trajects.
        Returns an integer as Min.
        """
        Min = 0

        # sums total minutes of each traject runs 7 times
        for traject in self.trajects:
            Min += traject.total_minutes

        return Min


    def get_K(self):
        """
        Calculates the quality score of all trajects the K value.
        Returns a float as K.
        """
        p = self.get_p()
        T = self.get_T()
        Min = self.get_Min()

        # formula for calculating K value
        K = p*10000 - (T*100 + Min)

        return K


    def delete_last_traject(self):
        """
        Removes last traject from trajects list.
        """
        self.trajects.pop()