from Vertex import Station as station
from Edge import Edge as edge

# Initialising the varibles
#################################
blue = "Blue"
purple = "Purple"
green= "Green"
red= "Red"
yellow= "Yellow"

stations = []
edges= []

blue_edges= []
purple_edges= []
green_edges=[]
red_edges=[]
green_branch_edges= []
circle_edges=[]
circle_branch_edges=[]


#generate a graph of the MRT map
#################################
def makeMap(): 
    makeBlueLine()
    makePurpleLine()
    makeGreenLine()
    makeRedLine()
    makeGreenBranch()
    makeCircleLine()
    makeCircleBranch()
    makeInterchanges()
    global edges 
    edges = blue_edges+ purple_edges + green_edges + red_edges+ green_branch_edges + circle_edges+ circle_branch_edges


# Helper functions 
#################################
def search(string):
    out = []
    for i in stations:
        if string in i.name:
            out.append(i.name)
    return out

def getAdjacencyListOf(string):
    for i in stations: 
        if string in i.name: 
            return i.getAdjacencyList()
    return "NIL"

def getIndexofStation(string, ls):
    for i in range(len(ls)): 
        if string in ls[i].name:
            return i 

# Dijkstra Algorithm to get the shortest path
#################################
def getShortestPath(source, destination):
    q= []
    for i in stations: 
        if i.name == source:
            i.dist = 0
        else:
            i.dist= 600
        i.prev= "NA"
        q.append(i)

    while len(q)!=0:
        index =0
        u= q[0]
        for i in q:
            if i.dist < u.dist:
                u=i 
        q.remove(u)

        for i in u.edges:
            id = getIndexofStation(i.destination ,stations)
            if stations[id].dist > u.dist + i.weight:
                stations[id].dist = u.dist + i.weight
                stations[id].prev= u 
    out = []
    id = getIndexofStation(destination ,stations)
    current_station = stations[id]
    while current_station.name!= source:
        if current_station.colour == "interchange":
            out.append(current_station.name+"*")
        else:
            out.append(current_station.name)
        current_station = current_station.prev
    out.append(source)
    return out[::-1]

# Dijkstra Algorithm to get the time taken for the shortest path
#################################
def getShortestTime(source, destination):
    q= []
    for i in stations: 
        if i.name == source:
            i.dist = 0
        else:
            i.dist= 600
        i.prev= "NA"
        q.append(i)

    while len(q)!=0:
        index =0
        u= q[0]
        for i in q:
            if i.dist < u.dist:
                u=i 
        q.remove(u)

        for i in u.edges:
            id = getIndexofStation(i.destination ,stations)
            if stations[id].dist > u.dist + i.weight:
                stations[id].dist = u.dist + i.weight
                stations[id].prev= u 

    for i in stations: 
        if i.name == destination:
            return i.dist

    return "NA"

# generating the MRT lines 
#################################
def makeBlueLine():
    makeBidirectional("Bukit Panjang", "Cashew", 2, blue_edges)
    stations.append(station("Bukit Panjang", blue, dist =600 , edges = [blue_edges[0]]))
    for i in range(len(blue_stations)-1):
        makeBidirectional(blue_stations[i], blue_stations[i+1], blue_times[i], blue_edges)

    for i in range(2, len(blue_edges), 2):
        stations.append(station(blue_edges[i].origin, blue, edges= [blue_edges[i-1], blue_edges[i]]))

    stations.append(station("Expo" , blue, edges= [blue_edges[-1]]))



def makePurpleLine():
    makeBidirectional("Punggol", "Sengkang", 3, purple_edges)
    stations.append(station("Punggol", purple, dist= 600, edges= [purple_edges[0]]))
    for i in range(len(purple_stations)-1):
        makeBidirectional(purple_stations[i], purple_stations[i+1], purple_times[i], purple_edges)

    for i in range(2, len(purple_edges), 2):
        stations.append(station(purple_edges[i].origin, purple, edges= [purple_edges[i-1], purple_edges[i]]))

    stations.append(station("Harbour Front" , purple, edges= [purple_edges[-1]]))



def makeGreenLine():
    makeBidirectional("Tuas Link", "Tuas West Road", 3, green_edges)
    stations.append(station("Tuas Link", green , dist= 600, edges= [green_edges[0]]))
    for i in range(len(green_stations)-1):
        makeBidirectional(green_stations[i], green_stations[i+1], green_times[i], green_edges)

    for i in range(2, len(green_edges), 2):
        stations.append(station(green_edges[i].origin, green, edges= [green_edges[i-1], green_edges[i]]))

    stations.append(station("Pasir Ris" , green, edges= [green_edges[-1]]))


def makeRedLine():
    makeBidirectional("Jurong East", "Bukit Batok", 3, red_edges)
    stations.append(station("Jurong East", red , dist= 600, edges= [red_edges[0]]))
    for i in range(len(red_stations)-1):
        makeBidirectional(red_stations[i], red_stations[i+1], red_times[i], red_edges)

    for i in range(2, len(red_edges), 2):
        stations.append(station(red_edges[i].origin, red, edges= [red_edges[i-1], red_edges[i]]))

    stations.append(station("Marina South Pier" , red, edges= [red_edges[-1]]))


def makeGreenBranch():
    makeBidirectional("Tanah Merah", "Expo", 9, green_branch_edges)
    stations.append(station("Tanah Merah", green, dist = 600, edges= [green_branch_edges[0]]))
    makeBidirectional("Expo", "Changi Airport", 5, green_branch_edges)
    stations.append(station("Expo", green, dist=600, edges= [green_branch_edges[1],green_branch_edges[2]]))
    stations.append(station("Changi Airport", green, dist=600, edges= [green_branch_edges[-1]]))


def makeCircleLine():
    makeBidirectional("Dhoby Ghout", "Bras Basah", 2, circle_edges)
    stations.append(station("Dhoby Ghout", yellow, dist= 600, edges= [circle_edges[0]]))
    for i in range(len(circle_stations)-1):
        makeBidirectional(circle_stations[i], circle_stations[i+1], circle_times[i], circle_edges)

    for i in range(2, len(circle_edges), 2):
        stations.append(station(circle_edges[i].origin, yellow, edges= [circle_edges[i-1], circle_edges[i]]))

    stations.append(station("Harbour Front" , yellow, edges= [circle_edges[-1]]))


def makeCircleBranch():
    makeBidirectional("Promenade", "Bayfront", 2, circle_branch_edges)
    stations.append(station("Promenade", yellow, dist = 600, edges= [circle_branch_edges[0]]))
    makeBidirectional("Bayfront", "Marina Bay", 2, circle_branch_edges)
    stations.append(station("Bayfront", yellow, dist=600, edges= [circle_branch_edges[1],circle_branch_edges[2]]))
    stations.append(station("Marina Bay", yellow, dist=600, edges= [circle_branch_edges[-1]]))


def makeInterchanges():
    for i in interchanges:
        tem_id= []
        for j in range(len(stations)):
            if stations[j].name == i:
                tem_id.append(j)
        tem_edges= []
        for j in range(len(tem_id)):
            tem_edges= tem_edges+ stations[tem_id[j]].edges
        count=0
        for j in range(len(tem_id)):
            tem= tem_id[j]-count
            del stations[tem]
            count+=1
        stations.append(station(i, "interchange", 600, tem_edges))


def makeBidirectional(origin, destination,weight, dest_edges):
    e1 = edge(origin, destination, weight)
    dest_edges.append(e1)
    dest_edges.append(e1.reverse())


# lists of station names and time taken 
#################################
blue_stations = ["Cashew", "Hillview", "Beauty World", "King Albert Park", "Sixth Avenue", 
 "Tan Kah Kee", "Botenic Gardens", "Stevens", "Newton", "Little India", "Rochor", "Bugis", 
 "Promenade", "Bayfront", "Downtown", "Telok Ayer", "Chinatown", "Fort Canning", "Bencoolen", 
 "Jalan Besar", "Bendemeer", "Geylang Bahru", "Mattar", "MacPherson", "Ubi", "Kaki Bukit",
 "Bedok North", "Bedok Reservoir", "Tampines West", "Tampines", "Tampines East", "Upper Changi", "Expo"]

blue_times= [2,3,2,2,2,2,2,2,3,1,2,2,2,2,1,2,2,2,1,2,2,2,2,2,2,2,2,3,2,2,3,2]

purple_stations =["Sengkang", "Bunagkok", "Hougang", "Kovan", "Serangoon", "Woodleigh", "Potong Pasir", "Boon Keng", "Farrer Park", 
"Little India", "Dhoby Ghout", "Clark Quay", "Chinatown", "Outrum Park", "Harbour Front"]

purple_times= [2,2,2,3,2,1,3,2,1,1,3,2,1,4]

green_stations = ["Tuas West Road", "Tuas Crescent", "Gul Circle", "Joo Koon", 
"Pioneer", "Boon Lay", "Lakeside", "Chinese Garden", "Jurong East", "Clementi", "Dover", "Bouna Vista", 
"Commonwealth", "Queenstown", "Redhill", "Tiong Bahru", "Outram Park", "Tanjong Pagar", "Raffles Place", 
"City Hall", "Bugis", "Lavender", "Kallang", "Aljunied", "Paya Lebar", "Eunos", "Kembangan", 
"Bedok", "Tanah Merah", "Simei", "Tampines", "Pasir Ris"]

green_times= [4, 3, 3, 3, 3, 2, 3, 2, 5, 2, 3, 2, 3, 2, 3, 3, 2, 2, 2, 3, 2, 2, 3, 2, 3, 
2, 2, 3, 3, 3, 3]

red_stations= ["Bukit Batok", "Bukit Gombak", "Chua Chu Kang", "Yew Tee", "Kranji", 
"Marsiling", "Woodlands", "Admiralty", "Sembawang", "Canberra" ,"Yishun", "Khatib", "Yio Chu Kang", "Ang Mo Kio", 
"Bishan", "Braddell", "Toa Payoh", "Novena", "Newton", "Orchard", "Somerset", "Dhoby Ghout", 
"City Hall", "Raffles Place", "Marina Bay", "Marina South Pier"]

red_times= [2, 3, 3, 4, 3, 2, 3, 3, 2, 2, 3, 5, 2, 3, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2]

circle_stations= ["Bras Basah", "Esplanade", "Promenade", "Nicoll Highway", "Stadium", 
"Mountbatten", "Dakota", "Paya Lebar", "MacPherson", "Tai Seng", "Bartley", "Serangoon", 
"Lorong Chuan", "Bishan", "Marymount", "Caldecott", "Botanic Gardens", "Farrer Road", "Holland Village", 
"Bouna Vista", "One-north", "Kent Ridge", "Haw Par Villa", "Pasir Pajang", "Labrador Park", 
"Telok Blangah", "Harbour Front"]

circle_times= [1,3,2,2,2,1,3,2,2,2,3,2,3,2,2,5,2,3,2,2,1,3,2,2,1,2]

interchanges= ["Chinatown", "Little India", "Bugis", "Outram Park", "Tampines", "Jurong East", "Newton", "Dhoby Ghout", 
"City Hall", "Raffles Place", "Tanah Merah", "Expo", "Promenade", "Bayfront", "Marina Bay", 
"Paya Lebar", "MacPherson", "Serangoon", "Bishan", "Caldecott", "Botanic Gardens", "Bouna Vista",
"Harbour Front"]

# print(len(blue_stations), len(blue_times))
# print(len(purple_stations), len(purple_times))
# print(len(green_stations), len(green_times))
# print(len(red_stations), len(red_times))
# print(len(circle_stations), len(circle_times))
