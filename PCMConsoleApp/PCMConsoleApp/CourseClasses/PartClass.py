class Part():
	def __init__(self, name, description):
		self.__name = name
		self.__description = description
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
	
	def AddProblem(self, problemName):
		self.__problems.append()
		pass
	def ShowProblems(self):
		i = 1
		for problem in __problems:
			print("{i}. {name}:{topicName}".format(i=i, name=problem.name))
			i += 1

	pass
