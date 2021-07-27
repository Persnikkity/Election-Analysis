#To do list:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

#import modules
import csv
import os

#Reading the election data
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total voter counter
total_votes = 0

#gather the candidate names and their votes
candidate_options = []
candidate_votes = {}

#declare variables for winner votes and percentage and track
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
        #print(f'{candidate_name} received {votes:,} total votes, representing {vote_percentage: .1f}% of the total vote')

        
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

    #print(winning_candidate_summary)

    #print election result
    #print(f'\nThe winner of the election is {winning_candidate} , who received {winning_count:,} total votes, representing {winning_percentage: .1f}% of the total vote')