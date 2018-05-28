class RatingScale():
	def __init__(self, min, max, step, ratingForCheck = 0):
		self.__min = min
		self.__max = max
		self.__step = step
		self.__ratingForCheck = ratingForCheck
		self.__ratingValues = []

		currentValue = self.__min
		while currentValue <= self.__max:
			self.__ratingValues.append(currentValue)
			currentValue += self.__step
		pass

	@property
	def min(self):
		return self.__min

	@property
	def max(self):
		return self.__max
	
	@property
	def step(self):
		return self.__step

	@property
	def ratingForCheck(self):
		return self.__ratingForCheck
	
	@property
	def ratingValues(self):
		return self.__ratingValues

	pass
