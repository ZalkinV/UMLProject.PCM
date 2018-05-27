from CourseClasses.ProblemClass import Problem

class Part():
	def __init__(self, name, description):
		self.__name = name
		self.__description = description
		self.__problems = {}
		self.__numberedProblems = []
		pass

	@property
	def name(self):
		return self.__name
	

	def GetInfo(self):
		return "{name}: {description}".format(name=self.__name, description=self.__description)
	
	def AddProblem(self, problemName, description, minValue, maxValue, step, ratingForCheck):
		self.__problems[problemName] = Problem(problemName)
		self.__problems[problemName].AddTopic(description)
		self.__numberedProblems.append(problemName)
		pass

	def ShowProblems(self):
		i = 1
		print(self.__name)
		for problemName in self.__numberedProblems:
			print("\t{i}. {name}".format(i=i, name=problemName))
			i += 1
		print()
		pass

	pass
