#coding: utf8

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


import math
def euclidean_metric(data, person1, person2):

	if(len([item for item in data[person1] if item in data[person2]]) == 0):
		return 0

	sum_of_squares = sum([(data[person1][item] - data[person2][item]) * (data[person1][item] - data[person2][item])\
		for item in data[person1] if item in data[person2]])
	return 1 / (1 + math.sqrt(sum_of_squares))

def pearson_metric(data, person1, person2):
	pass

def main():
	print euclidean_metric(critics, 'Lisa Rose', 'Gene Seymour')
	for person1 in critics:
		for person2 in critics:
			print euclidean_metric(critics, person1, person2)

if __name__ == '__main__':
	main()