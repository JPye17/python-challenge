#Dependecies
import os
import csv

#Create path to pull data
csvpath=os.path.join('Resources', 'budget_data.csv')

# The total number of months included in the dataset
with open(csvpath) as csvfile:

	csvreader = csv.reader(csvfile, delimiter=",")

	csv_header = next(csvreader)

#variables and lists
	total_months = 0
	total_revenue = 0
	revenue_change = 0
	prior_revenue = None	
	revenue_change_list =[] 
	greatest_pl_increase = [" ", 0]
	greatest_pl_decrease = [" ", 9999999]

#loop through CSV
	for row in csvreader:
		total_months += 1
		current_revenue = int(row[1]) 
		total_revenue += current_revenue

# The changes in "Profit/Losses" over the entire period
# and then the average of those changes
		if prior_revenue is not None:
			revenue_change = current_revenue - prior_revenue
			revenue_change_list.append(revenue_change)

# The greatest increase in profits (date and amount) over the entire period
		if revenue_change>greatest_pl_increase[1]:
			greatest_pl_increase[1] = revenue_change
			greatest_pl_increase[0] = row[0]

# The greatest decrease in profits (date and amount) over the entire period
		if revenue_change<greatest_pl_decrease[1]:
			greatest_pl_decrease[1] = revenue_change
			greatest_pl_decrease[0]	= row[0]

#set prior revenue equal to current revenew in row[1]
		prior_revenue = current_revenue

# If statment for average change
if revenue_change_list:
	average_change = sum(revenue_change_list)/len(revenue_change_list)
	round(average_change,2)
else:
	average_change = 0 

#Sending to text file 
output_path = os.path.join("analysis", "Pybank_Results.txt")

#open text file and write mode with results 
with open(output_path, "w") as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow([f"Financial Analysis"])
	csvwriter.writerow([f"----------------------------"])
	csvwriter.writerow([f"Total Months: {total_months}"])
	csvwriter.writerow([f"Total Revenue: ${total_revenue}"])
	csvwriter.writerow([f'Average Change: {round(average_change,2)}'])
	csvwriter.writerow([f"Greatest Incease in Profits: {greatest_pl_increase[0]} on (${greatest_pl_increase[1]})"])
	csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_pl_decrease[0]} on (${greatest_pl_decrease[1]})"])

#Print results to terminal 
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue}")
print(f'Average Change: ${round(average_change,2)}')
print(f"Greatest Incease in Profits: {greatest_pl_increase[0]} on (${greatest_pl_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_pl_decrease[0]} on (${greatest_pl_decrease[1]})")