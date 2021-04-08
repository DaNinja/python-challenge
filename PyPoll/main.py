import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

csv_path = os.path.join("Resources", "election_data.csv")



with open(csv_path, "r") as csv_file:
    csvreader = csv.reader(csv_file)
    next(csvreader)
    i = 0
    counter = 0
    
    candidate_votes = {}
    for items in csvreader:
        
        counter = counter + 1

        if items[2] not in candidate_votes.keys():
            candidate_votes[items[2]] = 1
        else:
            candidate_votes[items[2]] = candidate_votes[items[2]] + 1
        

    num_of_candidates = len(candidate_votes.keys())


highest_vote = max(list(candidate_votes.values()))
highest_vote_index = list(candidate_votes.values()).index(highest_vote)

#print ({list(candidate_votes.keys())[highest_vote_index]})

print(f'''

  Election Results
  -------------------------
  Total Votes: {counter}
  -------------------------
  {list(candidate_votes.keys())[0]}: {((list(candidate_votes.values())[0]) / counter) * 100}% ({(list(candidate_votes.values())[0])})
  {list(candidate_votes.keys())[1]}: {((list(candidate_votes.values())[1]) / counter) * 100}% ({(list(candidate_votes.values())[1])})
  {list(candidate_votes.keys())[2]}: {((list(candidate_votes.values())[2]) / counter) * 100}% ({(list(candidate_votes.values())[2])})
  {list(candidate_votes.keys())[3]}: {((list(candidate_votes.values())[3]) / counter) * 100}% ({(list(candidate_votes.values())[3])})
  -------------------------
  Winner: {list(candidate_votes.keys())[highest_vote_index]}
  -------------------------



''')

outF = open("Analysis/My_Election_Output_File.txt", "w")
outF.write(f'''

  Election Results
  -------------------------
  Total Votes: {counter}
  -------------------------
  {list(candidate_votes.keys())[0]}: {((list(candidate_votes.values())[0]) / counter) * 100}% ({(list(candidate_votes.values())[0])})
  {list(candidate_votes.keys())[1]}: {((list(candidate_votes.values())[1]) / counter) * 100}% ({(list(candidate_votes.values())[1])})
  {list(candidate_votes.keys())[2]}: {((list(candidate_votes.values())[2]) / counter) * 100}% ({(list(candidate_votes.values())[2])})
  {list(candidate_votes.keys())[3]}: {((list(candidate_votes.values())[3]) / counter) * 100}% ({(list(candidate_votes.values())[3])})
  -------------------------
  Winner: {list(candidate_votes.keys())[highest_vote_index]}
  -------------------------



''')
outF.write("\n")
outF.close()