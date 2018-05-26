from enum import Enum

dateFormat = "%d.%m.%Y"

class Course:
	def __init__(self, name, startDate, endDate, creator):
		self.__name = name
		self.__startDate = startDate
		self.__endDate = endDate
		self.__creator = creator
		self.__statement = Enum("Statement", "Creating Checking Active Finished Deleted")
		self.__description = None
		self.__parts = []
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

	def GetInfo(self):
		return "{name} from {start} to {end} by {creator}".format(name=self.__name, start=self.__startDate.strftime(dateFormat), end=self.__endDate.strftime(dateFormat), creator=self.__creator._User__login)

	def AddPart(name, description=None):
		pass

	def ShowParts(self):
		i = 1
		for part in self.__parts:
			print("{i}. {partInfo}".format(i=i, partInfo=part.GetInfo()))
			i += 1
	pass

class Part():
	def __init__(self, name):
		self.__name = name
		self.__description = None
		self.__problems = []
		pass

	@property
	def name(self):
		return self.__name
	
	@property
	def problems(self):
		return self.__problems

	def GetInfo(self):
		return "{name} — {description}".format(self.__name, self.__description)

	def AddDescription(self, description):
		self.__description = description
		pass
	
	def AddProblem(self, problemName):
		self.__problems.append()
		pass
	def ShowProblems(self):
		i = 1
		for problem in __problems:
			print("{i}. {name}:{topicName}".format(i=i, name=problem.name))
			i += 1

	pass


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