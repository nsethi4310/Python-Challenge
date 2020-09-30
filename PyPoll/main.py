import os
import csv

#Getting the file from the location
election = os.path.join('./Resources/election_data.csv')

#declaring and initiating variables
rowcount=0
lstofCandidate= []


#Opening  the file as read only and assigning to variable

with open(election,'r') as csvfile:
# Adding variable to the content of file
    election_reader = csv.reader(csvfile, delimiter=',')

   #Getting the header or row#1
    csv_header = next(election_reader)
    
    #print(csv_header)
    
    
    #looping through each row in the budget_reader
    for row in election_reader:
     rowcount = rowcount+1
     #candidate = lstofCandidate.append(row[2])
     #print(candidate[1])

      
print("Total_votes  :"+str(rowcount))     

#Printing to output file
output_path = os.path.join("./Analysis/output.txt")

with open(output_path, 'w') as txtfile:
    txtfile.writelines("Election Results")
    txtfile.write('\n')
    txtfile.writelines("---------------------")
    txtfile.write('\n')
    txtfile.write("Total votes : " + str(rowcount))
    txtfile.write('\n')
    