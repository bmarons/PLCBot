import unittest
import PLCBot

class TestUM(unittest.TestCase):


	def test_get_url(self):
		"""This Test sends a URL to a function and should get back a soup object"""
		testSoup = PLCBot.get_url("http://example.com/")
		self.assertEqual(str(testSoup.html.head.title),"<title>Example Domain</title>")

	def test_get_url(self):
		"""This tests the function that returns the number of items on the search"""
		self.fail("Not Written")


if __name__ == '__main__':
    unittest.main()