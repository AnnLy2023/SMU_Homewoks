import  csv 

cvs_file = "C:/Users/Home/OneDrive/Desktop/SMU BOOT CAMP 2023/2/Activities/GitHub/SMU_Homewoks/03-Python/PyPoll/Resources/election_data.csv"

total_votes = 0

candidates = {}

with open(cvs_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        total_votes += 1
       
    #get candidate, add 1 if candidate in the dictionary, if not, start 1 vote for them
        candidate=row[2]
        if candidate in candidates.keys():
            candidates[candidate] +=1
        else: 
            candidates[candidate] = 1

    print(f"Total Votes: {total_votes}")
    print(candidates)

    for key in candidates:
        print(key, 100*candidates[key]/total_votes)
        

                   
