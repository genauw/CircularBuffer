#!/usr/bin/env python

from collections import deque

def getInput():
		i = raw_input("-->")
		return i 

class CircularBuffer:
	def __init__(self, n):
		self.bufferList = deque(maxlen=n)
		self.totalChar = 0

	def size(self):
		return len(self.bufferList)
	
	def inputCommands(self, inputString):
		commandArray = ["A","R","L"]
		a = inputString.split(" ")
		if (a[0] == commandArray[0]):
			self.appender(a[1])
		elif (a[0] == commandArray[1]):
			self.remover(a[1])
		elif (a[0] == commandArray[2]):
			self.lister()
		else:
			print "invalid input, please try again"

	def appender(self, n):
		for i in range(0, int(n)):
			g = getInput()
			self.totalChar = self.totalChar + len(g)
			if (self.charLimitChecker):
				self.bufferList.append(g)
			else:
				self.totalChar = self.totalChar - len(g)
				break
				
	def remover(self, n):
		for i in range(0, int(n)):
			self.bufferList.popleft()

	def lister(self):
		for i in range(0, self.size()):
			print self.bufferList[i]

	def charLimitChecker(self):
		if (self.totalChar >= 20):
			print "There are too many characters stored, please remove something to continue"
			return False
		else:
			return True


while (True):
	i = int(getInput())
	if (i>=0 and i<=10000):
		x = CircularBuffer(i)
		break
	else:
		print "please keep buffer size between 0 and 10000, inclusive"

while (True):
	g = getInput()
	if g == "Q":
		break
	elif (x.charLimitChecker()):
		x.inputCommands(g)