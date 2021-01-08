class Traject():

    def __init__(self):
        self.stations = []
        self.total_minutes = 0
        pass

    # add station object to stations list and updates total_minutes
    def add_station(self, station, time):
        self.stations.add(station)

        self.total_minutes += time

    # returns list of stations
    def get_stations(self):
        return self.stations

    # removes station from traject if possible
    def remove_station(self, station):
        if station in stations:
            stations.remove(station)
            return True
        else:
            return False

    # returns whether traject has station or not
    def has_station(self, station):
        if station in self.stations:
            return True
        else:
            return False