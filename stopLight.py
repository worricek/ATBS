#! /usr/bin/python
import	logging
logging.basicConfig(level=logging.DEBUG,	format='	%(asctime)s	-	%(levelname)s-	%(message)s')
def	switchLights(stoplight):
    for	key	in	stoplight.keys():
        if	stoplight[key]	==	'green':
            stoplight[key]	=	'yellow'
        elif	stoplight[key]	==	'yellow':
            stoplight[key]	=	'red'
        elif	stoplight[key]	==	'red':
            stoplight[key]	=	'green'
 #   assert	'red'	in	stoplight.values(),	'Neither	light	is	red!	'	+	str(stoplight)

market_2nd	=	{'ns':	'green',	'ew':	'red'}
mission_16th	=	{'ns':	'red',	'ew':	'green'}
switchLights(market_2nd)
