class Command():
	def __init__(self, name, description = None):
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
		return "{name} — {description}".format(name=self.__name, description=self.__description)

	pass