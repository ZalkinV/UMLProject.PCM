import datetime
from CourseClass import *
from UsersClasses import *
from CommandClass import Command

def ShowHelp(commands):
	print("\nВозможные команды:")
	for command in commands:
		print(command.GetInfo())
	print()
	pass

def ShowCourses():
	i = 1
	for course in courses:
		print("{i}. {courseInfo}".format(i=i, courseInfo=course.GetInfo()))
		i += 1
	print()
	pass

def ShowUsers():
	for user in users:
		print(user.login, user.firstName, user.lastName, "Student" if type(user) == Student else "Teacher")
	print()
	pass


def ShowCurrentUser():
	print("Текущий пользователь:", currentUser.GetInfo())
	pass

def ShowCurrentLocation():
	locationString = "Текущее местоположение: "
	for location in currentUserLocation:
		locationString += '/' +location.name
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
	print("Новый курс \"{0}\" был успешно создан!".format(newCourse.name), end='\n\n')
	pass

def AddCourse(name, startDate, endDate, creator, description):
	courses.append(Course(name, startDate, endDate, creator))
	courses[-1].description = description
	return courses[-1]

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
		users.append(Teacher(login, firstName, lastName))
	elif (role == 'S'):
		users.append(Student(login, firstName, lastName))
	else:
		isSucces = False
	return isSucces

def Login(login):
	isExist = False
	for user in users:
		if (login == user._User__login):
			global currentUser 
			currentUser = user
			isExist = True
			print("Вход выполнен успешно,", currentUser._User__firstName, currentUser._User__lastName, end='\n\n')
	if (not isExist):
		print("Пользователя с логином {0} нет в системе. Зарегистрируйтесь с помощью команды /newUser".format(login), end='\n\n')
	pass

def HandleUserInput():
	commands = (
	Command("/help", "вывод всех допустимых команд"),
	Command("/showCourses", "отображение всех имеющихся курсов"),
	Command("/showUsers", "отображение всех пользоватлей в системе"),
	Command("/newCourse", "запуск помощника по созданию курса"),
	Command("/newUser", "создание нового аккаунта"),
	Command("/login", "войти в аккаунт (/login name)"),
	Command("/go", "перейти в содержимое курса/раздела/задания (/go номер_курса)"),
	Command("/curU", "получить информацию о текущем аккаунте"),
	Command("/curL", "получить информацию своём местоположении в системе"),
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
			CreateCourse()
		elif (commandName == commands[4].name):
			CreateUser()
		elif (commandName == commands[5].name):
			Login(commandAttribute)
		elif (commandName == commands[6].name):
			ChangeUserLocation(commandAttribute)
		elif (commandName == commands[7].name):
			ShowCurrentUser()
		elif (commandName == commands[8].name):
			ShowCurrentLocation()
		elif (commandName == commands[-1].name):
			break

		else:
			print("Команда \"{0}\" неизвестна. Введите действительную команду.".format(commandName), end='\n\n')
	pass


currentUser = None
currentUserLocation = []
courses = []
users = []
fileNameUsers = "DataFiles/Users.txt"
fileNameCourses = "DataFiles/Courses.txt"


def Main():
	open(fileNameUsers, 'a').close()
	open(fileNameCourses, 'a').close()

	users = GetUsersFromFile()
	courses = GetCoursesFromFile()
	
	Login("zalkin")
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
		AddCourse(name, startDate, endDate, GetCreator(creator), description)
	fileDescriptor.close()
	pass

def GetCreator(login):
	creator = None
	for user in users:
		if (user._User__login == login):
			creator = user
	return creator

def ChangeUserLocation(newLocation):
	global currentUserLocation

	if (newLocation == ""):
		ShowCourses()
	else:
		newLocation = int(newLocation)
		if (newLocation == 0):
			currentUserLocation.clear()
		elif (newLocation > 0):
			if (not currentUserLocation):
				try:
					currentUserLocation.append(courses[newLocation - 1])
					currentUserLocation[-1].ShowParts()
				except KeyError:
					print("Курса с таким номером нет, выберите курс из списка")

			elif (isinstance(currentUserLocation[-1], Course)):
				try:
					currentCourse = currentUserLocation[-1]
					currentUserLocation.append(currentCourse.parts[newLocation - 1])
					currentUserLocation[-1].ShowProblems()
				except KeyError:
					print("Раздела с таким номером нет, выберите раздел из списка")

			elif (isinstance(currentUserLocation, Part)):
				try:
					currentCourse = currentUserLocation[-2]
					currentPart = currentUserLocation[-1]
					currentUserLocation.append(currentCourse.problems[newLocation - 1])
					currentUserLocation[-1].ShowContent()
				except KeyError:
					print("Задания с таким номером нет, выберите задание из списка")
			ShowCurrentLocation()

		elif (newLocation < 0):
			pass


Main()