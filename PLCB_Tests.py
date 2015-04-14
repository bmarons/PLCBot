#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import unittest
import PLCBot
import requests
from bs4 import BeautifulSoup

class Test(unittest.TestCase):

	def setUp(self):
		page  = requests.get("http://www.lcbapps.lcb.state.pa.us/webapp/product_management/psi_ProductListPage_Inter.asp?strPageNum="+"1"+"&selTyp=Spirits&selTypS=&selTypW=&selTypA=&searchCode=&searchPhrase=&CostRange=&selSale=&strFilter=&prevSortby=BrndNme&sortBy=BrndNme&sortDir=ASC")
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
		self.assertEqual(test,5393)
	def test_table_ids(self):
		"""Test generating a list of table ids"""
		test_ids = PLCBot.table_ids(25)
		self.assertEqual(test_ids,[12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108])

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
		self.fail()

if __name__ == '__main__':
    unittest.main()