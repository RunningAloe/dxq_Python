#!/usr/bin/python
#backup_ver2.py
import os
import time
source=['/home/dong/dxq_Python','/home/dong/Codehub_dxq']
direc_file='/home/dong/backupfile'
today=direc_file+os.sep+time.strftime('%Y%m%d')
if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully make today dir'	
now=time.strftime('%H%M%S')
target=today+os.sep+now+'.zip'
zipcommand="zip -qr '%s' %s" %(target,' '.join(source))
if (os.system(zipcommand)==0):
	print 'Successfully backup!'
else:
	print 'error' 
