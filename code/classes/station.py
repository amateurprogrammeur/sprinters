class Station():

    def __init__(self, name):
        self.name = name
        self.coordinates = (0, 0)
        
        # dictionary {station : time}
        self.connections = {}

    # adds station and time to connections dictionary
    def add_connection(self, station, time):
        self.connections[station] = time
        return True

    # returns connections
    def get_connections(self):
        return self.connections

    # returns whether station has connection or not
    def has_connection(self, connection):
        if connection in self.connections:
            return True
        else:
            return False

    # saves coordinates as tuple
    def add_coordinates(self, x, y):
        self.coordinates = (x, y)
        return True

    # returns coordinates as tuple
    def get_coordinates(self):
        return self.coordinates

    # class object representation when printed
    def __repr__(self):
        return self.name
