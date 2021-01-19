# Celine Diks, Chris Bernsen & Julia Ham
class Station():
    """
    Class for a single station object
    """

    def __init__(self, name):
        self.name = name
        self.coordinates = (0, 0)
        
        # dictionary {station : time}
        self.connections = {}

    def add_connection(self, station, time):
        """
        Adds a station and a time to the dictionary with all connections.
        Expects an object as station and an integer as time.
        Returns boolean True if succesfull
        """

        self.connections[station] = time
        return True

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
        else:
            return False

    def add_coordinates(self, x, y):
        """
        Saves coordinatinates of a single station as a tuple.
        Expects floats as x and y for coordinates.
        Returns boolean True if succesfull.
        """

        self.coordinates = (x, y)
        return True

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
