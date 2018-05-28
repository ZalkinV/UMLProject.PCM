from Messages.MessageClass import Topic
from RatingClasses import *

class Problem():
	def __init__(self, name):
		self.__name = name
		self.__topic = None
		self.__solutions = []
		self.__ratingScale = None
		pass

	@property
	def name(self):
		return self.__name
	
	@property
	def topic(self):
		return self.__topic

	@property
	def ratingScale(self):
		return self.__ratingScale

	def AddTopic(self, topicText, creator):
		self.__topic = Topic(topicText, creator)
		pass

	def AddRatingScale(self, minValue, maxValue, step, ratingForCheck):
		self.__ratingScale = RatingScale(minValue, maxValue, step, ratingForCheck)
		pass
	
	def ShowContent(self):
		print("Problem name:", self.__name, "by", self.__topic.sender.login)
		print("Problem text:", self.__topic.text)
		print("Available ratings:", self.__ratingScale.ratingValues, end='\n\n')
	pass
