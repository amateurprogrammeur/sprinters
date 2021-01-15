# sprinters
RailNL - programmeertheorie

## Case: RailNL

### Assignment general
The next question will be asked for this assignement: 
- Trajectory management of trains: Which trajectories can be made for the trains to ride during the day in an given timeframe? 
More detailed: Trajectory management of intercitytrains. To make x trajectories in a certain timeframe. A trajectory is a route of the train between different stations. each station has a connection time. The total of the connection times of the trjaect can not be more then the given time.

### Assignment 1: Only of Noord-Holland en Zuid-Holland
We have 22 to most import stations in a csv file. There are 28 connections between stations (station1 - station2) with a connection time between the stations. In data/connectiesHolland.csv is the information stored. In data/StationsHolland.csv are the linked x & y coordinates saved. 

First question to anwser:
1. Trajectory management of trains with max 7 trajectories and a timeframe of 2 hours. Have to ride all connections you make. 

Assumpsions we make: 
- No delay of the trains
- Speed of trains are the same every time (x km/h)
- Every station is evenly busy
- A train can ride the connection both ways
- In one traject you can not pass the same station twice (no loops)
- Trajectories can use connections that are already used in another trajectory
- Trajectory time = max 2 hours
- Max 7 trajectories in the 2 hours
- Shortest connectiontime is 5 mintutes
- The most connections a station can have is 4

Second question to anwser:
2. Check quality of Trajectory management: What is the highest K with max 7 trajectories in 2 hours? 
- If 100% of connections is used in a trajectory, gives 10000 points, otherwise a fraction. 
- Less trajectories for the same service, is cheaper. 
- Less time for same trajectories, the better. 
You get the following formula to calculate the quality:

**Formula: K = p*10000 - (T*100 + Min)**
Where K is the quality of the trajectory management, p the fraction of the used connections (so between 0 and 1), T is the amount of Trajectories and Min is the amount of minutes in all trajectories combined.

Again, make a Trajectory management for North- and South-Holland with a maximum of seven trajectories within a timeframe of two hours, now try to get K as high as possible.

### Assignement 2: Netherland

Third question to anwser:
3. Are you ready for something bigger? We're going to work on The Netherlands as a whole now. Here, you'll find the document with connections and the document with intercity stations for The Netherlands, again with their x and y coordinates. 

Fourth question to anwser: 
4. Again, make a trajectory management for The Netherlands with a maximum of twenty trajectories within a time frame of three hours. Try to get K as high as possible again. The goal function stays the same. Create a good looking visualisation with your results, you can decide yourself how you do this.

### Advanced
Other question to be anwsered for advanced options: 

5. Move three random tracks and run your algorithms again. Do you now find better or worse numbers for the goal function? Try this a couple of times and find out which tracks have the most impact on the goal function.

6. Utrecht Central will be rebuilt and all connection from and to the station will be replaced by busses. All connections between the stations that are connected to Utrecht Centraal will not be available. Again, make a trajectory management. 

7. Also take a look at how big the impact for other stations would be, if they would lose all connections.

### Output
To verify the results, it is good to generate your format in a uniform output. Look at the example (3 trains through North-Holland) en make sure your program can change the solution for the right format. A constraint for the output are the header-line (line 1) and the footer-line (line 5). These will have to be visible in your output as well where only the number for the output has to change.

Note: Your program doesn't have to do anything with this. The program will only have to be able to do this in the last step of the process.

**header line** train,stations
                train_1,"[Beverwijk, Castricum, Alkmaar, Hoorn, Zaandam]"
                train_2,"[Amsterdam Sloterdijk, Amsterdam Centraal, Amsterdam Amstel, Amsterdam Zuid, Schiphol Airport]"
                train_3,"[Rotterdam Alexander, Gouda, Alphen a/d Rijn, Leiden Centraal, Schiphol Airport, Amsterdam Zuid]"
**footer line** score,3819.7142857142853

### Check50
Output testing in 3 steps:
1. Save awnser in format in new output.csv file
2. Open terminal in folder where output.csv is saved
3. Run: 
    - For Holland: check50 minprog/theorie-check50/master/railnl/holland
    - For Nederland:  minprog/theorie-check50/master/railnl/national

### Structuur
List of most important maps and files of the project: 

- ./code: All supporting code of the project
- ./code/algorithms: Code for mutiple algorithms
- ./code/classes: contains a code file for each three classes
    - /map.py
    - /station.py
    - /traject.py
- ./code/visualisation: contains the bokeh code for visualisation
- ./data: Contains numerous csv data files that are needed for the assignment and to fill in the graph
- ./docs: Contains designdocument
- ./main.py contains the project itself

### Changes
The following changes where made: 
- ConnectiesNationaal.csv: Time connections made integers instead of float numbers. 

### To run 
To run programm use python main.py
Can change to HL for Noord en zuid holland
    - In main.py (load function)
Can change to NL for data of whole of Netherlands 
    - Change 20 stations in main.py (load function) instead of 7 and minutes in map.py

### How we use the algorithms
uitleggen op welke manier de algoritmes door elkaar te gebruiken zijn
### Authors
- Celine Diks
- Chris Bernsen
- Julia Ham
