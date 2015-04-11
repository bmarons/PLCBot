from bs4 import BeautifulSoup
import requests
import re


def get_url(url):
	"""Returns Soup Object of the given URL"""
	page  = requests.get(url)
	data = page.text
	soup = BeautifulSoup(data)
	return soup