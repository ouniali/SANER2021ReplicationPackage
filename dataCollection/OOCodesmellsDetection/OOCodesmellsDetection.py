import os
import subprocess
import os.path
import shlex
import git
import json
import csv
from collections import Counter

import codecs
import pandas as pd

ECLIPSE_PATH ='C:/Users/AQ42770/Desktop/eclipse/plugins'
EQUINOX = ECLIPSE_PATH+'/org.eclipse.equinox.launcher_1.3.100.v20150511-1540.jar'
MAIN='org.eclipse.core.launcher.Main'
ORGANIC='organic.Organic'
a= "C:/Users/AQ42770/Documents/co-occurences/pack2/SimpleBitcoinWidget"

       
"""for element in os.listdir(a):
	path= a+"/"+element
	outversion = "C:/Users/AQ42770/Documents/co-occurences/"+"out"+element+".json"
	
	commande='java -jar -XX:MaxPermSize=2560m -Xms40m -Xmx2500m  "%s" %s -application %s -sf "%s" -src "%s"'
	commande= commande % (EQUINOX, MAIN, ORGANIC, outversion, path)
	
	args = shlex.split(commande)
	
	p = subprocess.Popen(args)"""
	
	
