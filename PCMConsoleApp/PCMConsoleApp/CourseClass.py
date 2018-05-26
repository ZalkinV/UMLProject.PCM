from enum import Enum

class Course:
	def __init__(self, name, startDate, endDate, creator):
		self.__name = name
		self.__startDate = startDate
		self.__endDate = endDate
		self.__creator = creator
		self.__statement = Enum("Statement", "Creating Checking Active Finished Deleted")
		self.__description = None
		self.__parts = []
		pass

	@property
	def name(self):
		return self.__name

	@property
	def startDate(self):
		return self.__startDate

	@property
	def endDate(self):
		return self.__endDate

	@property
	def creator(self):
		return self.__creator

	@property
	def description(self):
		return self.__description
	@description.setter
	def description(self, newDescription):
		self.__description = newDescription
		pass
	pass


class Part():
	def __init__(self, name):
		self.__name = name
		self.__problems = []
		pass

	@property
	def name(self):
		return self.__name

	def AddDescription(self, description):
		self.__description = description
		pass
	
	def AddProblem(self, problemName):
		self.__problems.append()
		pass
	pass


class Problem():
	def __init__(self, name):
		self.__name = name
		self.__topic = None
		self.__solutions = None
		self.__ratingScale = None
		pass
	pass