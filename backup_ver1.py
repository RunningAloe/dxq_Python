#!/usr/bin/python
#backup_ver1.py
import os
import time
source=['/home/dong/dxq_Python','/home/dong/Codehub_dxq']
direc_file='/home/dong/backupfile'
target=direc_file+time.strftime('%Y%m%d%H%M%S')+'.zip'
targetcommand="zip -qr '%s' %s" %(target,' '.join(source))
if (os.system(targetcommand)==0):
	print 'Successfully backup!'
else:
	print 'error' 
