#!/usr/bin/python3
# -*- coding: utf-8 -*-
from sense_hat import SenseHat
import subprocess
import schedule
import time

def joinlisttuples(listoftuples):
  reslist = []
  for eachitem in listoftuples:
    reslist.append(" ".join(map(str,eachitem)))
  #
  
  return " ".join(reslist)
#

def rotscreen():

	sense=SenseHat()

	monitdata = subprocess.check_output(["wlr-randr"]).decode("UTF-8").split("\n")
	currentpos= ""

	monitname = monitdata[0].split(" ")[0]
	for eachline in monitdata:
		if eachline.find("Transform") > 0:
			currentpos = eachline.split(":")[1].strip()
		#
	#	

	paramdict = dict()
	paramdict["wlr-randr"] = ""
	paramdict["--output"] = monitname
	paramdict["--transform"] = "normal"

	signal = False

	if sense.orientation_radians["pitch"] <-1 and currentpos!="270":
		signal = True
		paramdict["--transform"] = "270"
		
	elif sense.orientation_radians["pitch"] >1 and currentpos!="90":
		signal = True
		paramdict["--transform"] = "90"

	elif abs(sense.orientation_radians["pitch"])<1 and sense.orientation_radians["roll"] > 0 and currentpos!="normal":
		signal = True	
		paramdict["--transform"] = "normal"
		
	elif abs(sense.orientation_radians["pitch"])<1 and sense.orientation_radians["roll"] <-1 and currentpos!="180":
		signal = True
		paramdict["--transform"] = "180"
	#

	if signal:
		params = list(paramdict.items())
		subprocess.run(joinlisttuples(params),shell=True)
	#
#

schedule.every(1).seconds.do(rotscreen)

while True:
	schedule.run_pending()
	time.sleep(1)
#

