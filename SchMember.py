#!/usr/bin/python
#Filename:SchMember.py

class SchMember:
	def __init__(self,name,major):
		self.name=name
		self.major=major
		print "Initializing %s" %self.name
	def introduction(self):
		print "%s\'s major is %s." %(self.name,self.major)
class Teacher(SchMember):
	def __init__(self,name,major,salary):
		SchMember.__init__(self,name,major)
		self.salary=salary
	def introduction(self):
		SchMember.introduction(self)
		print "%s\'s salary is %d." %(self.name,self.salary)

class Student(SchMember):
	def __init__(self,name,major,score):
		SchMember.__init__(self,name,major)
		self.score=score
	def introduction(self):
		SchMember.introduction(self)
		print "%s\'s score is %d." %(self.name,self.score)
t=Teacher('wang','ee',3000)
s=Student('li','cs',90)
t.introduction()
s.introduction()
