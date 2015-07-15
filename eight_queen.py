#!usr/bin/python
#Filename:eight_queen

def conflict(state,pos_x):
  pos_y=len(state)
  for i in range(pos_y):
    if abs(state[i]-pos_x) in (0,pos_y-i):
      return True
  return False

def queens(num,state=()):
  for pos in range(num):
    if not conflict(state,pos):
      if len(state)==num-1:
        yield (pos,)
	print (pos,)
      else:
        for result in queens(num,state+(pos,)):
          yield result+(pos,)
          print result+(pos,)
print list(queens(8))
