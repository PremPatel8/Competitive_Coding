from collections import defaultdict, Counter, deque
import pprint


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, nodesNo, edgeWeight=6):
        self._graph = defaultdict(set)
        self._nodesNo = nodesNo
        self._edgeWeight = edgeWeight

    def connect(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    def find_all_distances(self, startNode):
        distances = []

        # Iterate through every node in the tree except the start node
        for node in range(self._nodesNo):
            if node != startNode:
                # For each node in the tree find the shortest distance between
                # that node and the given start node
                dist = self.BFS_Distance(startNode, node)
                distances.append(dist)

        print(*distances)

    def BFS_Distance(self, startNode, endNode):
        weight = 0
        queue = deque([(startNode, weight)])
        visited = {startNode}

        """ If the endNode is disconnected from the rest of the graph then
        it will not be present in the Adjacency list and won't be reachable
        from the start node, hence it's distance will be -1 """
        if endNode not in self._graph:
            return -1

        while queue:
            (curNode, wt) = queue.popleft()

            visited.add(curNode)

            for neighbour in self._graph[curNode]-visited:
                if neighbour == endNode:
                    return wt+6

                queue.append((neighbour, wt+6))
                visited.add(neighbour)

        """If the endNode is present in the Adjacency list but no path is found
        from the startNode to this endNode then it's distance will be -1 """
        return -1


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x-1, y-1)

    pretty_print = pprint.PrettyPrinter()
    pretty_print.pprint(graph._graph)

    s = int(input())
    graph.find_all_distances(s-1)
