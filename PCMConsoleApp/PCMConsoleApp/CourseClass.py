from enum import Enum

class Course:
	def __init__(self, name, startDate, endDate):
		self.__name = name
		self.__startDate = startDate
		self.__endDate = endDate
		self.__creator = None
		self.__statement = Enum("Statement", "Creating Checking Active Finished Deleted")
		self.__parts = []
		self.__description = None
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
	@creator.setter
	def creator(self, newCreator):
		self.__creator = newCreator
		pass

	@property
	def description(self):
		return self.__description
	@description.setter
	def description(self, newDescription):
		self.__description = newDescription
		pass
