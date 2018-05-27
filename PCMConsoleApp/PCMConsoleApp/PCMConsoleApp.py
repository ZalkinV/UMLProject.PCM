import datetime
from UsersClasses import *
from CommandClass import Command
from CourseClasses.CourseClass import *
from CourseClasses.PartClass import *
from CourseClasses.ProblemClass import *

def ShowHelp(commands):
	print("\nВозможные команды:")
	for command in commands:
		print(command.GetInfo())
	print()
	pass

def ShowCourses():
	i = 1
	for courseName in numberedCourses:
		print("{i}. {courseInfo}".format(i=i, courseInfo=courses[courseName].GetInfo()))
		i += 1
	print()
	pass

def ShowUsers():
	for user in users.values():
		print(user.login, user.firstName, user.lastName, "Student" if type(user) == Student else "Teacher")
	print()
	pass

def ShowCurrentUser():
	print("Текущий пользователь:", currentUser.GetInfo())
	pass

def ShowCurrentLocation():
	locationString = "Текущее местоположение: "
	for location in currentUserLocation:
		locationString += '/' + location.name
	print(locationString, end='\n\n')
	pass

def CreateCourse():
	def ReadDates():
		while (True):
			startString = input("\tдату начала курса (ДД.ММ.ГГГГ): ")
			try:
				start = datetime.datetime.strptime(startString, dateFormat)
				if (start.date() < datetime.datetime.today().date()):
					print("Курс не может начаться в прошлом")
					continue
			except:
				print("Это неверная дата")
				continue
			
			endString = input("\tдату окончания курса (ДД.ММ.ГГГГ): ")
			try:
				end = datetime.datetime.strptime(endString, dateFormat)
			except:
				print("Это неверная дата")
				continue

			if (start < end):
				break
			else:
				print("Курс не может завершиться не начавшись.\n")
		return (start, end)
	print("Для создания курса введите...")
	courseName = input("\tназвание курса: ")
	courseStart, courseEnd = ReadDates()
	description = input("\tописание для курса: ")

	newCourse = AddCourse(courseName, courseStart, courseEnd, currentUser, description)
	WriteData(fileNameCourses, newCourse.name, newCourse.startDate.strftime(dateFormat), newCourse.endDate.strftime(dateFormat), newCourse.creator._User__login, newCourse.description)
	print("Новый курс \"{0}\" был успешно создан!".format(courseName), end='\n\n')
	pass

def AddCourse(name, startDate, endDate, creator, description):
	courses[name] = Course(name, startDate, endDate, creator)
	courses[name].description = description
	numberedCourses.append(name)
	return courses[name]

def CreatePart():
	print("Для создания раздела введите...")
	partName = input("\tназвание раздела: ")
	partDescription = input("\tописание раздела: ")
	currentCourse = currentUserLocation[-1]
	currentCourse.AddPart(partName, partDescription)
	WriteData(fileNameParts, currentCourse.name, partName, partDescription)
	print("Новый раздел \"{0}\" был успешно создан!".format(partName), end='\n\n')
	pass

def CreateProblem():
	print("Для создания задания введите...")
	problemName = input("\tназвание задание: ")
	description = input("\tописание задания: ")
	minValue = input("\tминимальное количество баллов за выполнение: ")
	maxValue = input("\tмаксимальное количество баллов за выполнение: ")
	step = input("\tразница между соседними баллами: ")
	ratingForCheck = input("\tколичество баллов за проверку заданий: ")
	currentCourse = currentUserLocation[-2]
	currentPart = currentUserLocation[-1]
	part.AddProblem(problemName, description, minValue, maxValue, step, ratingForCheck)
	WriteData()
	pass

def WriteData(fileName, *args):
	toFileString = ""
	for arg in args:
		toFileString += str(arg) + ';'
	toFileString = toFileString[:-1] + '\n'
	fileDescriptor = open(fileName, 'a')
	fileDescriptor.write(toFileString)
	fileDescriptor.close()
	pass

def CreateUser():
	print("Введите ваши...")
	login = input("\tлогин: ")
	firstName = input("\tимя: ")
	lastName = input("\tфамилия: ")
	while (True):
		role = input("\tдолжность (T - преподаватель, S - студент): ")
		if (AddUser(login, firstName, lastName, role)):
			break
	
	WriteData(fileNameUsers, login, firstName, lastName, role)
	print("Новый пользователь был успешно создан! Теперь вы можете зайти в аккаунт под логином", login, end='\n\n')
	pass

def AddUser(login, firstName, lastName, role):
	isSucces = True
	if (role == 'T'):
		users[login] = Teacher(login, firstName, lastName)
	elif (role == 'S'):
		users[login] = Student(login, firstName, lastName)
	else:
		isSucces = False
	return isSucces

def Login(login):
	global currentUser
	
	if (login != ''):
		try:
			currentUser = users[login]
			print("Вход выполнен успешно,", currentUser.firstName, currentUser.lastName, end='\n\n')
		except KeyError:
			print("Пользователя с логином {0} нет в системе. Зарегистрируйтесь с помощью команды /newUser".format(login), end='\n\n')
	else:
		currentUser = None
		print("Вы вышли из аккаунта.", end='\n\n')
	pass

def HandleUserInput():
	commands = (
	Command("/help", "вывод всех допустимых команд"),
	Command("/showCourses", "отображение всех имеющихся курсов"),
	Command("/showUsers", "отображение всех пользоватлей в системе"),
	Command("/newCourse", "запуск помощника по созданию курса"),
	Command("/newUser", "создание нового аккаунта"),
	Command("/login", "войти в аккаунт (/login name) (при вызове команды без параметров происходит выход из аккаунта)"),
	Command("/go", "перейти в содержимое курса/раздела/задания (/go номер_курса)"),
	Command("/curU", "получить информацию о текущем аккаунте"),
	Command("/curL", "получить информацию своём местоположении в системе"),
	Command("/newPart", "создать новый раздел (нужно находится внутри курса)"),
	Command("/newProblem", "создать новое задание (нужно находиться внутри раздела"),
	Command("/exit", "выход из программы")
	)

	commandsDict = {command.name : command for command in commands}

	beforeLoginMessage = "Перед началом использования программы войдите в свой аккаунт с помощью команды /login вашлогин или зарегистрируйтесь с помощью /newUser"
	greetingMessage = "Введите /help для получения справки по всем командам или введите команду для исполнения."
	print(greetingMessage, beforeLoginMessage, sep='\n')
	while (True):
		command = input("Новая команда: ").split(' ')
		commandName = command[0]
		commandAttribute = command[1] if len(command) > 1 else ""

		if (currentUser == None and (commandName != "/login" and commandName != "/newUser")):
			print("Войдите в свой аккаунт перед использованием программы с помощью команды /login вашлогин", end='\n\n')

		elif (commandName == commands[0].name):
			ShowHelp(commands)
		elif (commandName == commands[1].name):
			ShowCourses()
		elif (commandName == commands[2].name):
			ShowUsers()
		elif (commandName == commands[3].name):
			if (isinstance(currentUser, Teacher)):
				CreateCourse()
			else:
				print("Создавать новые курсы могут только преподаватели.", end='\n\n')
		elif (commandName == commands[4].name):
			if (currentUser == None):
				CreateUser()
			else:
				print("Для создания нового пользователя вы должны выйти из аккаунта.", end='\n\n')
		elif (commandName == commands[5].name):
			Login(commandAttribute)
		elif (commandName == commands[6].name):
			ChangeUserLocation(commandAttribute)
		elif (commandName == commands[7].name):
			ShowCurrentUser()
		elif (commandName == commands[8].name):
			ShowCurrentLocation()
		
		elif (commandName == commands[9].name):
			if (isinstance(currentUserLocation[-1], Course)):
				if (currentUser == currentUserLocation[-1].creator):
					CreatePart()
				else:
					print("Добавлять новые разделы в курс может толкько создатель курса")
			else:
				print("Создать раздел можно только находясь внутри курса. Воспользуйтесь командой /go номер_курса", end='\n\n')
		
		elif (commandName == commands[10].name):
			if (isinstance(currentUserLocation[-1], Part)):
				if (currentUser == currentUserLocation[-2].creator):
					CreateProblem()
				else:
					print("Добавлять новые задания в курс может толкько создатель курса", end='\n\n')
			else:
				print("Создать задание можно только находясь внутри раздела. Воспользуйтесь командой /go номер_раздела", end='\n\n')
		
		elif (commandName == commands[-1].name):
			break

		else:
			print("Команда \"{0}\" неизвестна. Введите действительную команду.".format(commandName), end='\n\n')
	pass


currentUser = None
currentUserLocation = []
courses = {}
numberedCourses = []
users = {}
filesDirectory = "DataFiles/"
fileNameUsers = filesDirectory + "Users.txt"
fileNameCourses = filesDirectory + "Courses.txt"
fileNameParts = filesDirectory + "Parts.txt"
fileNameProblems = filesDirectory + "Problems.txt"


def Main():
	open(fileNameUsers, 'a').close()
	open(fileNameCourses, 'a').close()
	open(fileNameParts, 'a').close()
	open(fileNameProblems, 'a').close()
	
	GetUsersFromFile()
	GetCoursesFromFile()
	GetPartsFromFile()

	Login("t")
	HandleUserInput()

	print("Выполнение программы завершено.")
	pass

def GetUsersFromFile():
	fileDescriptor = open(fileNameUsers)
	rawData = fileDescriptor.readlines()
	for line in rawData:
		login, firstName, lastName, role = line.replace('\n','').split(';')
		AddUser(login, firstName, lastName, role)
	fileDescriptor.close()
	pass

def GetCoursesFromFile():
	fileDescriptor = open(fileNameCourses)
	rawData = fileDescriptor.readlines()
	for line in rawData:
		name, start, end, creator, description = line.replace('\n','').split(';')
		startDate = datetime.datetime.strptime(start, dateFormat)
		endDate = datetime.datetime.strptime(end, dateFormat)
		AddCourse(name, startDate, endDate, users[creator], description)
	fileDescriptor.close()
	pass

def GetPartsFromFile():
	fileDescriptor = open(fileNameParts)
	rawData = fileDescriptor.readlines()
	for line in rawData:
		courseName, partName, description = line.replace('\n','').split(';')
		courses[courseName].AddPart(partName, description)
	fileDescriptor.close()
	pass

def GetProblemsFromFile():
	fileDescriptor = open(fileNameProblems)
	rawData = fileDescriptor.readlines()
	for line in rawData:
		courseName, partName, problemName, description, minValue, maxValue, step, ratingForCheck = line.replace('\n','').split(';')
		courses[courseName].parts[partName].AddProblem(problemName, description, minValue, maxValue, step, ratingForCheck)
	pass

def ChangeUserLocation(newLocation):
	global currentUserLocation

	if (newLocation == ""):
		if (not currentUserLocation):
			ShowCourses()
		elif (isinstance(currentUserLocation[-1], Course)):
			currentUserLocation[-1].ShowParts()
		elif (isinstance(currentUserLocation[-1], Part)):
			currentUserLocation[-1].ShowProblems()
		elif (isinstance(currentUserLocation[-1], Problem)):
			currentUserLocation[-1].ShowContent()

	else:
		locationNumber = int(newLocation)
		if (locationNumber == 0):
			currentUserLocation.clear()
		elif (locationNumber > 0):
			if (not currentUserLocation):
				try:
					choosenCourseName = numberedCourses[locationNumber - 1]
					currentUserLocation.append(courses[choosenCourseName])
					currentUserLocation[-1].ShowParts()
				except KeyError:
					print("Курса с таким номером нет, выберите курс из списка")
				

			elif (isinstance(currentUserLocation[-1], Course)):
				try:
					currentCourse = currentUserLocation[-1]
					currentUserLocation.append(currentCourse.parts[currentCourse.numberedParts[locationNumber - 1]])
					currentUserLocation[-1].ShowProblems()
				except KeyError:
					print("Раздела с таким номером нет, выберите раздел из списка")
				

			elif (isinstance(currentUserLocation, Part)):
				try:
					currentPart = currentUserLocation[-1]
					currentUserLocation.append(currentPart.problems[numberedProblems[locationNumber - 1]])
					currentUserLocation[-1].ShowContent()
				except KeyError:
					print("Задания с таким номером нет, выберите задание из списка")

		elif (locationNumber < 0):
			try:
				for i in range(abs(locationNumber)):
					currentUserLocation.pop()
			except IndexError:
				print("Вы в самом начале. Назад идти больше некуда")
			pass
		
	pass

Main()