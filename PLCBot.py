from bs4 import BeautifulSoup
import requests
import re


def get_url(url):
	"""Returns Soup Object of the given URL"""
	page  = requests.get(url)
	data = page.text
	soup = BeautifulSoup(data)
	return soup

def num_items(in_soup):
	"""gets the number of items in the search"""
	array = in_soup.body.findAll(text=re.compile('Total Number of Records'))
	numbers = re.findall(r'\d+',array[0])
	return int(numbers[0]+numbers[1])
