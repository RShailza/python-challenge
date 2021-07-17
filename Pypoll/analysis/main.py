#!/usr/bin/env python
# coding: utf-8

# In[1]:


# creating dependencies 
import os 
import csv


# In[2]:


#Setting Variables 

total_votes = 0
candidate_vote_count = []
candidates_unique = []


# In[4]:


#Opening and readng csv file

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader, None)

#complete list of candidtates who received votes 
    for row in csvreader:
        # number of rows
        total_votes += 1
        
        #read candidates name form column 3 of csv
        candidate_name = (row[2])
        
        #if candidate in the list add 1
        if candidate_name in candidates_unique:
            candidate_index = candidates_unique.index(candidate_name)
            candidate_vote_count[candidate_index] += 1
        else:
            candidates_unique.append(candidate_name)
            candidate_vote_count.append(1)


# In[5]:


#variables for determining percent votes/candidate, total votes / candidate and winner by popular vote  
pct = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):
    #loop through candidate unique as x 
    vote_pct = round(candidate_vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x
        
    election_winner = candidates_unique[max_index] 


# In[7]:


print('=' * 50)
print('|                  Election Results                  |')
print('=' * 50)
print(f'Total Votes: {total_votes}')
print('~' * 50)
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print('~' * 50)
print(f'Election winner: {election_winner.upper()}')
print('~' * 50)


# In[10]:


#output txt file
output_file = os.path.join(".", "Analysis",  "pypoll_election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('======================================================\n')
    datafile.write('|                  Election Results                  |\n')
    datafile.write('======================================================\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    for x in range(len(candidates_unique)):
        datafile.write(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write(f'Election winner: {election_winner.upper()}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write("---END OF REPORT---")


# In[ ]:




