===What Data you must know and have beforehand===
1. Longitude/Lattitude of each station
2. Maximum capacity of each truck in kilograms 
3. CSV file whose columns are formatted just like malawi-example.csv

===How to compute most efficient paths===
1. Create a csv file in the same EXACT format as malawi-example.csv. Make sure the first row is the supply station. The demand for this MUST be 0.
2. Call 'python main.py your_csv_file max_capacity_of_each_truck'
    - Example call:
    $ python main.py malawai.csv 5000

===What is going on behind the scenes===
1. I take the CSV file, parse it into standard VRP format.
2. I call CVRP library function that I heavily modified
3. Results are formatted into Json file called output.json