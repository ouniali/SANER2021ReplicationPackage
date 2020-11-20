import os
import os.path
import shlex, subprocess
import git
import pandas as pd
os.chdir('C:/Users/AQ42770/Desktop/aDoctor')
retval = os.getcwd()
a= "C:/Users/AQ42770/Documents/co-occurences/"

for element in os.listdir(a):

    path= a+"/"+element
    outversion = "C:/Users/AQ42770/Documents/co-occurences/Andoidresullts/pack2/"+ "out"+element+".csv"
    cmd='java -cp aDoctor-1.0.jar it.unisa.aDoctor.process.RunAndroidSmellDetection %s %s "111111111111111"'
    cmd = cmd % (path,outversion)
    args = shlex.split(cmd)
    p = subprocess.Popen(args)
    
