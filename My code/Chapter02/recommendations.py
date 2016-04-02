# coding: utf8
from math import *

critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}


def euclidean_metric(data, person1, person2):
	if len([item for item in data[person1] if item in data[person2]]) == 0:
		return 0
	sum_of_squares = sum([(data[person1][item] - data[person2][item]) * (data[person1][item] - data[person2][item]) for item in data[person1] if item in data[person2]])
	return 1 / (1 + sqrt(sum_of_squares))


def pearson_metric(data, person1, person2):
	si = {}
	for item in data[person1]:
		if item in data[person2]:
			si[item] = 1
	if len(si) == 0:
		return 1
	sum1 = sum(data[person1][item] for item in si)
	sum2 = sum(data[person2][item] for item in si)

	sum1sq = sum([data[person1][item] * data[person1][item] for item in si])
	sum2sq = sum([data[person2][item] * data[person2][item] for item in si])

	pSum = sum([data[person1][item] * data[person2][item] for item in si])

	num = pSum - (sum1 * sum2 / len(si))
	den = sqrt((sum1sq - sum1 * sum1 / len(si)) * (sum2sq - sum2 * sum2 / len(si)))

	return 0 if den == 0 else num / den


def topMatches(data, person, n=5, metric=pearson_metric):
	metrics = [(metric(data, person, other), other) for other in data if other != person]
	metrics.sort()
	metrics.reverse()
	return metrics[0: n]


def getRecommendations(data, person, metric=pearson_metric):
	totals = {}
	simSums = {}

	for other in data:
		if other == person:
			continue
		sim = metric(data, person, other)
		if sim <= 0:
			continue
		for item in data[other]:
			if item not in data[person] or data[person][item] == 0:
				totals.setdefault(item, 0)
				totals[item] += data[other][item] * sim
				simSums.setdefault(item, 0)
				simSums[item] += sim
	rankings = [(total / simSums[item], item) for item, total in totals.items()]
	rankings.sort()
	rankings.reverse()
	return rankings


def transformPrefs(prefs):
	result = {}
	for item1 in prefs:
		for item2 in prefs[item1]:
			result.setdefault(item2, {})
			result[item2][item1] = prefs[item1][item2]
	return result


def main():
	print euclidean_metric(critics, 'Lisa Rose', 'Gene Seymour')
	print pearson_metric(critics, 'Lisa Rose', 'Gene Seymour')
	for person1 in critics:
		for person2 in critics:
			print euclidean_metric(critics, person1, person2)

	print topMatches(critics, 'Toby')
	print getRecommendations(critics, 'Toby')

	print topMatches(transformPrefs(critics), 'Superman Returns')


if __name__ == '__main__':
	main()
