from collections import defaultdict


class OrbitMap:
    """ Graph data structure, undirected by default. """

    def __init__(self, connections):
        self._graph = defaultdict(set)
        self._add_connections(connections)
        self._root_node = self._get_root_node()
        self.count = 0

    def _add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self._add(node1, node2)

    def _add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)

    def _find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self._find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def _count_orbit(self):
        processed = []
        path_count = 0
        for node, values in self._graph.items():
            if node == self._root_node:
                continue
            path = self._find_path(self._root_node, node)
            if len(path) > 0 and node not in processed:
                path_count = path_count + len(path) - 1
            for v in values:
                path = self._find_path(self._root_node, v)
                if len(path) > 0 and v not in processed:
                    path_count = path_count + len(path) - 1
                processed.append(v)
            processed.append(node)
        self.count = path_count

    def _get_root_node(self):
        root_node = None
        for node in self._graph:
            root = True
            for node1, values in self._graph.items():
                if node in values:
                    root = False
                    break
            if root:
                root_node = node
                break
        return root_node

    def get_orbit_count(self):
        self._count_orbit()
        return self.count

    def get_orbital_transfer(self, node1, node2):
        path1 = self._find_path(self._root_node, node1)
        path2 = self._find_path(self._root_node, node2)
        res = list(set(path1) ^ set(path2))
        return len(res) - 2


with open(r"day_6_input.txt", "r") as fd:
    lst = []
    lines = fd.read().splitlines()
    for line in lines:
        lineparameter = line.split(')')
        lst.append((lineparameter[0], lineparameter[1]))

g = OrbitMap(lst)

print(g.get_orbit_count())
print(g.get_orbital_transfer('YOU', 'SAN'))
