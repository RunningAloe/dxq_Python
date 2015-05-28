#!/usr/bin/python
#backup_ver3.py
import os
import time
import sys
source=['/home/dong/dxq_Python','/home/dong/Codehub_dxq']
direc_file='/home/dong/backupfile'
if (sys.argv[1]=='-v'):
	print "source file:%s\ndirect dir:%s\n" %(' '.join(source),'/home/dong/backupfile')
else:
	addsource=raw_input('input the file/dir name you want to add:')
	delsource=raw_input('input the file/dir name you want to delete:')
	if (len(addsource)!=0):
		source.append(addsource)
	if (len(delsource)!=0):
		for item in source:
			if (item==delsource):
				source.remove(item)
				break
			else:
				if (item==len(source)):
					print 'Error!No such file/dir!'
	comments=raw_input('Please input comments:')
	today=direc_file+os.sep+time.strftime('%Y%m%d')
	now=time.strftime('%H%M%S')
	if (sys.argv[1]=='-z'):	
		if (len(comments)==0):
			target=today+os.sep+now+'.zip'
		else:
			target=today+os.sep+now+'_'+comments.replace(' ','_')+'.zip'
	else:
		if (len(comments)==0):
			target=today+os.sep+now+'.tar.gz'
		else:
			target=today+os.sep+now+'_'+comments.replace(' ','_')+'.tar.gz'
	if not os.path.exists(today):
		os.mkdir(today)
		print 'Successfully make today dir'	
	if (sys.argv[1]=='-z'):	
		zipcommand="zip -qr '%s' %s" %(target,' '.join(source))
	else:
		zipcommand="tar -cvzf %s %s" %(target,' '.join(source))
	if (os.system(zipcommand)==0):
		print 'Successfully backup!'
	else:
		print 'error' 
