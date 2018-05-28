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
		if (courses[courseName].statement == Statement.active or isinstance(currentUser, Moderator)):
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
	newCourse = AddCourse(courseName, courseStart, courseEnd, currentUser, Statement.checking, description)
	print("Новый курс \"{0}\" был успешно создан и отправлен на проверку модератору!".format(courseName), end='\n\n')
	pass

def AddCourse(name, startDate, endDate, creator, statement, description):
	courses[name] = Course(name, startDate, endDate, creator)
	courses[name].statement = Statement(statement)
	courses[name].description = description
	numberedCourses.append(name)
	return courses[name]

def CreatePart():
	print("Для создания раздела введите...")
	partName = input("\tназвание раздела: ")
	partDescription = input("\tописание раздела: ")
	currentCourse = currentUserLocation[-1]
	currentCourse.AddPart(partName, partDescription)
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
	currentPart.AddProblem(problemName, description, currentUser, float(minValue), float(maxValue), float(step), float(ratingForCheck))
	print("Новое задание \"{0}\" было успешно создано!".format(problemName), end='\n\n')
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
	
	print("Новый пользователь был успешно создан! Теперь вы можете зайти в аккаунт под логином", login, end='\n\n')
	pass

def AddUser(login, firstName, lastName, role):
	isSucces = True
	if (role == 'T'):
		users[login] = Teacher(login, firstName, lastName)
	elif (role == 'S'):
		users[login] = Student(login, firstName, lastName)
	elif (role == 'M'):
		users[login] = Moderator(login, firstName, lastName)
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
	Command("/invite", "пригласить пользователя в текущий курс (/invite логин_приглашаемого)"),
	Command("/join", "вступить в курс (/join номер_курса)"),
	Command("/acceptCourse", "подтверждение создания курса (/acceptCourse номер_курса) (доступно только модераторам"),
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
		
		elif (commandName == commands[11].name):
			if (isinstance(currentUserLocation[0], Course)):
				if (currentUser == currentUserLocation[-1].creator):
					try:
						currentUserLocation[0].AddParticipant(users[commandAttribute])
						print("Пользователь {0} был успешно добавлен в курс".format(commandAttribute), end='\n\n')
					except KeyError:
						print("Пользователя с таким логином в системе нет", end='\n\n')
				else:
					print("Только владелец курса может приглашать в него пользователей", end='\n\n')
			else:
				print("Приглашать пользователей в курс можно только находясь внутри курса", end='\n\n')
			pass

		elif (commandName == commands[12].name):
			if (currentUserLocation and isinstance(currentUserLocation[0], Course)):
				if(currentUserLocation[0].AddParticipant(currentUser)):
					print("Вы вступили в курс {0}!".format(currentUserLocation[0].name), end='\n\n')
				else:
					print("Вы уже находитесь внутри курса {0} и не можете вступить повторно".format(currentUserLocation[0].name), end='\n\n')
			else:
				print("Зайдите внутрь курса, чтобы присоединиться к нему", end='\n\n')
		elif (commandName == commands[13].name):
			if (isinstance(currentUser, Moderator)):
				if (commandAttribute != ''):
					courseName = numberedCourses[int(commandAttribute) - 1]
					courses[courseName].statement = Statement.active
					print("Курс {0} был опубликован.".format(courseName), end='\n\n')
				else:
					print("Нужно выбрать курс для опубликовывания.", end='\n\n')
			else:
				print("Публиковать курсы может только модератор!", end='\n\n')
			pass

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
filesNames = {"users" : "Users.txt",
			  "courses" : "Courses.txt",
			  "parts" : "Parts.txt",
			  "problems" : "Problems.txt",
			  "coursesUsers" : "CoursesUsers.txt"}

def Main():
	filesNames.update({fileName: filesDirectory + filesNames[fileName] for fileName in filesNames})
	for fileName in filesNames.values():
		open(fileName, 'a').close()
	
	GetUsersFromFile()
	GetCoursesFromFile()
	GetPartsFromFile()
	GetProblemsFromFile()

	Login("teacher")

	try:
		HandleUserInput()
	finally:
		SaveDataToFiles()
	print("Выполнение программы завершено.")
	pass

def SaveDataToFiles():
	def WriteData(fileName, *args):
		toFileString = ""
		for arg in args:
			toFileString += str(arg) + ';'
		toFileString = toFileString[:-1] + '\n'
		fileDescriptor = open(fileName, 'a')
		fileDescriptor.write(toFileString)
		fileDescriptor.close()
		pass

	def GetUserRoleChar(user):
		userChar = ''
		if (isinstance(user, Moderator)):
			userChar = 'M'
		elif (isinstance(user, Teacher)):
			userChar = 'T'
		elif (isinstance(user, Student)):
			userChar = 'S'
		return userChar

	for fileName in filesNames.values():
		open(fileName, 'w').close()

	for user in users.values():
		WriteData(filesNames["users"], user.login, user.firstName, user.lastName, GetUserRoleChar(user))

	for courseName in numberedCourses:
		course = courses[courseName]
		WriteData(filesNames["courses"], course.name, course.startDate.strftime(dateFormat), course.endDate.strftime(dateFormat), course.creator.login, course.statement.value, course.description)
		participantsList = [userInCourse.login for userInCourse in course.participants.values()]
		WriteData(filesNames["coursesUsers"], course.name, participantsList)
		
		for partName in course.numberedParts:
			part = course.parts[partName]
			WriteData(filesNames["parts"], course.name, part.name, part.description)

			for problemName in part.numberedProblems:
				problem = part.problems[problemName]
				WriteData(filesNames["problems"], course.name, part.name, problem.topic.text, problem.ratingScale.min, problem.ratingScale.max, problem.ratingScale.step, problem.ratingScale.ratingForCheck)
	
	pass

def GetUsersFromFile():
	fileDescriptor = open(filesNames["users"])
	rawData = fileDescriptor.readlines()
	for line in rawData:
		login, firstName, lastName, role = line.replace('\n','').split(';')
		AddUser(login, firstName, lastName, role)
	fileDescriptor.close()
	pass

def GetCoursesFromFile():
	fileDescriptor = open(filesNames["courses"])
	rawData = fileDescriptor.readlines()
	for line in rawData:
		name, start, end, creator, statement, description = line.replace('\n','').split(';')
		startDate = datetime.datetime.strptime(start, dateFormat)
		endDate = datetime.datetime.strptime(end, dateFormat)
		currentCourse = AddCourse(name, startDate, endDate, users[creator], Statement(int(statement)), description)
	fileDescriptor.close()
	pass

def GetParticipantsFromFile():
	fileDescriptor = open(filesNames["coursesUsers"])
	rawData = fileDescriptor.readlines()
	for line in rawData:
		courseName, participants = line.replace('\n','').split(';')
		participantsLogins = participants.split(',')

		for participantLogin in participantsLogins:
			courses[courseName].AddParticipant(users[participantLogin])

	fileDescriptor.close()
	pass

def GetPartsFromFile():
	fileDescriptor = open(filesNames["parts"])
	rawData = fileDescriptor.readlines()
	for line in rawData:
		courseName, partName, description = line.replace('\n','').split(';')
		courses[courseName].AddPart(partName, description)
	fileDescriptor.close()
	pass

def GetProblemsFromFile():
	fileDescriptor = open(filesNames["problems"])
	rawData = fileDescriptor.readlines()
	for line in rawData:
		courseName, partName, problemName, description, minValue, maxValue, step, ratingForCheck = line.replace('\n','').split(';')
		courses[courseName].parts[partName].AddProblem(problemName, description, currentUser, minValue, maxValue, step, ratingForCheck)
	pass

def ChangeUserLocation(newLocation):
	global currentUserLocation

	if (newLocation == ""):
		if (not currentUserLocation):
			ShowCourses()
		elif (isinstance(currentUserLocation[-1], Course)):
			currentUserLocation[-1].ShowInfo()
		elif (isinstance(currentUserLocation[-1], Part)):
			currentUserLocation[-1].ShowProblems()
		elif (isinstance(currentUserLocation[-1], Problem)):
			currentUserLocation[-1].ShowContent()

	else:
		locationNumber = int(newLocation)
		if (locationNumber == 0):
			currentUserLocation.clear()
			print("Вы вышли из курса.", end='\n\n')
		elif (locationNumber > 0):
			if (not currentUserLocation):
				try:
					choosenCourse = courses[numberedCourses[locationNumber - 1]]
					if (choosenCourse.statement == Statement.active or isinstance(currentUser, Moderator)):
						currentUserLocation.append(courses[choosenCourse.name])
						currentUserLocation[-1].ShowInfo()
					else:
						raise KeyError
				except KeyError:
					print("Курса с таким номером нет, выберите курс из списка", end='\n\n')
				

			elif (isinstance(currentUserLocation[-1], Course)):
				try:
					currentCourse = currentUserLocation[-1]
					currentUserLocation.append(currentCourse.parts[currentCourse.numberedParts[locationNumber - 1]])
					currentUserLocation[-1].ShowProblems()
				except (KeyError, IndexError):
					print("Раздела с таким номером нет, выберите раздел из списка", end='\n\n')
				

			elif (isinstance(currentUserLocation[-1], Part)):
				try:
					currentPart = currentUserLocation[-1]
					currentUserLocation.append(currentPart.problems[currentPart.numberedProblems[locationNumber - 1]])
					currentUserLocation[-1].ShowContent()
				except (KeyError, IndexError):
					print("Задания с таким номером нет, выберите задание из списка", end='\n\n')
			elif (isinstance(currentUserLocation[-1], Problem)):
				print("Вы находитесь внутри задания и дальше идти некуда")

		elif (locationNumber < 0):
			try:
				for i in range(abs(locationNumber)):
					currentUserLocation.pop()
			except IndexError:
				print("Вы в самом начале. Назад идти больше некуда", end='\n\n')
			pass
	pass
#TODO: добавить приглашения пльзователей и написание сообщений
Main()