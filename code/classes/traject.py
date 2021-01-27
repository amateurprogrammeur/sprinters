# Celine Diks, Chris Bernsen & Julia Ham
class Traject():
    """
    Class for a traject made of station objects.
    """
        
    def __init__(self):

        # stations = [ station_object ]
        self.stations = []
        self.total_minutes = 0


    def add_station(self, station, time):
        """
        Adds a station object to the stations list.
        Updates the total amount of minutes in a traject object.
        Expects a station object and an integer as time.
        """
        self.stations.append(station)
        self.total_minutes += time


    def get_stations(self):
        """
        Returns a list of station object as a traject object.
        """
        return self.stations


    def remove_station(self, station, time):
        """
        Removes a station from the traject object if possible.
        Expects an object as station and an integer as time.
        Returns boolean True if succesfull, else False.
        """
        if station in self.stations:
            self.stations.remove(station)
            self.total_minutes -= time
            return True
        return False


    def has_station(self, station):
        """
        Checks whether traject has a station object already.
        Expects an object as station.
        Returns boolean True if traject object has station, else False.
        """
        if station in self.stations:
            return True
        return False


    def get_time(self):
        """
        Retrieves total amount of minutes of traject object.
        Returns itself.
        """
        return self.total_minutes

    
    def get_last_station(self):
        """
        Retrieves last added station to the traject.
        Returns itself.
        """
        return self.stations[-1]

    def __repr__(self):
        """
        Represents a traject object when printed.
        Returns string of first station of traject
        """
        return f"TR: {self.stations[0].name}<>{self.stations[-1].name}"