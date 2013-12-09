import sys, csv, os

def validate_args(args):
    if len(args) != 3:
        print "\nERROR: Insufficient Arguments\n"
        print "Command should be in the following format:\n"
        print "$ main.py CSV_FILE TRUCK_CAPACITY\n"
        return False
    return True  

def process_csv(filename):
    stations = {}
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        flag = True
        for row in reader:                    
            if flag:
                flag = False
                continue
            stations[row[0]] = {
                'coords': (float(row[1]),float(row[2])),
                'demand': float(row[3])
            }
    return stations            

def process_cvrp_file(stations, capacity, dimension):
    vrp_file = open("malawi.vrp", "w+")
    vrp_lines = []
    vrp_lines.append(base_vrp) #append general format
    vrp_lines.append("\nDIMENSION : " + str(dimension) + "\n")
    vrp_lines.append("EDGE_WEIGHT_TYPE : EUC_2D \n")
    vrp_lines.append("CAPACITY : " + str(capacity) + "\n")
    vrp_lines.append("NODE_COORD_SECTION\n")

    station_keys = stations.keys()

    count = 1
    for key in station_keys:
        vrp_lines.append(" " + str(count) + " " + str(stations[key]['coords'][0]) + 
            " " + str(stations[key]['coords'][1]) + "\n")
        count += 1
    
    vrp_lines.append("DEMAND_SECTION\n")    

    count = 1
    for key in station_keys:
        vrp_lines.append(str(count) + " " + str(stations[key]['demand']) + "\n")
        count += 1

    vrp_lines.append("DEPOT_SECTION\n1\n-1\nEOF\n")

    vrp_file.writelines(vrp_lines)
    vrp_file.close()

base_vrp = "NAME : Malawi\nCOMMENT : Malwai TeaTracker\nTYPE : CVRP"

if __name__ == "__main__":
    args = sys.argv
    if validate_args(args):
        _file = args[1] #get CSV file
        _capacity = int(args[2]) #get Capacity
        _stations_info = process_csv(_file) #station dict
        _dimension = len(_stations_info) #number of stations

        #Write station to .VRP file
        process_cvrp_file(_stations_info, _capacity, _dimension)

        os.chdir(os.getcwd() + "/cvrp-mc")
        os.system("python cvrpmc.py ../malawi.vrp -o paths.json")

        

        
    