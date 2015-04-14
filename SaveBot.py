import PLCBot

f = open("Output.txt",'w')
url = "http://www.lcbapps.lcb.state.pa.us/webapp/product_management/psi_ProductListPage_Inter.asp?strPageNum="+"1"+"&selTyp=Spirits&selTypS=&selTypW=&selTypA=&searchCode=&searchPhrase=&CostRange=&selSale=&strFilter=&prevSortby=BrndNme&sortBy=BrndNme&sortDir=ASC"
soup = PLCBot.get_url(url)
num_items = PLCBot.num_items(soup)
items_retrived = 0

if (num_items%25 ==0):
	pages = num_items/25
else:
	pages = (num_items/25)+1

for j in xrange(1,pages+1):

	url = "http://www.lcbapps.lcb.state.pa.us/webapp/product_management/psi_ProductListPage_Inter.asp?strPageNum="+str(j)+"&selTyp=Spirits&selTypS=&selTypW=&selTypA=&searchCode=&searchPhrase=&CostRange=&selSale=&strFilter=&prevSortby=BrndNme&sortBy=BrndNme&sortDir=ASC"
	soup = PLCBot.get_url(url)

	if ((num_items - items_retrived) > 25):
		ids = PLCBot.table_ids(25)
	else:
		ids = PLCBot.table_ids(num_items - items_retrived)
	rows = soup.findAll('tr')
	for count in xrange(0,len(ids)):
		product = PLCBot.parse_item(str(rows[ids[count]])+str(rows[ids[int(count)]+2]))
		clean_string = PLCBot.make_csv(product)
		clean_string = clean_string.encode('ascii', 'ignore').decode('ascii')
		print clean_string
		f.write(clean_string+"\n")
	items_retrived = items_retrived + 25



