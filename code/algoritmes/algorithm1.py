from code.classes.traject import Traject
from code.classes.map import Map
import random 

def algorithm1(amount, stations):

    new_map = Map(stations)

    for i in range(7):

        new_traject = Traject()

        # print(random.choice(list(stations.values())))
        
        # add random station to traject
        random_station = random.choice(list(stations.values()))
        # print(f"random station = {random_station}")

        new_traject.add_station(random_station, 0)

        # check connections of station
        connections = random_station.get_connections()
        # print(f"connections of random station ={connections}")

        x = True
        while x == True:
            # check if connection is already in traject
            station = random.choice(list(connections.keys()))
            # print(station)

            if new_traject.has_station(station):
                # hier gaat het waarschijnlijk fout
                list_1 = list(connections.keys())
                list_2 = new_traject.get_stations()
                
                # print(list_1)
                # print(list_2)

                check = all(item in list_2 for item in list_1)
                # print(check)
                if check:
                    x = False
                else:
                    continue
            else:
                time = int(connections[station])
                last_station = station
                last_time = int(connections[station])
                connections = last_station.get_connections()
                new_traject.add_station(station, time)

                # print(f"new connection = {station} with time = {time}")

                if new_traject.get_time() > 120:
                    x = False


        # print(f"TRAJECT: {new_traject.get_stations()} with TIME: {new_traject.get_time()}")
        if new_traject.get_time() > 120:
            new_traject.remove_station(last_station, last_time)
        print(f"TRAJECT: {new_traject.get_stations()} with TIME: {new_traject.get_time()}")

        new_map.add_traject(new_traject)

    print(new_map.get_K())

    return new_map

        # delete last added station (so that total_minutes < 2 hours)

































































































































































































































































































































































































































































































