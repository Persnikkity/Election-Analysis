# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

#gather the candidate names and their votes
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

#declare variables for winner votes and percentage and track
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# 2: Track the largest county and county voter turnout.
largest_turnout_county = ""
largest_turnout_votes = 0
largest_turnout_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #Read header row 
    headers = next(file_reader)

    #Print each row in the csv file
    for row in file_reader:
        #add to the total vote count same as total_votes = total_votes + 1
        total_votes += 1
        #get candidates name from a row and store as key in dictionary
        candidate_name = row[2]

        #add candidate names to candidate list IF not already there!
        if candidate_name not in candidate_options:
            #add candidate name to candidate list
            candidate_options.append(candidate_name)
            #begin tracking candidates vote count
            candidate_votes[candidate_name] = 0

        #add a vote to candidate's votes
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:    

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Print the total votes
    #print(total_votes)

    #print all candidate names
    #print(candidate_options)

    #print the candidate vote dictionary showing each person's votes
    #print(candidate_votes)

    #print vote percentages for candidates

    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        candidate_results = (f'{candidate_name}: {vote_percentage: .1f}% ({votes:,}) \n')
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
            
        #determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    

    #print election result
    #print(f'\nThe winner of the election is {winning_candidate} , who received {winning_count:,} total votes, representing {winning_percentage: .1f}% of the total vote')

total_votes = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # 3: Extract the county name from each row.
        county_name = row[1]

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:


    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county_name)
        
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"County Votes:\n"
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # 6d: Print the county results to the terminal.
        print(county_results)
        

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > largest_turnout_votes) and (vote_percentage > largest_turnout_percentage):
            largest_turnout_votes = votes
            largest_turnout_county = county_name
            largest_turnout_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    largest_turnout_summary = (
        f"-------------------------\n"
        f"Largest Turnout: {largest_turnout_county}\n"
        f"Largest Turnout Count: {largest_turnout_votes:,}\n"
        f"Largest Turnout Percentage: {largest_turnout_percentage:.1f}%\n"
        f"-------------------------\n")
    print(largest_turnout_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_turnout_summary)