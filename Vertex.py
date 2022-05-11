class Station: 
    def __init__(self, name, colour, dist =600 , edges = []):
        self.name= name
        self.colour= colour
        self.dist= dist
        self.edges = edges 
        self.prev= "NA"

    def addEdges(self, v):
        self.edges.append(v)

    def __str__(self) -> str:
        return "Station: " + self.name + "\nLine: " + self.colour
    
    def getAdjacencyList(self):
        for i in self.edges:
            print(i.destination, end= ", ") 