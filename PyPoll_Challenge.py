# Add our dependencies
import csv
import os

## add a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# add a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# create a candidate options list and candidate votes dictionary
candidate_options = []
candidate_votes = {}

# create a county list and county votes dictionary
county_list = []
county_votes = {}


# Initiaize an empty string that will hold the county name for the county with the largest turnout
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# track largest county and county voter turnout
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # read election results from each row and get county name
    for row in reader:

        # add to the toal vote count
        total_votes = total_votes + 1

        # get the candidate name
        candidate_name = row[2]

        # check if candidate name is in list
        if candidate_name not in candidate_options:

            # add candidate name to candidate list if not in it
            candidate_options.append(candidate_name)

            # begin tracking that candidates voter count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        county_name = row[1]
        # write an if statement that checks that the county does not match any 
        # county in the county
        if county_name not in county_list:

            # add county name to county list
            county_list.append(county_name)

            #begin tracking county voter count
            county_votes[county_name] = 0

        # add vote to that county's count
        county_votes[county_name] += 1

# save the results to our text file
with open(file_to_save, "w") as txt_file:

    # print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # write a for loop to get the county from the county dictionary
    for county_name in county_votes: 

        # retrieve the county vote count
        c_votes = county_votes.get(county_name)
        # calculate the percentage of votes for the county
        vote_p = float(c_votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_p:.1f}% ({c_votes:,})\n")
        # print the county results to the terminal
        print(county_results)
        # save the county votes to a text file
        txt_file.write(county_results)

        # determine the winning county
        if (c_votes > winning_county_count) and (vote_p > winning_county_percentage):
            winning_county_count = c_votes
            winning_county = county_name
            winning_county_percentage = vote_p

    # print the county with the largest turnout to terminal
    winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    # print winning candidate to the terminal
    print(winning_county_summary)

    # save the county with the largest turnout to a text file
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)



