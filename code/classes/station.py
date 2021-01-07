class Station():

    def __init__(self, name):
        self.name = name
        self.coordinates = (0, 0)
        
        #dictionary {station : time}
        self.connections = {}

    def add_connection(self, station, time):
        self.connections[station] = time
        return True

    def get_connections(self):
        return self.connections

    def has_connection(self, connection):
        if connection in self.connections:
            return True
        else:
            return False

    def add_coordinates(self, x, y):
        self.coordinates = (x, y)
        return True

    def get_coordinates(self):
        return self.coordinates

    def __repr__(self):
        return self.name
