# Election_analysis

## Project Overview
Analyzing congressional election data from the Colorado Board of Elections. 

Completed the following tasks: 
1. Calculated the total number of votes cast.
2. Got a complete list of candidates who received votes.
3. Calculated the total number of votes each candidate received.
4. Calculated the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculated the voter turnout for each county.
7. Calculated the percentage of votes from each county out of the total count
8. Determined the county with the highest turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.38.1

## Results 
The analysis of the election show that:

* There were 369,711 votes cast in the election. 

* The candidates were: 
    * Charles Casper Stockham 
    * Diana DeGettea
    * Raymon Anthony Doane. 

* The candidate results were: 
    * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes. 

* The winner of the election was:
    * Diana DeGette, with a winning percentage of 73.8% and winning vote count of 272,892. 

* The county results were:
    * Jefferson county had 10.5% of the vote and 38,855 votes.
    * Denver county had 82.8% of the vote and 306,055 votes.
    * Arapahoe county had 6.7% of the vote and 24,801 votes.

* The county with the largest voter turnout:
    * Denver county with a voting percentage of 82.8% and winning vote count of 306,055.


### Summary
This script can be used, with some modificatins, for other types of elections. Small edits/changes to variables will allow flexibility with election data. This script will output the analysis above, but with respect to the specific data provided. 
The following are three examples of script to modify to be used for other elections:
1. In the following code, change the file to load to the specific file containing data for a different election. In the second line of code, change the folder and text file name to the specific folder and name for the respective election data.
```
        ## add a variable to load a file from a path
        file_to_load = os.path.join("Resources", "election_results.csv")
        # add a variable to save the file to a path
        file_to_save = os.path.join("analysis", "election_analysis.txt")
```
2. In the following code, change the row indexes to the specific indexes where the respective data lies in the file for each row.
```
        candidate_name = row[2]
        county_name = row[1]
```
3. Change the following list and dictionary to gather whatever data is in question for the specific analysis. For example, if the analysis was focused on voter turnouts for different races, the county_list could be changed to race_list and county_votes could be changed to race_votes. 
```
        #create a county list and county votes dictionary
        county_list = []
        county_votes = {}
```
