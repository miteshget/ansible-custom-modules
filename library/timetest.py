#!/usr/bin/python

import json
import datetime

def show_time():
  date = str(datetime.datetime.now())
  print json.dumps({ "time": date })

show_time()
	
