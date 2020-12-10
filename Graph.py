class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        '''JSON TO GRAPH METHOD:'''
        self.graph_dict = {}
        for i in range(len(vertices)):
            if vertices[i]["name"] in self.graph_dict:
                self.graph_dict[i]["name"].append(vertices[i]["prerequisites"])
            else:
                self.graph_dict[vertices[i]["name"]] = vertices[i]["prerequisites"]
        print(self.graph_dict)

    def traverse(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.traverse(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths
    
    def numPrereqs(self, data, paths=[], visited=[]):
        for i in self.graph_dict[data]:
            if i is not None:
                self.numPrereqs(i)
                if i not in paths:
                    paths.append(i)
        return paths