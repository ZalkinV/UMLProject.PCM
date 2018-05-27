from Messages.MessageClass import Topic

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

	def ShowContent(self):
		print(self.__name, "by", self.__topic.sender.login)
		print(self.__topic.text)
	pass
