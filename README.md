# Election Analysis

## Overview of Election Audit
### Project Overview
A Colorado Board of Elections employee requested a Python script to automate some election auditing data analysis.  Using a recent local congressional election as a test case, the script is to provide a summary of:
- The total number of votes cast;
- A complete list of candidates who received votes;
- The percentage of votes each candidate won;
- The total number of votes each candidate won;
- The winner of the election based on popular vote.

In subsequent review, the election commission has requested the following additional data:
- The voter turnout for each county;
- The percentage of votes from each county out of the total count;
- The county with the highest turnout.

### Purpose
The purpose of this analysis is to summarize the recent Colorado congressional election results for the election commission's audit, with the goal of extending the analysis methodology to any election.

### Resources
- Data Source: [election_results.csv](Resources/election_results.csv) 
- Software: Python 3.7
- Analysis Code: [PyPoll_Challenge.py](PyPoll_Challenge.py)

## Election Audit Results
### Original Audit Test Case Analysis
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 3.1% of the vote and 11,606 number of votes.

### Additional County Data

### Python PyPoll_Challenge.py Script
A snapshot of the **Terminal output** of [PyPoll_Challenge.py](PyPoll_Challenge.py) is available at: [Election_Results_Command_Line.png](analysis/Election_Results_Command_Line.png).
The created **text output file** of [PyPoll_Challenge.py](PyPoll_Challenge.py) is available at: [election_analysis.txt](analysis/election_analysis.txt).

### Challenges & Limitations

## Election-Audit Summary
