# Election-Analysis

## Project Overview

Tom and Seth have a data set holding the result of a vote. We need to analyze the data to find out the election result. To break down, we need total vote cast; vote cast of each county; Candidates' result; who is the winner. 


## Election-Audit Results

- Total Votes: 369,711

- County Votes:
  * Jefferson : 38,855  (10.51%)
  * Denver : 306,055  (82.78%)
  * Arapahoe : 24,801  (6.71%)

- Largest County Turnout: 
  * Denver (306,055)

- Candidate Result:
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)

- Winning Detail:
  * Winner: Diana DeGette
  * Winning Vote Count: 272,892
  * Winning Percentage: 73.8%


![image](https://user-images.githubusercontent.com/48306359/125550133-75b0ff7f-039e-4d42-83c5-82a94b108359.png)


## Election-Audit Summary: 

In this Challenge, Python _os_ and _csv_ modules are imported. If another similar analysis will be performed, the data should be save into the Resources file, and the Path in the code should be modified.

### Refactoring for Condition I
For any election data, having the second column as Region name, and the third column as the candidates' name, we can run this code. Just replace 'County' with other region unit. (like Community, Class, Cities, etc.) 

### Refactoring for Condition II
If there's no county/region information, this code could also reusable. From line94 to line121, all the County analysis should be removed. As well as line 89 (f"County Votes:\n") should be removed as well.