import csv
import os

# Define the file path
csv_path = "PyBank/Resources/budget_data.csv"

# Initialize variables
total_months = 0
total_net = 0
changes = []
max_change = -9999999999
max_month = ""
min_change = 9999999999
min_month = ""

# Read the CSV file
with open(csv_path) as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # Read the header row
    header = next(csvreader)

    for row in csvreader:
        # Calculate total months and net profit/loss
        total_months += 1
        total_net += int(row["Profit/Losses"])

        # Calculate changes in profit/loss
        current_value = int(row["Profit/Losses"])
        if total_months == 1:
            last_value = current_value
        else:
            change = current_value - last_value
            changes.append(change)
            last_value = current_value

            # Track greatest increase and decrease
            if change > max_change:
                max_change = change
                max_month = row["Date"]
            if change < min_change:
                min_change = change
                min_month = row["Date"]

# Calculate average change
average_change = sum(changes) / len(changes)

# Print the analysis to terminal
output = f'''Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})
'''

print(output)

# Save output to a text file
output_name = "financial_analysis.txt"
output_folder = "PyBank/Pybank_Analysis"
output_path = os.path.join(output_folder, output_name)
with open(output_path, 'w') as textfile:
    textfile.write(output)

print(f"Analysis results saved to {output_path}")

   