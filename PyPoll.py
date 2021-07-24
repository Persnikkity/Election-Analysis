#To do list:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

#import modules
import csv
import os

#Direct Path to a File

#Assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'

#open the data file
#election_data = open(file_to_load,'r')
#To dos from the list
#close the data file
#election_data.close()

#Better option using with statement:
#Open the election results and read the file
#with open(file_to_load) as election_data:
    #To Dos and analysis
    #print(election_data)


#Indirect Path to the File

#Assign a variable for the file to load into as an object and give the path
#file_to_load = os.path.join("Resources","election_results.csv")

#Open the election results and read the file
#with open(file_to_load) as election_data:

     # Print the file object
     #print(election_data)

#3.4.3 Writing to files in Python

#creating a file to write to
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

#writing to the actual file
# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

#replace the open and close - use with
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World2")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

    #or
    #txt_file.write("\nArapahoe, Denver, Jefferson")

    #with a heading
    #txt_file.write("\n ")
    #txt_file.write("\nCounties in the Election")
    #txt_file.write("\n-----------------------")
    #txt_file.write("\nArapahoe\nDenver\nJefferson")

#3.4.4  Reading the election data
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Print each row in the csv file
    #for row in file_reader:
        #print(row)
    
    #Print header row 
    headers = next(file_reader)
    print(headers)

    #Skip header row
    #next(file_reader)
