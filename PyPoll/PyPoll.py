#Import dependencies
import os
import csv

#Open file
csvpath = os.path.join((os.path.abspath(__file__)), '..', 'Resources', 'election_data.csv')

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv in read mode
with open(csvpath) as csvfile:

    # Store data under csvreader variable
    csvreader = csv.reader(csvfile,delimiter=",") 

    # Skip the header so we go through the actual values
    csv_header = next(csvreader)     

    # Go through each row in the csv
    for row in csvreader: 

        # Count the votes and store in variable called total_votes
        total_votes +=1

        # There are four candidates, and each time their name appears, the counter will go up by one
        # Their names will be stored on a list, and their votes in another list
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 #To find the winner, a dictionary was made out of the two lists
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
winner = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Find percent of votes
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the election results
print(f"Election Results")
print(f"Total Votes: {total_votes}")
print(f"Khan: {round(khan_percent,3)}% ({khan_votes})")
print(f"Correy: {round(correy_percent,3)}% ({correy_votes})")
print(f"Li: {round(li_percent, 3)}% ({li_votes})")
print(f"O'Tooley: {round(otooley_percent, 3)}% ({otooley_votes})")
print(f"Winner: {winner}")