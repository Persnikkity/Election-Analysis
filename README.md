# Election-Analysis
Python &amp; VS Code

## Project Overview

### Purpose

Our team was tasked with creating an analysis of election data to present the results of an election for individual candidates as well as provide the result of the overall winner of the election.  The specific request for our team was from a Colorado Board of Elections employee and was to
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calcuate the percentage and the total number of votes each candidate received.
4. Determine the winner of the election based upon popular vote.
5. Calcuate the percentage and the total number of votes cast in each county.
6. Determine which county had the largest number of votes.

### Resources

Data source: election_results.csv
Software: Python 3.8.8, Visual Studio Code 1.58.2

## Election-Audit Results

The analysis of the election data show that:

1. There were 369,711 votes cast in the election overall.
2. The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
3. The candidate results were:
    - Charles Casper Stockham received 23% of the vote with 85,213 votes
    - Diana DeGette received 73.8% of the vote with 272,892 votes
    - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes
4. The winner of the election was:
    - Diana DeGette
5. The county votes were cast as follows:
    - Jefferson County cast 10.5% of the total votes with 38,855 votes
    - Denver County cast 82.8% of the total votes with 306,055 votes
    - Arapahoe County cast 6.7% of the total votes with 24,801 votes
6. The county with the largest number of votes cast was:
    - Denver County

### Challenges and Difficulties Encountered

Challenges were experienced in printing both candidate and county data to the .txt file due to duplicate reading and writing blocks in the script. The efficiency of this script can be improved by addressing the multiple instances of writing to the .txt file and combining into a single instance of writing the results.  The usability of this script for future analyses of election data justifies returning to this script to improve efficiency.   

## Election-Audit Summary

In summary, the script developed for analyzing the election data in this project can be expanded upon to apply to larger and more complex election data sets.  As mentioned, the script could be refactored to simplify the writing process to the .txt file.  Additionally, a more granular analysis including a breakdown of candidate results within each county could be informative for future election cycles and future campaign planning.  Lastly, this script could be useful in any kind of democratic process, whether for candidates, legislation, or leadership selection.  
