# The data we need to retrieve.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("../Resources/election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: Perform analysis
    print(election_data)
# Close the file.

# 1. The total number of votes to cast.
# 2. A complete list of candidate.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on the popular vote. 