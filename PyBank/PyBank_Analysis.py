#Import dependencies
import os
import csv

#Open file
csvpath = os.path.join((os.path.abspath(__file__)), '..', 'Resources', 'budget_data.csv')

#Create empty lists to add the csv values to
month_count = []
profit = []
change_profit = []

# Open csv in read mode
with open(csvpath) as csvfile:

    # Store data under csvreader variable
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip the header so we go through the actual values
    header = next(csvreader)
                    
    # Go through the values and add them to the empty list 
    for row in csvreader:

        #Find the number of months
        month_count.append(row[0])

        #Find the row with profits profits
        profit.append(int(row[1]))

    #Create i variable to calculate change in profits; use len to find the sum of profits
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
#Calculate greatest increase in profits (date and amount) over entire period
increase = max(change_profit)
month_increase = change_profit.index(max(change_profit))+1

#Calculate greatest decrease in profits (date and amount) over entire period
decrease = min(change_profit)
month_decrease = change_profit.index(min(change_profit))+1

# Print the financial analysis
print("Financial Analysis")
print(f"Total Months: {len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})") 