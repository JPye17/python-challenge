#Dependecies
import os
import csv

csvpath=os.path.join('Resources', 'budget_data.csv')

# The total number of months included in the dataset
with open(csvpath) as csvfile:

	csvreader = csv.reader(csvfile, delimiter=",")
	#print(csvreader)

	csv_header = next(csvreader)
	#print(f"CSV Header: {csv header}") - why did this not work?

#variables and lists
	total_months = 0
	total_revenue = 0
	revenue_change = 0 #
	prior_revenue = 0 #
	revenue_change_list =[] #
	greatest_pl_increase = [" ", 0]
	greatest_pl_decrease = [" ", 9999999]
	average_change = 0
	monthly_change = []

#loop through CSV
	for row in csvreader:
		total_months += 1
		total_revenue = total_revenue + int(row[1])

# The total number of months included in the dataset
	#	print("Total Months:", total_months)
# The net total amount of "Profit/Losses" over the entire period
	# 	print(f"Total Revenue: ${total_revenue}")

# The changes in "Profit/Losses" over the entire period
# and then the average of those changes
		revenue_change = int(row[1]) - prior_revenue
		prior_revenue = int(row[1])
		revenue_change_list = revenue_change_list + [revenue_change]
		monthly_change = [monthly_change] + [row[0]]
		average_change = sum(revenue_change_list)/len(revenue_change_list)
		#rint(f'Average Change: {average_change}')

# The greatest increase in profits (date and amount) over the entire period
		if revenue_change>greatest_pl_increase[1]:
			greatest_pl_increase[1] = revenue_change
			greatest_pl_increase[0] = row[0]
	#print(f"Greatest Incease in Profits: {greatest_pl_increase[0]} on (${greatest_pl_increase[1]})")

# The greatest decrease in profits (date and amount) over the entire period
		if revenue_change<greatest_pl_decrease[1]:
			greatest_pl_decrease[1] = revenue_change
			greatest_pl_decrease[0]	= row[0]
#	print(f"Greatest Decrease in Profits: {greatest_pl_decrease[0]} on (${greatest_pl_decrease[1]})")

##worked to not print out the entire list once i moved print statements to the bottom

#Sending to text file 
#output_path = os.path.join("analysis", "Pybank_Results")

#open text file and write mode
#with open(output_path, "w") as csvfile:
#	csvwriter = csv.writer(csvfile)
#	csvwriter.writerow("Total Months:", total_months)
#	csvwriter.writerow(f"Total Revenue: ${total_revenue}")
#	csvwriter.writerow(f'Average Change: {average_change}')
#	csvwriter.writerow(f"Greatest Incease in Profits: {greatest_pl_increase[0]} on (${greatest_pl_increase[1]})")
#	csvwriter.writerow(f"Greatest Decrease in Profits: {greatest_pl_decrease[0]} on (${greatest_pl_decrease[1]})")

print("Total Months:", total_months)
print(f"Total Revenue: ${total_revenue}")
print(f'Average Change: {average_change}')
print(f"Greatest Incease in Profits: {greatest_pl_increase[0]} on (${greatest_pl_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_pl_decrease[0]} on (${greatest_pl_decrease[1]})")