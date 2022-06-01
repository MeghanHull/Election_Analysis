#******************************************************************************
# RICE-VIRT-DATA-PT-05-2022-U-B-MW Module 3 Challenge
#******************************************************************************
#------------------------------------------------------------------------------
# Purpose  := Analyses election results in Python
# Created  := 2022 Jun 01 19:15:02 UTC (Meghan E. Hull)
# Modified := 2022 Jun 01 20:28:49 UTC (Meghan E. Hull)
#******************************************************************************
# ANALYSIS REQUIREMENTS
#----------------------------------------------------------------
# Orginal Analysis
#----------------------------------------------------------------
# The data we need to retrieve:
# 1. The total number of votes cast;
# 2. A complete list of candidates who received votes;
# 3. The percentage of votes each candidate won;
# 4. The total number of votes each candidate won;
# 5. The winner of the election based on popular vote.
#----------------------------------------------------------------
# Challenge Analysis
#----------------------------------------------------------------
# The election commission has requested the following additional data:
# 6. The voter turnout for each county;
# 7. The percentage of votes from each county out of the total count;
# 8. The county with the highest turnout.

#******************************************************************************
# ENVIRONMENT SETUP
#----------------------------------------------------------------
# Import Modules needed
import csv
import os

# Initialize data variables
total_votes = 0                 # Data 1 - total vote counter
candidate_options = []          # Data 2 - list of candidates
candidate_votes = {}            # Data 4 - dictionary of candidate votes
candidate_results =""           # Empty string for printing Data 2, 3, & 4

# Initialize Data 5 variables - Winning Candidate and Winning Count Tracker
winning_candidate = ""          # Name of winning candidate
winning_count = 0               # Number of votes for winning candidate
winning_percentage = 0          # Percentage of total vote for winning candidate

# Initialize Challenge data variables
# C.S1
counties = []                   # Empty list of counties
county_votes = {}               # Empty dictionary of county votes
county_results =""              # Empty string for printing county results
# C.S2
highest_turnout_county = ""     # Name of county with highest turnout
highest_turnout_count = 0       # Number of votes for county with highest turnout
highest_turnout_percentage = 0  # Percentage of total vote for county with highest turnout

# Specify input file
# Assign a variable for the file to load and the path (indirect path with os module)
file_to_load = os.path.join("Resources", "election_results.csv")

#******************************************************************************
# ANALYZE INPUT DATA
#----------------------------------------------------------------
# Gather Data 1, 2, & 4 from input file
#----------------------------------------------------------------
# Open the election results and read the file with open()
with open(file_to_load) as election_data:
     # To do: perform analysis.
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     
     # Get headers
     headers = next(file_reader)
     
     # Print each row in the CSV file.
     for row in file_reader:
        #----------------------------------------------------------------
        # Data 1 - Add to the total vote count
        #----------------------------------------------------------------
        total_votes += 1
        
        #----------------------------------------------------------------
        # Data 2 - Add new candidate names
        #----------------------------------------------------------------
        # Find the candidate name from each row
        candidate_name = row[2]
        
        # Check if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
             # D2 - Add the candidate name to the candidate list.
             candidate_options.append(candidate_name)
             
             # D3 - Begin tracking that candidate's vote count.
             candidate_votes[candidate_name] = 0
        
        #----------------------------------------------------------------
        # Data 4 - Add to candidate vote count
        #----------------------------------------------------------------
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1     

        #----------------------------------------------------------------
        # Data 6 - Find turnout for each county
        #----------------------------------------------------------------
#-->    # C.S3 - Find the county name from each row
        county_name = row[1]
        
#-->    # C.S4a - Check if the county does not match any existing county
        if county_name not in counties:
#-->         # C.S4b - Add the county name to the counties list.
             counties.append(county_name)
             
#-->         # C.S4c - Begin tracking that counties's vote count.
             county_votes[county_name] = 0
             
#-->    # C.S5 - Add a vote to that county's count.
        county_votes[county_name] += 1     
        
#----------------------------------------------------------------
# Data 3 - Find percentage of votes for each candidate
#----------------------------------------------------------------
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # 4. Save the candidate name and percentage of votes.
    candidate_results = candidate_results + f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

    #----------------------------------------------------------------
    # Data 5 - Determine winning vote count and candidate
    #----------------------------------------------------------------
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage

        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# Save winning candidate summary
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------")

#----------------------------------------------------------------
# Data 7 - Find percentage of votes for each county
#----------------------------------------------------------------
# C.S6a - Iterate through the county list
for county_name in county_votes:
    # C.S6b - Retrieve vote count of a county
    votes = county_votes[county_name]
    
    # C.S6c - Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # C.S6d&e - Save the county name and percentage of votes
    county_results = county_results + f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n"

    #----------------------------------------------------------------
    # Data 8 - Determine county with the highest voter turnout
    #----------------------------------------------------------------
    # C.S6f - Determine if the votes are greater than the highest turnout count
    if (votes > highest_turnout_count) and (vote_percentage > highest_turnout_percentage):

        # If true then set highest_turnout_count = votes and highest_turnout_percent = vote_percentage.
        highest_turnout_count = votes
        highest_turnout_percentage = vote_percentage

        # Set the highest_turnout_county equal to the county's name.
        highest_turnout_county = county_name

# Save highest turnout summary
highest_turnout_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {highest_turnout_county}\n"
    f"-------------------------")
    
#******************************************************************************
# WRITE OUTPUT
#----------------------------------------------------------------
# C.S7 - Print to Terminal
#----------------------------------------------------------------
# Print election results
print(
     f"\nElection Results\n"
     "------------------------\n"
     f"Total Votes: {total_votes:,}\n"
     "------------------------\n"
     f"\nCounty Votes:\n"
     + county_results + "\n"
     + highest_turnout_summary + "\n"
     + candidate_results
     + winning_candidate_summary)

#----------------------------------------------------------------
# C.S8 - Print to output file
#----------------------------------------------------------------
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
     # Results
     txt_file.write(
     f"\nElection Results\n"
     "------------------------\n"
     f"Total Votes: {total_votes:,}\n"
     "------------------------\n"
     f"\nCounty Votes:\n"
     + county_results + "\n"
     + highest_turnout_summary + "\n"
     + candidate_results
     + winning_candidate_summary)