from enum import Enum
from CourseClasses.PartClass import Part

dateFormat = "%d.%m.%Y"

class Statement(Enum):
	creating = 0
	checking = 1
	active = 2
	finished = 3
	deleted = 4
	pass

class Course:
	def __init__(self, name, startDate, endDate, creator):
		self.__name = name
		self.__startDate = startDate
		self.__endDate = endDate
		self.__creator = creator
		self.__participants = {}
		self.__statement = Statement.creating
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
	def participants(self):
		return self.__participants

	@property
	def statement(self):
		return self.__statement
	@statement.setter
	def statement(self, newState):
		self.__statement = newState
		pass

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
		return "{name} from {start} to {end} by {creator} State:{state}".format(name=self.__name, start=self.__startDate.strftime(dateFormat), end=self.__endDate.strftime(dateFormat), creator=self.__creator.login, state=self.__statement.value)

	def AddPart(self, partName, description):
		self.__parts[partName] = Part(partName, description)
		self.__numberedParts.append(partName)
		pass

	def ShowInfo(self):
		i = 1
		print("Курс:", self.__name)
		print("Description:", self.__description)
		for partName in self.__numberedParts:
			print("\t{i}. {partInfo}".format(i=i, partInfo=self.__parts[partName].GetInfo()))
			i += 1
		print()
		pass

	def AddParticipant(self, user):
		canJoin = False
		if (self.__participants.get(user.login) == None):
			self.__participants[user.login] = user
			canJoin = True

		return canJoin


		pass
	pass