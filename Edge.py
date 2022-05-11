class Edge: 
    def __init__(self, origin, destination, weight):
        self.origin= origin 
        self.destination= destination
        self.weight = weight 
    
    def reverse(self):
        return Edge(self.destination, self.origin, self.weight )