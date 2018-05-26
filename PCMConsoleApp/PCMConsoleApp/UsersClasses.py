class User:
	def __init__(self, login, firstName, lastName):
		self.__login = login
		self.__firstName = firstName
		self.__lastName = lastName
		pass

	@property
	def login(self):
		return self.__login
		
	@property
	def firstName(self):
		return self.__firstName
		
	@property
	def lastName(self):
		return self.__lastName

	def GetInfo(self):
		return "{login} — {fName} {lName}".format(login=self.__login, fName=self.__firstName, lName=self.__lastName)
	pass

class Teacher(User):
	pass

class Student(User):
	pass