#!/usr/bin/python
#backup_ver1.py
import os
import time
source=['/home/dong/dxq_Python','/home/dong/Codehub_dxq']
direc_file='/home/dong/backupfile'
comments=raw_input('Please input comments:')
today=direc_file+os.sep+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')
if (len(comments)==0):
	target=today+os.sep+now+'.zip'
else:
	target=today+os.sep+now+'_'+comments.replace(' ','_')+'.zip'
if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully make today dir'	
zipcommand="zip -qr '%s' %s" %(target,' '.join(source))
if (os.system(zipcommand)==0):
	print 'Successfully backup!'
else:
	print 'error' 
