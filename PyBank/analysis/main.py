#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Creating dependencies
import os
import csv


# In[ ]:


# Setting Variables
count_months = []
total_months = 0
net_change = []
average_net_change = 0
list_2 = []


# In[ ]:


#Opening and readng csv file

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   
   next(csvreader, None)
#     print(csvreader)
#     csv_header = next(csvreader)
#     print(f"CSV Header: {csv_header}")

   for row in csvreader:
       month = row[0]
       count_months.append(month)
       
       #print(count_months)
       
       profloss = int(row[1])
       list_2.append(profloss)
       
       #print(list_2)
       
       total_months = len(count_months)
       #print (total_months)
       net_total = sum(list_2)
       #print(net_total)
           


# In[ ]:


#calculating the average of the changes in "Profit/Losses" over the entire period
#to calculte the avergage changes between the month we will have to subtract 1 form 
#the length since it will be one value less for example: if we have a list 
# list = [10,20,50,65,90]... here length is 5 however when looking at the net change between values tghe length will be 4

net_total_months = len(count_months)-1
budget_diff = []

for x in range(len(list_2)-1):
        budget_diff.append(float(list_2[x+1]) - float(list_2[x]))
        new_net_total = sum(budget_diff)

# determining the average diff of profit/loss sum
average_net_change = new_net_total/net_total_months
print(average_net_change)


# In[ ]:


# greatest increase and decrease (date and amount)
min_list_2 = list_2[list_2.index(min(list_2))] - list_2[list_2.index(min(list_2))-1]
max_list_2 = list_2[list_2.index(max(list_2))] - list_2[list_2.index(max(list_2))-1]

print(min_list_2)
print(max_list_2)


# In[ ]:


print("Financial Analysis")
print("-" * 50)
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_net_change,2)}")
print(f'Greatest Increase in Profits: {count_months[list_2.index(max(list_2))]} (${max_list_2})')
print(f"Greatest Descrease in Profits: {count_months[list_2.index(min(list_2))]} (${min_list_2})")


# In[ ]:


output_file = os.path.join(".", "analysis", "financial.txt")
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${net_total}"])
    csvwriter.writerow([f"Average Change: ${round(average_net_change,2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {count_months[list_2.index(max(list_2))]} (${max_list_2})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {count_months[list_2.index(min(list_2))]} (${min_list_2})"])


# In[ ]:




