import os
import csv
import numpy
import string

#Getting the file from the location
budget_r = os.path.join('./Resources/budget_data.csv')

#Declaring and initializing the variables
average_change = []
rowcount =0
plsum=0
average=0
prev_col=0
next_col=0
i=2 
avg_change=0
laverage=0
max_change=0
min_change=0
month_list=[]
Inc_lt  = ["",9999]
Dec_lt= ["",0]


#Opening  the file as read only and assigning to variable

with open(budget_r,'r') as csvfile:
# Adding variable to the content of file
    budget_reader = csv.reader(csvfile, delimiter=',')

    
#Getting the header or row#1
    csv_header = next(budget_reader)
    
    print(csv_header)
     
#looping through each row in the budget_reader
    for row in budget_reader:

       #Calculating total months              
        rowcount = rowcount+1
        #Calculating total profit and Loss Sum
        plsum= int(row[1]) + plsum
        #Getting average change and storing in a list
        average=int(row[1])-prev_col
        prev_col=int(row[1])
        average_change.append(average)
        #Getting the greatest increase and month
        if average> Inc_lt[1]:
            Inc_lt[0] = row[0]
            Inc_lt[1] = average
        #Getting the greatest decrease and month
        if average< Dec_lt[1]:
            Dec_lt[0]=row[0]
            Dec_lt[1]= average

  
            
         
                
               
 #Deleting First element of array       
average_change.pop(0)
#Calculating average of change
laverage= sum(average_change)/len(average_change)


        
       
#Print Statments
print("Financial Analysis")
print("---------------------")
print("Total months : "+ str(rowcount))
print("Total Profit is $" +str(plsum))
print("Average increase/decrease is $"+ str(round(laverage,2)))
# print("Greatest Increase in Profits: "+ str(max_change))
# print("Greatest Decrease in Profits: "+ str(min_change))
print("Greatest Increase in Profits in "+ (Inc_lt[0]) +" is $ " + str(Inc_lt[1]))
print("Greatest Decrease in Profits in " + (Dec_lt[0]) +" is $" + str(Dec_lt[1]))




#Printing to output file
output_path = os.path.join("./Analysis/output.txt")

with open(output_path, 'w') as txtfile:
    
    txtfile.writelines("Financial Analysis")
    txtfile.write('\n')
    txtfile.writelines("---------------------")
    txtfile.write('\n')
    txtfile.write("Total months : " + str(rowcount))
    txtfile.write('\n')
    txtfile.write("Total Profit is $" +str(plsum))
    txtfile.write('\n')
    txtfile.write("Average increase/decrease is $"+ str(round(laverage,2)))
    txtfile.write('\n')
    txtfile.write("Greatest Increase in Profits in "+ (Inc_lt[0]) +" is $ " + str(Inc_lt[1]))
    txtfile.write('\n')
    txtfile.write("Greatest Decrease in Profits in " + (Dec_lt[0]) +" is $" + str(Dec_lt[1]))
