#!/usr/bin/python
#Filename:contactor.py
import cPickle as pickle
import os,sys

class person:
	def __init__(self,name,tel_dict,email_dict):
		self.name = name
	def _if_exist(self,name,tel_dict):
		return name in tel_dict.keys()	
	def addnew(self,tel_dict,email_dict):
		if not (self._if_exist(self.name,tel_dict)):
        		self.telnum = raw_input('Input telnum:\n')
        		self.email = raw_input('Input email:\n')
        		tel_dict[self.name]=self.telnum
        		email_dict[self.name]=self.email
        		print 'Successful add a contactor!'
		else:
			print 'This contactor is already existed,can\'t be added!'
	def delold(self,tel_dict,email_dict):
		if (self._if_exist(self.name,tel_dict)):
			del tel_dict[self.name]
			del email_dict[self.name]
			print 'Successful delete a contactor!'	
		else:
			print 'This contactor is not existed,can\'t be deleted!'	
	def search(self,tel_dict,email_dict):	
		for n in tel_dict:
			if (n==self.name):
				self.telnum=tel_dict[n]
				self.email=email_dict[n]
				print 'Contactor:%s\nTelephone number:%s\nEmail:%s\n' %(self.name,self.telnum,self.email)
				break
		else:
			print 'This contactor is not existed!'
	def modify(self,tel_dict,email_dict):
		if (self._if_exist(self.name,tel_dict)):				
        		self.telnum = raw_input('Input new telnum:\n')
        		self.email = raw_input('Input new email:\n')
        		tel_dict[self.name]=self.telnum
        		email_dict[self.name]=self.email
        		print 'Successful modified!'
		else:
			print 'This contactor is not existed!'
	

with open('telnum.txt','rb') as f:
	telnum = pickle.load(f)
with open('email.txt','rb') as f:
	email = pickle.load(f)

if (len(sys.argv)!=3):
	print 'Too more arguments or too less!'
	exit()
contactor=person(sys.argv[2],telnum,email)

if (sys.argv[1]=='-a'):
	contactor.addnew(telnum,email)
elif (sys.argv[1]=='-d'):
	contactor.delold(telnum,email)
elif (sys.argv[1]=='-s'):
	contactor.search(telnum,email)
elif (sys.argv[1]=='-m'):
	contactor.modify(telnum,email)
else:
	print 'Wrong command.'
			
with open('telnum.txt','wb') as f:
	pickle.dump(telnum,f)
with open('email.txt','wb') as f:
	pickle.dump(email,f)

