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

	def test_table_ids_1000(self):
		"""Test generating a list of table ids"""
		test_ids = PLCBot.table_ids(1000)
		answer = [12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192, 196, 200, 204, 208, 212, 216, 220, 224, 228, 232, 236, 240, 244, 248, 252, 256, 260, 264, 268, 272, 276, 280, 284, 288, 292, 296, 300, 304, 308, 312, 316, 320, 324, 328, 332, 336, 340, 344, 348, 352, 356, 360, 364, 368, 372, 376, 380, 384, 388, 392, 396, 400, 404, 408, 412, 416, 420, 424, 428, 432, 436, 440, 444, 448, 452, 456, 460, 464, 468, 472, 476, 480, 484, 488, 492, 496, 500, 504, 508, 512, 516, 520, 524, 528, 532, 536, 540, 544, 548, 552, 556, 560, 564, 568, 572, 576, 580, 584, 588, 592, 596, 600, 604, 608, 612, 616, 620, 624, 628, 632, 636, 640, 644, 648, 652, 656, 660, 664, 668, 672, 676, 680, 684, 688, 692, 696, 700, 704, 708, 712, 716, 720, 724, 728, 732, 736, 740, 744, 748, 752, 756, 760, 764, 768, 772, 776, 780, 784, 788, 792, 796, 800, 804, 808, 812, 816, 820, 824, 828, 832, 836, 840, 844, 848, 852, 856, 860, 864, 868, 872, 876, 880, 884, 888, 892, 896, 900, 904, 908, 912, 916, 920, 924, 928, 932, 936, 940, 944, 948, 952, 956, 960, 964, 968, 972, 976, 980, 984, 988, 992, 996, 1000, 1004, 1008, 1012, 1016, 1020, 1024, 1028, 1032, 1036, 1040, 1044, 1048, 1052, 1056, 1060, 1064, 1068, 1072, 1076, 1080, 1084, 1088, 1092, 1096, 1100, 1104, 1108, 1112, 1116, 1120, 1124, 1128, 1132, 1136, 1140, 1144, 1148, 1152, 1156, 1160, 1164, 1168, 1172, 1176, 1180, 1184, 1188, 1192, 1196, 1200, 1204, 1208, 1212, 1216, 1220, 1224, 1228, 1232, 1236, 1240, 1244, 1248, 1252, 1256, 1260, 1264, 1268, 1272, 1276, 1280, 1284, 1288, 1292, 1296, 1300, 1304, 1308, 1312, 1316, 1320, 1324, 1328, 1332, 1336, 1340, 1344, 1348, 1352, 1356, 1360, 1364, 1368, 1372, 1376, 1380, 1384, 1388, 1392, 1396, 1400, 1404, 1408, 1412, 1416, 1420, 1424, 1428, 1432, 1436, 1440, 1444, 1448, 1452, 1456, 1460, 1464, 1468, 1472, 1476, 1480, 1484, 1488, 1492, 1496, 1500, 1504, 1508, 1512, 1516, 1520, 1524, 1528, 1532, 1536, 1540, 1544, 1548, 1552, 1556, 1560, 1564, 1568, 1572, 1576, 1580, 1584, 1588, 1592, 1596, 1600, 1604, 1608, 1612, 1616, 1620, 1624, 1628, 1632, 1636, 1640, 1644, 1648, 1652, 1656, 1660, 1664, 1668, 1672, 1676, 1680, 1684, 1688, 1692, 1696, 1700, 1704, 1708, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1740, 1744, 1748, 1752, 1756, 1760, 1764, 1768, 1772, 1776, 1780, 1784, 1788, 1792, 1796, 1800, 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2100, 2104, 2108, 2112, 2116, 2120, 2124, 2128, 2132, 2136, 2140, 2144, 2148, 2152, 2156, 2160, 2164, 2168, 2172, 2176, 2180, 2184, 2188, 2192, 2196, 2200, 2204, 2208, 2212, 2216, 2220, 2224, 2228, 2232, 2236, 2240, 2244, 2248, 2252, 2256, 2260, 2264, 2268, 2272, 2276, 2280, 2284, 2288, 2292, 2296, 2300, 2304, 2308, 2312, 2316, 2320, 2324, 2328, 2332, 2336, 2340, 2344, 2348, 2352, 2356, 2360, 2364, 2368, 2372, 2376, 2380, 2384, 2388, 2392, 2396, 2400, 2404, 2408, 2412, 2416, 2420, 2424, 2428, 2432, 2436, 2440, 2444, 2448, 2452, 2456, 2460, 2464, 2468, 2472, 2476, 2480, 2484, 2488, 2492, 2496, 2500, 2504, 2508, 2512, 2516, 2520, 2524, 2528, 2532, 2536, 2540, 2544, 2548, 2552, 2556, 2560, 2564, 2568, 2572, 2576, 2580, 2584, 2588, 2592, 2596, 2600, 2604, 2608, 2612, 2616, 2620, 2624, 2628, 2632, 2636, 2640, 2644, 2648, 2652, 2656, 2660, 2664, 2668, 2672, 2676, 2680, 2684, 2688, 2692, 2696, 2700, 2704, 2708, 2712, 2716, 2720, 2724, 2728, 2732, 2736, 2740, 2744, 2748, 2752, 2756, 2760, 2764, 2768, 2772, 2776, 2780, 2784, 2788, 2792, 2796, 2800, 2804, 2808, 2812, 2816, 2820, 2824, 2828, 2832, 2836, 2840, 2844, 2848, 2852, 2856, 2860, 2864, 2868, 2872, 2876, 2880, 2884, 2888, 2892, 2896, 2900, 2904, 2908, 2912, 2916, 2920, 2924, 2928, 2932, 2936, 2940, 2944, 2948, 2952, 2956, 2960, 2964, 2968, 2972, 2976, 2980, 2984, 2988, 2992, 2996, 3000, 3004, 3008, 3012, 3016, 3020, 3024, 3028, 3032, 3036, 3040, 3044, 3048, 3052, 3056, 3060, 3064, 3068, 3072, 3076, 3080, 3084, 3088, 3092, 3096, 3100, 3104, 3108, 3112, 3116, 3120, 3124, 3128, 3132, 3136, 3140, 3144, 3148, 3152, 3156, 3160, 3164, 3168, 3172, 3176, 3180, 3184, 3188, 3192, 3196, 3200, 3204, 3208, 3212, 3216, 3220, 3224, 3228, 3232, 3236, 3240, 3244, 3248, 3252, 3256, 3260, 3264, 3268, 3272, 3276, 3280, 3284, 3288, 3292, 3296, 3300, 3304, 3308, 3312, 3316, 3320, 3324, 3328, 3332, 3336, 3340, 3344, 3348, 3352, 3356, 3360, 3364, 3368, 3372, 3376, 3380, 3384, 3388, 3392, 3396, 3400, 3404, 3408, 3412, 3416, 3420, 3424, 3428, 3432, 3436, 3440, 3444, 3448, 3452, 3456, 3460, 3464, 3468, 3472, 3476, 3480, 3484, 3488, 3492, 3496, 3500, 3504, 3508, 3512, 3516, 3520, 3524, 3528, 3532, 3536, 3540, 3544, 3548, 3552, 3556, 3560, 3564, 3568, 3572, 3576, 3580, 3584, 3588, 3592, 3596, 3600, 3604, 3608, 3612, 3616, 3620, 3624, 3628, 3632, 3636, 3640, 3644, 3648, 3652, 3656, 3660, 3664, 3668, 3672, 3676, 3680, 3684, 3688, 3692, 3696, 3700, 3704, 3708, 3712, 3716, 3720, 3724, 3728, 3732, 3736, 3740, 3744, 3748, 3752, 3756, 3760, 3764, 3768, 3772, 3776, 3780, 3784, 3788, 3792, 3796, 3800, 3804, 3808, 3812, 3816, 3820, 3824, 3828, 3832, 3836, 3840, 3844, 3848, 3852, 3856, 3860, 3864, 3868, 3872, 3876, 3880, 3884, 3888, 3892, 3896, 3900, 3904, 3908, 3912, 3916, 3920, 3924, 3928, 3932, 3936, 3940, 3944, 3948, 3952, 3956, 3960, 3964, 3968, 3972, 3976, 3980, 3984, 3988, 3992, 3996, 4000, 4004, 4008]
		self.assertEqual(test_ids,answer)

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