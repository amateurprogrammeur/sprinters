# De sprinters
RailNL - programmeertheorie

## Case: RailNL

### Assignment general
The next question will be asked for this assignement: 
- Trajectory management of trains: Which trajectories can be made for the trains to ride of a given timespan? To make x trajectories of a certain timespan.
- A trajectory is a route between stations. Two stations can be connected with a certain duration. The sum of the durations of the connections within a traject cannot exceed a given time.

### Assumptions
Assumpsions we make: 
- A train can ride the connection both ways
- In one traject you can not pass the same station twice (no loops)
- Trajectories can use connections that are already used in another trajectory
- Trajectory time = max 3 hours
- Max 20 trajectories
- Shortest connection time is 5 mintutes
- The most connections a station has is 4

### Assignment 1: Only of Noord-Holland en Zuid-Holland
We have 22 stations in a csv file. There are 28 connections between stations (station1 - station2) with a connection time between the stations. In data/connectiesHolland.csv is the information stored. are the linked x & y coordinates saved. 

First question to anwser:
1. Trajectory management of trains with max 7 trajectories and a timeframe of 2 hours. Have to ride all connections you make. 

Second question to anwser:
2. Check quality of Trajectory management: What is the highest K with max 7 trajectories in 2 hours? 
    - 100% coverage of stations gives 100% of 10 000 points. 50% coverage thus gives 5000 points.
    - Less trajectories for same coverage gives a better score. 
    - Less time for the same coverage gives a better score.

You get the following formula to calculate the quality:

**Formula: K = p*10000 - (T*100 + Min)**

Where K is the quality of the trajectory management, p the fraction of the used connections (between 0 and 1), T is the amount of Trajectories and Min is the total duration of all trajectories in minutes.
### Assignement 2: Netherlands

Third question to anwser:
3. Do the same in question 1 and 2 but then with data/connectiesNederland.csv. In this data file there are 61 stations found with their connections. In data/StationsNederland.csv are the corresponding coordinates stored. 

Fourth question to anwser: 
4. Visualise the results from question 1,2 and 3. 

### Advanced
Other questions anwsered for advanced options: 

5. Move three random tracks and run your algorithms again. Do you now find better or worse numbers for the goal function? What gives the most impact? 

6. Utrecht Central will be rebuilt and all connection from and to the station will be replaced by busses. All connections between the stations that are connected to Utrecht Centraal will not be available. Again, make a trajectory management. 

7. The same as question 6 with other stations.

### Requirements // installation 

#### How to run
How to use requirements.txt:

run: pip3 install -r requirements.txt 

#### programs
contains the following installations:
- networkx
- matplotlib
- pandas

### Output
The output needs to be in this format: 
**header line** train,stations
                train_1,"[Beverwijk, Castricum, Alkmaar, Hoorn, Zaandam]"
                train_2,"[Amsterdam Sloterdijk, Amsterdam Centraal, Amsterdam Amstel, Amsterdam Zuid, Schiphol Airport]"
                train_3,"[Rotterdam Alexander, Gouda, Alphen a/d Rijn, Leiden Centraal, Schiphol Airport, Amsterdam Zuid]"
**footer line** score,3819.7142857142853

### Structuur
List of most important maps and files of the project: 

- ./code: All supporting code of the project
- ./code/algorithms: Code for mutiple algorithms
    - chance.py
    - hillclimber.py
    - prims.py
    - random.py
    - sim_ann.py
    Tried but not succeeded:
    - depth_first.py
    - kruskals.py
- ./code/classes: contains a code file for each class
    - /map.py
    - /station.py
    - /traject.py
- ./code/output: All output and visualiations of algoritmes. 
    - /csvs: Output
    - /graphs: Visualisation
- ./data: Contains numerous csv data files that are needed for the assignment and to fill in the graph
- ./docs: Contains designdocument
- ./main.py: Manages and runs algorithms and saves output
- ./load.py: Loads files for main assignment and add coordinates & connections to stations
- ./advanced.py: Loads files for advanced assignment and add coordinates & connections to stations

### Changes
The following changes where made: 
- ConnectiesNationaal.csv: Time connections made integers instead of float numbers.

### algorithms
#### 1. random
The random algorithm begins with choosing a random station. From its connecting stations, it chooses a random station to progress to. It does this for all 20 trajects until a. the traject reaches its max time, or b. all connecting stations are already visited. In that case, there's a 50% chance it will still progress to an already used station.

#### 2. Prims
Our prims algorithm creates a minimum spanning tree. It chooses a random station to grow the tree from (this does not influence the shape of the tree). There, it adds the smallest connection to the tree. It then compares the connections of all covered stations and chooses the smallest. It never chooses a connection between two already covered stations. It repeats this untill all stations are covered.

#### 3. Hill Climber
Our Hill climber algorithm takes a solution (e.g. from the random algorithm) as input. It mutates the solution by replacing one traject with a new random traject or deleting a traject. After each mutation, it checks the K-value of the new solution. If its higher, it saves the mutation. Otherwise, it reverts the mutation.

### 4. Simulated Annealing
To check if our Hill Climber algorithm was stuck in a local maximum, we wrote a Simulated Annealing algorithm. This algorithm, in contradiction to the Hill Climber, also accepts worse K values. It also takes a solution as input and mutates the solution. It does so by replacing one traject with a new random traject, deleting a traject or adding a traject. After each mutation, it checks the K-value of the new solution. If it's higher, it saves the mutation. If it's lower, it calculates the chance to reject or accept the worse mutation. If the chance is met, it accepts the worse solution. Otherwise, it reverts the mutation.

### 5. Chance (own algorithm)
Lastly, we created our own algorithm with heuristics we thought could be efficient for this case. Our first heuristic said that we wanted the algorithm to always start with a deadend station. We did this to make sure all stations will have a chance to be used. Then, to select the next station (a connection) we let the algorithm make a choice based on the calculation of a chance: the less minutes the connection has, the more chance it will have to be chosen as the next station. It repeats this until there are no available deadend stations.

### How we combine the algorithms
As said in the explanation from the algorithms above, we use a couple of algorithm combined with each other. Our algorithms can be divided into three "layers". On the first being Prim's algorithm. After this algorithm, the random or the chance algorithm can be applied. And on the last layer, the Hill Climber or Simulated Annealing can be applied.

### How to run 
- To run programm use: "python main.py"
- For iterations give any amount of integer
- After running: User is allways asked for input to choose data files and algorithms:
    1. Witch datafiles to load? Options given: 
        - Holland (HL)
        - Netherlands (NL)
        - Advanced (AD)
        If Advanced is chosen, continues at iii.

    ***NL & HL***
    
    2. Asks if Prims needs to be applied, (y)es or (n)o. Continues at v.
    
    ***AD***
    
    3. Asks input for (station name) to remove that station object or (connections) for three random connections to be removed.

    4. Choose first algorithm to run:
        - Random (random)
        - Chance (chance)
    5. How many iterations? (integer)
    6. Choose second algorithm to run:
        - Hillclimber (hc)
        - Simulated Annealing (sa)
        - None (n)
    7. How many iterations? (integer)

### Other
We also tried implementing a depth first and kruskals algorithm, but did not manage to make them work perfectly. You can still find the documents of depth first and kruskals algorithms in the folder sprinters/algorithms/ but you will not be asked if you want to use these in the command line of the terminal.

### Authors
- Celine Diks
- Chris Bernsen
- Julia Ham
