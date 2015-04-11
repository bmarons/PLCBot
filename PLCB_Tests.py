import unittest
import PLCBot

class TestUM(unittest.TestCase):
	def test_get_url(self):
		"""This Test sends a URL to a function and should get back a soup object"""
		testSoup = PLCBot.get_url("http://example.com/")
		self.assertEqual(str(testSoup.html.head.title),"<title>Example Domain</title>")

if __name__ == '__main__':
    unittest.main()