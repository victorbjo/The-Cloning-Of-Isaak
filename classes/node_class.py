#nodeclass for a*
from unicodedata import name


class Node:
    def __init__ (self,id, position):
        self.id = id
        self.connections = []
        self.position = position
        self.f, self.g, self.h = 0, 0, 0
        self.backpointer = None
    def __repr__(self) -> str:
        return "n"+str(self.id)

#add connections to nodes in nodelist
def add_connections(nodes):
    for node in nodes:
        lowerId = node.id[0] - 1, node.id[1]
        upperId = node.id[0] + 1, node.id[1]
        leftId = node.id[0], node.id[1] - 1
        rightId = node.id[0], node.id[1] + 1
        ids = [lowerId, upperId, leftId, rightId]
        for nodeTemp in nodes:
            if nodeTemp.id in ids:
                node.connections.append(nodeTemp)
    return nodes

def grid_to_nodes(grid):
    nodes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                nodes.append(Node((i,j), (i,j)))
    add_connections(nodes)
    return nodes

#euclidean distance
def distance(start, goal):
    return ((start[0] - goal[0])**2 + (start[1] - goal[1])**2)**0.5
#astar algorithm for pathfinding
def aStar(start, goal):
    openList = []
    closedList = []
    openList.append(start)
    while len(openList) > 0:
        current = openList[0]
        for node in openList:
            if node.f < current.f:
                current = node
        openList.remove(current)
        closedList.append(current)
        if current == goal:
            path = []
            while current.backpointer != None:
                path.append(current)
                current = current.backpointer
            path.append(current)
            return path
        for node in current.connections:
            if node not in closedList:
                if node not in openList:
                    node.g = current.g + 1
                    node.h = distance(node.position, goal.position)
                    node.f = node.g + node.h
                    node.backpointer = current
                    openList.append(node)
                else:
                    if node.g > current.g + 1:
                        node.g = current.g + 1
                        node.backpointer = current
    return None
if __name__ == "__main__":
    map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1],
            [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1]]
    nodes = grid_to_nodes(map)
    nodes = add_connections(nodes)
    print(nodes[60])
    print(nodes[17].connections)
    print(aStar(nodes[0], nodes[60]))
    #print(nodes)