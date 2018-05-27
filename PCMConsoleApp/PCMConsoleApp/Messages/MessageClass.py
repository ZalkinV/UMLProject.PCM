import datetime

class Message():
	def __init__(self, text, sender):
		self.__sender = sender
		self.__text = text
		self.__creationDateTime = datetime.datetime.now()
		pass

	@property
	def sender(self):
		return self.__sender

	@property
	def text(self):
		return self.__text
	pass

class Topic(Message):
	pass

class Solution(Message):
	pass