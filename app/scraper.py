import bs4, requests

def article_scraper(url):
	response = requests.get(url)
	text = ''

	# try story-body-text class for older articles
	soup = bs4.BeautifulSoup(response.text).select('p.story-body-text')

	if not soup:
		soup = bs4.BeautifulSoup(response.text).select('p')
		soup.pop(-1)
		# print soup

	for i in soup:
		text += i.get_text()
	
	# print text
	return text
