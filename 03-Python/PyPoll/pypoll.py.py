import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('PyPoll/Resources/election_data.csv')

# Task 1: Total number of votes cast
total_votes = len(df)

# Task 2: List of candidates who received votes
candidates = df['Candidate'].unique()

# Task 3 and 4: Percentage and total number of votes each candidate won
candidate_votes = df['Candidate'].value_counts()
percentage_votes = (candidate_votes / total_votes) * 100

# Task 5: Winner of the election based on popular vote
winner = candidate_votes.idxmax()

# Print the results
print(f'Election Results')
print(f'-------------------------------')
print(f"Total Votes: {total_votes}")
print(f"--------------------------------")

for candidate in candidates:
    print(f"{candidate}: {percentage_votes[candidate]:.2f}% ({candidate_votes[candidate]})")

print(f"\nWinner: {winner}")
print('----------------------------------')


output_path = "PyPoll/Analysis/pypoll_analysis.txt"

with open(output_path, 'w') as textfile:
    textfile.write(f'Election Results\n')
    textfile.write(f'-------------------------------\n')
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write(f"--------------------------------\n")

    for candidate in candidates:
        textfile.write(f"{candidate}: {percentage_votes[candidate]:.2f}% ({candidate_votes[candidate]})\n")

    textfile.write(f"\nWinner: {winner}\n")

print(f"Results saved to {output_path}")




