#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import unittest
import PLCBot
import requests
from bs4 import BeautifulSoup

class Test(unittest.TestCase):

	def setUp(self):
		page  = requests.get("http://blue.betadevbox.com/test.html")
		data = page.text
		soup = BeautifulSoup(data)
		self.tsoup = soup


	def test_get_url(self):
		"""This Test sends a URL to a function and should get back a soup object"""
		testSoup = PLCBot.get_url("http://example.com/")
		self.assertEqual(str(testSoup.html.head.title),"<title>Example Domain</title>")

	def test_num_items(self):
		"""This tests the function that returns the number of items on the search"""
		test = PLCBot.num_items(self.tsoup)
		self.assertEqual(test,5391)

	def test_table_ids(self):
		"""Test generating a list of table ids"""
		test_ids = PLCBot.table_ids(25)
		self.assertEqual(test_ids,[12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108])

	def test_table_ids_other(self):
		"""Test generating a list of table ids"""
		test_ids = PLCBot.table_ids(20)
		self.assertEqual(test_ids,[12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88])

	def test_table_ids_1(self):
		"""Test generating a list of table ids"""
		test_ids = PLCBot.table_ids(1)
		self.assertEqual(test_ids,[12])

	def test_table_ids_1(self):
		"""Test generating a list of table ids"""
		test_ids = PLCBot.table_ids(-1)
		self.assertEqual(test_ids,[])

	def test_parse_item(self):
		"""This tests the parseing of HTML Items"""
		HTML = '<tr bgcolor="#EEEEEE" height="1"><!--td align="right" valign="middle"><b><font face=Verdana size=1><=intRecCount%></font></b></td--><td align="right" valign="middle"><a href="psi_ProductLocation_inter.asp?cdeNo=8886" target="_blank"><b><font size="1">8886</font></b></a></td><td><table width="100%"><tr><td><b><font size="1">10 Cane Rum</font></b></td></tr></table></td><td align="center" valign="middle"><b><font size="1">750 ML</font></b></td><td align="center" valign="middle"><b><font size="1"></font></b></td><td align="left" valign="middle"><b><font size="1">80</font></b></td><td align="right" valign="middle"><b><font size="1"><font size="1">17.99</font></font></b></td></tr><tr bgcolor="#EEEEEE" height="1"><!--td>&nbsp;</td--><td> </td><td align="left" valign="middle"><font size="1">Regular</font></td><td align="center" valign="middle"><font size="1">Closeout</font></td><td align="center" valign="middle"><font size="1">Spirit</font></td><td align="left" valign="middle"><font size="1">RUMS (IMPORTED)</font></td><td> </td><!--/tr></table></td--></tr>'
		item = PLCBot.parse_item(HTML)
		self.assertEqual(item,[u'8886', u'10 Cane Rum', u'750 ML', 'NULL', u'80', u'17.99', u'Regular', u'Closeout', u'Spirit', u'RUMS (IMPORTED)', 'NULL'])
	def test_make_csv(self):
		"""Tests makeing a list into a CSV"""
		self.assertEqual("8886,10 Cane Rum,750 ML,NULL,80,17.99,Regular,Closeout,Spirit,RUMS (IMPORTED),NULL",PLCBot.make_csv([u'8886', u'10 Cane Rum', u'750 ML', 'NULL', u'80', u'17.99', u'Regular', u'Closeout', u'Spirit', u'RUMS (IMPORTED)', 'NULL']))

	def test_read_file(self):
		comp = [('8886', '10 Cane Rum', '750 ML', 'NULL', '80', '17.99', 'Regular', 'Closeout', 'Spirit', 'RUMS (IMPORTED)', 'NULL'), ('34361', '123 Tequila Anejo Organic 80 Proof', '750 ML', 'NULL', 'NULL', '63.99', 'Luxury', 'NULL', 'Spirit', 'TEQUILA', 'NULL'), ('34360', '123 Tequila Blanco Organic 80 Proof', '750 ML', 'NULL', 'NULL', '42.99', 'Luxury', 'NULL', 'Spirit', 'TEQUILA', 'NULL')]
		test = PLCBot.read_file("TestFile.txt")
		self.assertEqual(test,comp)

	def test_search_type(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer = [('8886', '10 Cane Rum', '750 ML', 'NULL', '80', '17.99', 'Regular', 'Closeout', 'Spirit', 'RUMS (IMPORTED)', 'NULL')]
		self.assertEqual(PLCBot.search_type(test_list, "RUM"),answer)

	def test_search_type_num(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer = []
		self.assertEqual(PLCBot.search_type(test_list, "PineApplePineApplePineApplePineApplePineApplePineApplePineApple22CATS"),answer)

	def test_search_type_lowercase(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer = [('8886', '10 Cane Rum', '750 ML', 'NULL', '80', '17.99', 'Regular', 'Closeout', 'Spirit', 'RUMS (IMPORTED)', 'NULL')]
		self.assertEqual(PLCBot.search_type(test_list, "rum"),answer)

	def test_search_type_none(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer =[]
		self.assertEqual(PLCBot.search_type(test_list, "dkaskjdhasdhDCBNZXNMCBZXMNCBIR	IQURYUR"),answer)

	def test_search_price_under(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer = [('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL')]
		self.assertEqual(PLCBot.search_price(test_list, 15,False),answer)
	
	def test_search_price_under_none(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer =[]
		self.assertEqual(PLCBot.search_price(test_list, 5,False),answer)

	def test_search_price_over_none(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer =[]
		self.assertEqual(PLCBot.search_price(test_list, 100,True),answer)
	
	def test_search_price_under_none_neg(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer =[]
		self.assertEqual(PLCBot.search_price(test_list, -120,False),answer)

	def test_search_price_over(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		self.assertEqual(PLCBot.search_price(test_list, 15,True),answer)
	
	def test_search_price_range(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060')]
		self.assertEqual(PLCBot.search_price_range(test_list,15,60),answer)

	def test_search_price_range_none(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer =[]		
		self.assertEqual(PLCBot.search_price_range(test_list,100,200),answer)

	def test_search_price_range_none_neg(self):
		test_list = [('8886','10 Cane Rum','750 ML','NULL','80','17.99','Regular','Closeout','Spirit','RUMS (IMPORTED)','NULL'),('545382','2 Gingers Irish Whiskey 80 Proof','1 L','NULL','80','22.79','SLO', 'Minumum 12','NULL','Spirit','IRISH WHISKEY','8060'),('5242','99 Blackberries Schnapps','750 ML','NULL','99','10.99','Regular','Closeout','Spirit','SCHNAPPS - OTHER (U.S.)','NULL'),('71195','Aberlour Single Malt Single Malt Scotch 16 Year Old 86 Proof','750 ML','NULL','86','70.09','SLO', 'Minumum 6','NULL','Spirit','SINGLE MALT SCOTCH','8060')]
		answer =[]		
		self.assertEqual(PLCBot.search_price_range(test_list,-100,-200),answer)


if __name__ == '__main__':
    unittest.main()