class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, value):
        if self.adj_list[value] not in self.adj_list.keys:
            self.adj_list[value] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, v1):
        if v1 not in self.adj_list.keys():
            return False
        for i in self.adj_list[v1]:
            try:
                self.adj_list[i].remove(v1)
            except ValueError:
                pass
        self.adj_list.pop(v1)
        return True