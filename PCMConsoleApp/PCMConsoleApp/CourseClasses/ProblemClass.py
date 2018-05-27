class Problem():
	def __init__(self, name):
		self.__name = name
		self.__topic = None
		self.__solutions = None
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

	def ShowContent(self):
		print(self.__topic)
	pass
