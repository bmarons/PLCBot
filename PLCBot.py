from bs4 import BeautifulSoup
import requests
import re
import sys

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

def table_ids(num_page):
	ids = []
	x = 12
	for i in xrange(0,num_page):
		ids.append(x)
		x = x + 4
	return ids

def parse_item(item_dec):
	product = []
	blank = ''
	insoup = BeautifulSoup(item_dec)
	cells = insoup.findAll('td')
	cells.pop(2)
	cells.pop(6)
	for a,cell in enumerate(cells):
		text = cell.text.strip()
		if (a == 6):
			if text.startswith('SLO'):
				numbers = re.findall(r'\d+',text)
				if (not numbers):
					numbers.append(0)
				text = 'SLO Minumum ' + str(numbers[0])
		if (text==''):
			text = 'NULL'
		product.append(text)
	return product

def make_csv(list):
	"""makes list into CSV"""
	return ",".join(list) # some times i forget how simple python is

def read_file(filename):
	"""Reads a file into a list so it can be searched"""
	ret = []
	with open(filename, 'r') as f:
		for line in f.readlines():
			Product_ID,Name,Size,Vintage,Proof,Price,Avaliblity,Stock_Type,Spirit,Type,Vender_ID = line.strip().split(',')
			ret.append((Product_ID,Name,Size,Vintage,Proof,Price,Avaliblity,Stock_Type,Spirit,Type,Vender_ID))
	return ret
def search_type(inlist,search):
	ret = []
	for item in inlist:
		if search.upper() in item[9]:
			ret.append(item)
	return ret

def search_price(inlist,price,over):
	ret = []
	if (over):
		for item in inlist:
			if float(item[5]) >= price :
				ret.append(item)
	else:
		for item in inlist:
			if float(item[5]) < price :
				ret.append(item)
	return ret

def search_price_range(inlist,low,high):
	ret = []
	for item in inlist:
		if float(item[5]) < high and float(item[5]) > low:
				ret.append(item)
	return ret

