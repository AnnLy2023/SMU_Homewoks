import csv

csv_path = "C:/Users/Home/OneDrive/Desktop/SMU BOOT CAMP 2023/2/Activities/GitHub/SMU_Homewoks/03-Python/PyBank/Resources/budget_data.csv"

#set variables

months=0
total_profit=0
#there shouldn't be any changes in the first month, therefore set first month = 0 ... 
is_first_row=True
last_month_profit = 0 
changes = []

max_change = -9999999999
max_month = []

min_change = 9999999999
min_month = ""


#notes: delimiter is a character that separates item in a string, in this case, a comma
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        print(row)

        row_profit = int(row[1])
        #1st month profit - 0 
        if is_first_row:
            last_month_profit=row_profit
            is_first_row=False
        else:
            change=row_profit-last_month_profit
            changes.append(change)

            last_month_profit=row_profit

            if change > min_change:
                max_change=change
                max_month=row[0]
            if change < min_change:
                min_change = change
                min_month = row[0]


        
        months +=1
        total_profit += int(row[1])

    print("***********************************************************************************")
    #Print the analysis to termimal
    
    print ("Financial Analysis")

    print(f"Total Months : {months}")
    print(f"Total: {total_profit}")

    avg_changes = sum(changes) /len(changes)
    print(f"Average Change: ${avg_changes}")

    print(f"Greatest Increase in Profits: {max_month}, (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month}, (${min_change})") 



   






 

