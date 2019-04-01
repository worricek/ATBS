#! /usr/bin/python

#2048	is	a	simple	game	where	you	combine	tiles	by	sliding	them	up,	down,	left,	or	right
#with	the	arrow	keys.	You	can	actually	get	a	fairly	high	score	by	repeatedly	sliding	in	an
#up,	right,	down,	and	left	pattern	over	and	over	again.	Write	a	program	that	will	open	the
#game	at	https://gabrielecirulli.github.io/2048/	and	keep	sending	up,	right,	down,	and	left
#keystrokes	to	automatically	play	the	game.

from selenium import webdriver
from	selenium.webdriver.common.keys	import	Keys

browser	=	webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem	=	browser.find_element_by_tag_name('html')
while True:
    htmlElem.send_keys(Keys.UP)					#	scrolls	to	bottom
    htmlElem.send_keys(Keys.RIGHT)					#	scrolls	to	bottom
    htmlElem.send_keys(Keys.DOWN)					#	scrolls	to	bottom
    htmlElem.send_keys(Keys.LEFT)					#	scrolls	to	bottom


