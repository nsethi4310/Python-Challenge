import os
import csv


#Getting the file from the location
election = os.path.join('./Resources/election_data.csv')

#Declaring and initializing the variables
rowcount = 0
votenamepercent = {}
unqlsitofcandidate = []
votecount =[]
average_votecount=[]
i = 1
votenamepercentnew={}


#Opening  the file as read only and assigning to variable

with open(election,'r') as csvfile:
# Adding variable to the content of file
    election_reader = csv.reader(csvfile, delimiter=',')

    
#Getting the header or row#1
    csv_header = next(election_reader)
    
    #print(csv_header)
     
#looping through each row in the file
    for row in election_reader:

       #Calculating total votes           
        rowcount = rowcount+1
        #Gettilng list of candidates and percentage of votes
        if row[2] not in unqlsitofcandidate:
            unqlsitofcandidate.append(row[2])
            votenamepercent[row[2]] = 0 
        votenamepercent[row[2]] = votenamepercent[row[2]] + 1
for x in votenamepercent:
    votenamepercentnew[x]=round(votenamepercent[x]*100/rowcount,2)
#Getting the winner     
max_dict = max(votenamepercentnew, key=votenamepercentnew.get)
        
         
                
               
 
     
  
#Print Statment
print("-------Votes Analysis-------------")
print("Total_votes  :"+str(rowcount))
for a,y in votenamepercentnew.items():
    print((a,y))
    
print("Winner is ...:" + max_dict)

#Printing to output file
output_path = os.path.join("./Analysis/output.txt")

with open(output_path, 'w') as txtfile:
    
    txtfile.writelines("Votes Analysis")
    txtfile.writelines("---------------------")
    txtfile.write('\n')
    txtfile.write("Total votes : " + str(rowcount))
    txtfile.write('\n')
    txtfile.write("Candidates and Percentage of Votes")
    txtfile.write('\n')
    txtfile.write(str(votenamepercentnew))
    txtfile.write('\n')
    txtfile.write("Winner is ....:"+" "+ max_dict)





    
    
