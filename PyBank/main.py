import os
import csv

#initialise variables
months = 0
total = 0
last_month =0
changes =0
avg_change = 0
greatest_increase =list()
greatest_decrease = list()

# path to collect data
pyBank_csv = os.path.join('budget_data.csv')

# prints results in terminal end exports identical output onto a textfile
def print_and_export_results(months, total, avg_change, greatest_increase, greatest_decrease ):

    results= list()
    results.append("Financial Analysis")
    results.append("----------------------------------")
    results.append(f'Total months: {months}')
    results.append(f'Total: ${total}')
    results.append(f'Average Change: ${avg_change}')
    results.append(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
    results.append(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')
    
    #creates a textfile 
    output = open("Pybank_results.txt", "w")
    
    #prints each string in output list and rites each string in results list as a line in the output textfile
    for str in results:
        print (str)
        output.write(str)
        output.write('\n')
    output.close()

#read in csv file
with open (pyBank_csv) as csvfile:
    csvreader= csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)  
    for row in csvreader:
        months= months +1              #month counter
        current_profit = int(row[1])    
        
        # changes is the sum of all the net changes from month to month
        # because of this, it only makes sense to start calculating it 
        # on month two, because we do not know the "last month" for month 1
        # this seems more honest than assuming than "last month" is 0 in 
        # month one when that is very unlikely to be true in reality
        if (months > 1):
            changes= changes + (current_profit-last_month)
        total = total + current_profit
        # when months == 1, greatest_increase and greatest_decrease are empty lists
        # they are initialized as empty and not as ["", 0] 
        # because of the offchance that the data is all positive or all negative
        # which would leave one of these lists as ["", 0] by the end of this function
        if ( months ==1 or current_profit > greatest_increase[1]):
            greatest_increase = [row[0], current_profit]
        if (months== 1 or current_profit < greatest_decrease[1]):
            greatest_decrease = [row[0], current_profit]
        
        last_month = current_profit

avg_change  = '%.2f'%(changes/months)
print (type(avg_change))
print_and_export_results(months, total, avg_change, greatest_increase, greatest_decrease)