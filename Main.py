from Vertex import Station as station
from Edge import Edge as edge 
import Graph

Graph.makeMap()

origin = "Yishun"
destination= "MacPherson"

# search() method returns a "list" of stations containing the input string
print(Graph.search("Woodlands"))
print(Graph.search("Tampines"))
print("--------------------------------")

# returns the neighbouring stations 
print(Graph.getAdjacencyListOf("Yishun"))
print(Graph.getAdjacencyListOf("Dhoby Ghout"))
print("--------------------------------")

# returns the list of stations along the journey of the shortest path
print(Graph.getShortestPath(origin, destination))
print("--------------------------------")

# returns the time taken to travel the shortest path
print(Graph.getShortestTime(origin, destination))
print("--------------------------------")
