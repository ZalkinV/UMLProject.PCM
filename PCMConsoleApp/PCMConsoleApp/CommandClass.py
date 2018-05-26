class Command():
	def __init__(self, name, description = None):
		self.__name = name
		self.__description = description
		self.__attibutes = []
		pass

	@property
	def name(self):
		return self.__name

	@property
	def description(self):
		return self.__description

	def GetInfo(self):
		return "{name} — {description}".format(name=self.__name, description=self.__description)

	def PrintInfo(self):
		print(self.GetInfo())
		attributesInfo = self.GetAttributesInfo()
		for attributeInfo in attributesInfo:
			print("\t", attributeInfo, sep='')


	def AddAtribute(self, name, description):
		self.__attributes.append(Attribute(name, description))
		pass
	
	def GetAttributesInfo(self):
		attributesInfo = []
		for attribute in self.__attributes:
			attributesInfo.append(attribute.GetInfo())
		return attributesInfo

	pass

class Attribute():
	def __init__(self, name, description):
		self.__name = name
		self.__description = description
		pass

	@property
	def name(self):
		return self.__name

	@property
	def description(self):
		return self.__description

	def GetInfo(self):
		return "{name} : {description}".format(name=self.__name, description=self.__description)


	pass