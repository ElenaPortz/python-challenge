import os
import csv

election_results = dict()
votes =0
winner =["", 0]

# Compares candidate in arg to the winner currently held in the winner variable.
# Called on each candidate in the election
def calculate_winner (candidate):
    candidate_votes = election_results[candidate]
    if candidate_votes > winner[1]:
        winner[0] = candidate
        winner[1] = candidate_votes
    return (winner)

# prints election results in terminal end exports identical output onto a textfile
def print_and_export_results():
    #creates a textfile 
    output = open("PyPoll_results.txt", "w")
    
    # prints each string in output list and rites each string in 
    # output_list as a line in the output textfile
    for str in output_list():
        print (str)
        output.write(str)
        output.write('\n')
    output.close()

# generates a list of strings, which together comprise the desired print output
# returned list will be used to print results in both the terminal and the exported textfile
def output_list():
    output = list()
    output.append("Election Results")
    output.append ("-"*20)
    output.append(f'Total Votes: {votes}')
    output.append ("-"*20)

    for candidate in election_results:
        winner = calculate_winner(candidate)
        percentage = '%.3f'%(election_results[candidate]/votes*100)
        output.append(f'{candidate}:  {percentage}% ({election_results[candidate]})')
    output.append("-"*20)
    output.append(f' Winner: {winner[0]}')
    output.append ("-"*20)
    return (output)

# main 
pyPoll_csv = os.path.join('election_data.csv')
with open (pyPoll_csv) as csvfile:
    csvreader= csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)  
    
    # creates dictionary of candidates (the keys) and the number of votes cast for each (value)
    for row in csvreader:
        votes += 1 
        if row[2] in election_results:
            election_results[row[2]] +=1
        else:
            election_results[row[2]] = 1
    
print_and_export_results()

