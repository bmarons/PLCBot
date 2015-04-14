import PLCBot
import random
items = PLCBot.read_file("Output.txt")
search = raw_input("Enter a type of liquor (vodka or scotch)")
typelist = PLCBot.search_type(items, search)
maxprice = raw_input("Enter the max you want to spend ")
minprice = raw_input("Enter the min you want to spend ")
pricelist = PLCBot.search_price_range(typelist,int(minprice),int(maxprice))
if len(pricelist) > 1:
	print PLCBot.make_csv(random.choice(pricelist))
else:
	print "Your search returned no results"