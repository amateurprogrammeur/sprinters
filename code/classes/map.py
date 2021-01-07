from code.classes.traject import Traject

class Map():

    def __init__(self):
        self.trajects = []
        pass

    def add_traject(self, traject):
        self.trajects.append(traject)
        return True
    
    def get_trajects(self):
        return self.trajects

    def visualise(self):
        # make html file

        # for each station, make node with station.get_coordinates()

        # for each traject
        #       for each station
        #           create line between stations

        #matplotlib?

        pass
    
    def get_p(self):
        stations = []

        #save stations from trajects in stations list (runs 7x)
        for traject in self.trajects:
            traject_stations = traject.get_stations()
            stations.extend(traject_stations)

        #remove duplicates
        stations = list(dict.fromkeys(stations))

        p = len.stations / 22
        return p

    def get_T(self):
        T = len(self.trajects)
        return T

    def get_Min(self):

        Min = 0

        #sums total minutes of each traject (runs 7x)
        for traject in self.trajects:
            Min += traject.total_minutes

        return Min
        pass


    def get_K(self):
        p = self.get_p()
        T = self.get_T()
        Min = self.get_Min()

        K = p*10000 - (T*100 + Min)

        return K

