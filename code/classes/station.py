# Celine Diks, Chris Bernsen & Julia Ham
class Station():
    """
    Class for a single station object
    """

    def __init__(self, name):
        self.name = name
        self.coordinates = (0, 0)
        
        # dictionary {station_object : time}
        self.connections = {}


    def add_connection(self, station, time):
        """
        Adds a station and a time to the dictionary with all connections.
        Expects an object as station and an integer as time.
        """
        self.connections[station] = time


    def get_connections(self):
        """
        Retrieves all connections for a single station object.
        Returns connections of given station.
        """
        return self.connections


    def has_connection(self, connection):
        """
        Checks whether station object has a connection.
        Expects a string as connection.
        Returns boolean True if station has a connection, else False.
        """
        if connection in self.connections:
            return True
        return False


    def remove_connection(self, connection):
        """
        Removes connection from given station object.
        Expects an object as station.
        Returns boolean True if successful.
        """
        if connection in self.connections:
            self.connections.pop(connection)
            return True
        return False
            

    def add_coordinates(self, x, y):
        """
        Saves coordinatinates of a single station as a tuple.
        Expects floats as x and y for coordinates.
        """
        self.coordinates = (x, y)


    def get_coordinates(self):
        """
        Returns the coordinates for a single station as a tuple
        """
        return self.coordinates


    def __repr__(self):
        """
        Representates a station object when printed.
        Returns string as name of the station object.
        """
        return self.name