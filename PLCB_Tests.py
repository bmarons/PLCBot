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
		self.fail("This is a fail")


if __name__ == '__main__':
    unittest.main()