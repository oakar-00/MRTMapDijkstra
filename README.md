# MRTMapDijkstra

## Non-technical introduction of the project
I am Oakar, Computer Science and Design (CSD) student from Singapore University of Technology and Design. 

During my time in Term 4 of CSD, I was introduced to various Algorithms and I was paprticularly interested in the applications of the graph algorithms to the real world context. 

This was my motivation for this project. 

One of the Graph Algorithms that I learnt was Dijkstra's Algorithm, where the algorithm finds the shorest path from a source node to a destination node, given a non-negative weighted graph. 

I am also someone who frequently take public transport and most of my transport time is spent on the train.
Since I have quite a few minutes to spare on the MRT, I spend my commute time coding (P.S. I am doing this while on MRT as well haha)

One day, I had an idea that sprung up my head about making the Map of the MRT stations and running Dijkstra's algorithm on it brining me to this project. 

## How is the map created?

Each station on the map is represented by an object "Station" in the Vertex.py and a Station is defined by its name, colour, edges, distance and a reference of the previous station. The first 3 attributes are crucial in creating a unique station and the last 2 is crucial in storing the information while running the Dijkstra's Algorithm. 

Each 'connection' is represented by an object "edge" defined by its origin, destination and weight- time taken to travel from origin to destination

Using multiple helper functions, the stations and the edges are created through looping over the list of the station names and the durations. Each MRT line is created in isolation and once all the lines are created, we connect one line to another using the interchanges. 

Tada! We have our MAP!

## Functions 
 search (string)
 - returns a list of station names containing the input string

 getAdjacencyListOf(station)
 - returns the Adjacency List of the input station - Adjacency List is the list of the neighbouring nodes in the graph, in this case they are the next stations from the station in all directions. 

 getShortestPath(origin, destination)
 - returns a list of stations along the shortest path from origin to destination

 getShortestTime(origin, destination)
 - returns time taken for shortest path from origin to destination
