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
		self.assertEqual(test,5384)
	def test_table_ids(self):
		"""Test generating a list of table ids"""
		test_ids = PLCBot.table_ids(25)
		self.assertEqual(test_ids,[12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108])


if __name__ == '__main__':
    unittest.main()