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
				text = 'SLO, Minumum ' + str(numbers[0])
		if (text==''):
			text = 'NULL'
		product.append(text)
	return product
def make_csv(list):
	"""makes list into CSV"""
	return ",".join(list) # some times i forget how simple python is

url = "http://www.lcbapps.lcb.state.pa.us/webapp/product_management/psi_ProductListPage_Inter.asp?strPageNum="+"1"+"&selTyp=Spirits&selTypS=&selTypW=&selTypA=&searchCode=&searchPhrase=&CostRange=&selSale=&strFilter=&prevSortby=BrndNme&sortBy=BrndNme&sortDir=ASC"
soup = get_url(url)
num_items = num_items(soup)
print float(num_items/25)
items_retrived = 0

print num_items%25

if (num_items%25 ==0):
	pages = num_items/25
else:
	pages = (num_items/25)+1

print pages

for j in xrange(1,pages+1):

	url = "http://www.lcbapps.lcb.state.pa.us/webapp/product_management/psi_ProductListPage_Inter.asp?strPageNum="+str(j)+"&selTyp=Spirits&selTypS=&selTypW=&selTypA=&searchCode=&searchPhrase=&CostRange=&selSale=&strFilter=&prevSortby=BrndNme&sortBy=BrndNme&sortDir=ASC"
	soup = get_url(url)

	if ((num_items - items_retrived) > 25):
		ids = table_ids(25)
	else:
		ids = table_ids(num_items - items_retrived)
	rows = soup.findAll('tr')
	#print ids[1]
	#print rows[12]
	for count in xrange(0,len(ids)):
		#print ids[count]
		#print count
		product = parse_item(str(rows[ids[count]])+str(rows[ids[int(count)]+2]))
		print make_csv(product)
	items_retrived = items_retrived + 25




