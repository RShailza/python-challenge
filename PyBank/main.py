# Import Modules
import os
import csv

# Variables 
count_months = []
total_months = 0
net_change = []
average_net_change = 0
list2 = []

# Set path for the file
#csvpath = "../Resourses/budget_data.csv"
csvpath = os.path.join("..", "Resources", "budget_data.csv")


# Reading using CSV module

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    reader = csv.reader(csvfile)
    next(reader, None)
    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        month = row[0]
        count_months.append(month)
        profloss = int(row[1])
        list2.append(profloss)
    
        total_months = len(count_months)
        net_total = sum(list2)
        
    total_months = len(count_months)
    net_total = sum(list2)
    net_total_months = len(count_months)-1
    budget_diff = []

    for x in range(len(list2)-1):
        budget_diff.append(float(list2[x+1]) - float(list2[x]))
        new_net_total = sum(budget_diff)

# determining the average diff of profit/loss sum
average_net_change = new_net_total/net_total_months

# greatest increase and decrease (date and amount)
min_list2 = list2[list2.index(min(list2))] - list2[list2.index(min(list2))-1]
max_list2 = list2[list2.index(max(list2))] - list2[list2.index(max(list2))-1]

# Print out results
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_net_change,2)}")
print(f'Greatest Increase in Profits: {count_months[list2.index(max(list2))]} (${max_list2})')
print(f"Greatest Descrease in Profits: {count_months[list2.index(min(list2))]} (${min_list2})")

output_file = os.path.join("financial.txt")
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${net_total}"])
    csvwriter.writerow([f"Average Change: ${round(average_net_change,2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {count_months[list2.index(max(list2))]} (${max_list2})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {count_months[list2.index(min(list2))]} (${min_list2})"])