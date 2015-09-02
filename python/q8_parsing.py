#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv

  def read_data(data):
	with open(data, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		parsed_data = list(reader)
	return parsed_data

def get_min_score_difference(self, parsed_data):
	current_min = 100
	for team in parsed_data:
		diff = team[6] - team[7]
		if diff < current_min:
			current_min = diff

	return current_min   

def get_team(self, index_value, parsed_data):
    team = parsed_data[index_value][0]
    return team
