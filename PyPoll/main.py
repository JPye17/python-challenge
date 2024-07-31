#Dependecies
import os
import csv

#create  path to pull data 
csvpath=os.path.join('Resources', 'election_data.csv')

# Open the reader file 
with open(csvpath) as csvfile:

	csvreader = csv.reader(csvfile, delimiter=",")

	header = next(csvreader, None)

#variables and lists and dictionary
	total_votes = 0
	candidates =[]
	vote_counts = {}
	results = []
	highest_vote = 0


#loop through csv to get total votes
	for row in csvreader:
		total_votes += 1
		candidate = row[2]

# if statement to append candidates in list
		if candidate not in candidates:
				candidates.append(candidate)

# adding candidates to dictionary
		if candidate in vote_counts:
			vote_counts[candidate] += 1
		else:
			vote_counts[candidate] = 1

#Find percentage of votes per candidate
	for candidate, count in vote_counts.items():
		percentage = (count / total_votes) * 100
		percentage_rounded = round(percentage, 3)
		results.append(f'{candidate}: {percentage_rounded}% ({count})')

#Find the winner 
	for candidate, count in vote_counts.items():
		if count > highest_vote:
			winner = candidate
			highest_vote = count

#Sending to text file 
output_path = os.path.join("analysis", "PyPoll_Results.txt")

#open text file and write mode
with open(output_path, "w") as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow([f"Election Results"])
	csvwriter.writerow([f"-------------------------"])
	csvwriter.writerow([f"Total Votes: {total_votes}"])
	csvwriter.writerow([f"-------------------------"])
	csvwriter.writerow([f'{results[0]}'])
	csvwriter.writerow([f'{results[1]}'])
	csvwriter.writerow([f'{results[2]}'])
	csvwriter.writerow([f"-------------------------"])
	csvwriter.writerow([f"Winner: {winner}"])
	csvwriter.writerow([f"-------------------------"])

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(results[0])
print(results[1])
print(results[2])
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")