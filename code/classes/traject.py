class Traject():

    def __init__(self):
        self.stations = []
        self.total_minutes = 0
        pass

    def add_station(self, station, time):
        self.stations.add(station)

        self.total_minutes += time

    def get_stations(self):
        return self.stations

    def has_station(self, station):
        if station in self.stations:
            return True
        else:
            return False