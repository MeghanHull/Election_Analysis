#******************************************************************************
# RICE-VIRT-DATA-PT-05-2022-U-B-MW Module 3 Python
#******************************************************************************
#------------------------------------------------------------------------------
# Purpose  := Analyses election results in Python
# Created  := 2022 May 23 23:21:05 UTC (Meghan E. Hull)
# Modified := 2022 Jun 01 17:27:08 UTC (Meghan E. Hull)
#----------------------------------------------------------------
# ANALYSIS REQUIREMENTS
#----------------------------------------------------------------
# The data we need to retrieve:
# 1. The total number of votes cast;
# 2. A complete list of candidates who received votes;
# 3. The percentage of votes each candidate won;
# 4. The total number of votes each candidate won;
# 5. The winner of the election based on popular vote.

#----------------------------------------------------------------
# ENVIRONMENT SETUP
#----------------------------------------------------------------
# Import Modules needed
import csv
import os

#----------------------------------------------------------------
# GET INPUT DATA
#----------------------------------------------------------------
# Assign a variable for the file to load and the path.
# Option 1 - Direct Path
# file_to_load = 'Resources/election_results.csv'
# Option 2 -Indirect Path with os module
file_to_load = os.path.join("Resources", "election_results.csv")

# File Open Option 1 - Open() & Close()
# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')
# 
# # To do: perform analysis.
# 
# # Close the file.
# election_data.close()

# File Open Option 2 - With Open()
# Open the election results and read the file
with open(file_to_load) as election_data:
     # To do: perform analysis.
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     
     # Check headers
     headers = next(file_reader)
     print(headers)
     
     # Print each row in the CSV file.
     #for row in file_reader:
     #   print(row)
#----------------------------------------------------------------
# WRITE OUTPUT
#----------------------------------------------------------------
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
     # Write header
     txt_file.write("Counties in the Election\n------------------------\n")
     # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")