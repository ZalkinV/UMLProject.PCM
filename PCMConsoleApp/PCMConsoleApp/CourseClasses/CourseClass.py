from enum import Enum
from CourseClasses.PartClass import Part

dateFormat = "%d.%m.%Y"

class Course:
	def __init__(self, name, startDate, endDate, creator):
		self.__name = name
		self.__startDate = startDate
		self.__endDate = endDate
		self.__creator = creator
		self.__statement = Enum("Statement", "Creating Checking Active Finished Deleted")
		self.__description = None
		self.__parts = {}
		self.__numberedParts = []
		self.__ratingScale = None
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

	@property
	def parts(self):
		return self.__parts

	@property
	def numberedParts(self):
		return self.__numberedParts

	def GetInfo(self):
		return "{name} from {start} to {end} by {creator}".format(name=self.__name, start=self.__startDate.strftime(dateFormat), end=self.__endDate.strftime(dateFormat), creator=self.__creator._User__login)

	def AddPart(self, partName, description):
		self.__parts[partName] = Part(partName, description)
		self.__numberedParts.append(partName)
		pass

	def ShowParts(self):
		i = 1
		print(self.__name)
		for partName in self.__numberedParts:
			print("\t{i}. {partInfo}".format(i=i, partInfo=self.__parts[partName].GetInfo()))
			i += 1
		print()
		pass
	pass