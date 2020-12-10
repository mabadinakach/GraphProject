from Graph import Graph

data = [
    {
        "name": "CS 1.0",
        "prerequisites": []
    },
    {
        "name": "WEB 1.0",
        "prerequisites": []
    },
    {
        "name": "WEB 1.1",
        "prerequisites": ["WEB 1.0"]
    },
    {
        "name": "FEW 1.2",
        "prerequisites": ["WEB 1.0"]
    },
    {
        "name": "FEW 2.3",
        "prerequisites": ["FEW 1.2", "WEB 1.1"]
    },
]

g = Graph(data)

print(g.numPrereqs("TEST"))
print(g.traverse("FEW 2.3", "WEB 1.0"))