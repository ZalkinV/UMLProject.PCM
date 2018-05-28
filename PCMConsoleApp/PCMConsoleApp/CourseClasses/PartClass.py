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

	@property
	def description(self):
		return self.__description
	
	@property
	def problems(self):
		return self.__problems

	@property
	def numberedProblems(self):
		return self.__numberedProblems

	def GetInfo(self):
		return "{name}: {description}".format(name=self.__name, description=self.__description)
	
	def AddProblem(self, problemName, description, creator, minValue, maxValue, step, ratingForCheck):
		currentProblem = self.__problems[problemName] = Problem(problemName)
		currentProblem.AddTopic(description, creator)
		currentProblem.AddRatingScale(minValue, maxValue, step, ratingForCheck)
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
