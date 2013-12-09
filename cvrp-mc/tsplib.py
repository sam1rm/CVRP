from cvrp import ProblemInstance
import sys, json

def readProblem(filename):
    f = open(filename)
    cvrp = ProblemInstance()
    #read data segment
    while True:
        line = f.readline()
        (var,_, val) = line.partition(":")
        var = var.strip()
        val = val.strip()
        if var == "NAME":
            cvrp.name = val
        elif var == "TYPE":
            cvrp.type = val
        elif var == "COMMENT":
            cvrp.comment = val
        elif var == "DIMENSION":
            cvrp.dimension = int(val)
        elif var == "CAPACITY":
            cvrp.capacity = int(val)
        elif var == "EDGE_WEIGHT_TYPE":
            cvrp.ewt = val
        elif var == "EDGE_WEIGHT_FORMAT":
            cvrp.ewf = val
        elif var == "EDGE_DATA_FORMAT":
            cvrp.edf = val
        elif var == "NODE_COORD_TYPE":
            cvrp.nct = val
        elif var == "DISPLAY_DATA_TYPE":
            cvrp.ddt = val

        elif var == "NODE_COORD_SECTION":
            cvrp.node_coord = [(lambda x: (float(x[1]), float(x[2])))(f.readline().split()) for _ in xrange(cvrp.dimension)]
        elif var == "DEMAND_SECTION":
            cvrp.node_demand = [( lambda x: float(x[1]) )(f.readline().split()) for _ in xrange(cvrp.dimension)]
        elif var == "EOF":
            break
        elif var == "":
            break
    return cvrp.prepare()

def writeSolution(result,filename = None):
        (cost,paths) = result
        if filename == None:
            f = sys.stdout
        else:
            f = open("../" + filename, "w+")
        i = 1
        lines = []
        for path in paths:
            lines.append(path)
        json.dump(lines, f)
