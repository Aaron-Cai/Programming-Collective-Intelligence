# coding: utf8

from pydelicious import get_popular, get_urlposts, get_userposts


def initializeUserDict(tag, count=5):
	user_dict = {}
	for pl in get_popular(tag=tag)[0:count]:
		try:
			for p2 in get_urlposts(pl['href']):
				user = p2['user']
				print 'Collecting user info ', user
				user_dict[user] = {}
		except:
			continue
	return user_dict


def fillItems(user_dict):
	all_items = {}
	for user in user_dict:
		for i in range(3):
			try:
				posts = get_userposts(user)
				break
			except Exception:
				print 'Failed user', user, ", retrying"
		for post in posts:
			url = post['href']
			user_dict[user][url] = 1.0
			all_items[url] = 1
	for ratings in user_dict.values():
		for item in all_items:
			if item not in ratings:
				ratings[item] = 0.0


def main():
	# print get_popular(tag='programming')
	delusers = initializeUserDict('programming')
	print 'Sucessfully collecting ', len(delusers), 'users'
	print delusers
	fillItems(delusers)
	print delusers


if __name__ == '__main__':
	main()
