from datetime import datetime
from CourseClass import Course
from UsersClasses import *

def ShowHelp():
	print("\nВозможные команды:")
	for command in commandsOperations:
		print(command, sep='', end=' — ')
		try:
			print(commandsComments[command])
		except KeyError:
			print("описание команды отсутствует")
	pass

def ShowCourses():
	for course in courses:
		print("{name} from {start} to {end} by {creator}".format(name=course.name, start=course.startDate, end=course.endDate, creator=course.creator))
	pass

def CreateCourse():
	def ReadDates():
		beginString = input("Введите дату начала курса (ДД.ММ.ГГГГ): ")
		begin = datetime.strptime(beginString, "%d.%m.%Y")
		endString = input("Введите дату окончания курса (ДД.ММ.ГГГГ): ")
		end = datetime.strptime(beginString, "%d.%m.%Y")
		return (begin, end)

	courseName = input("\nВведите название курса: ")
	courseStart, courseEnd = ReadDates()
	newCourse = Course(courseName, courseStart, courseEnd)
	newCourse.description = input("Введите описание для курса:\n")

	courses.append(newCourse)
	pass

def CreateUser():
	print("Введите ваши...")
	login = input("\tлогин: ")
	firstName = input("\tимя: ")
	lastName = input("\tфамилия: ")
	while (True):
		role = input("\tдолжность (T - преподаватель, S - студент): ")
		if (role == 'T'):
			users.append(Teacher(login, firstName, lastName))
			break
		elif (role == 'S'):
			users.append(Student(login, firstName, lastName))
			break
		else:
			print("Выберите T, если вы преподаваетль, либо S, если вы студент. Других вариантов нет.")
	fileDescriptor = open(fileNameUsers, 'a')
	pass

commandsOperations = {
	"/help" : ShowHelp,
	"/exit" : "exit",
	"/showCourses" : ShowCourses,
	"/newCourse" : CreateCourse,
	"/newUser" : CreateUser
	}

commandsComments = {
	"/help" : "вывод всех допустимых команд",
	"/exit" : "выход из программы",
	"/showCourses" : "отображение всех имеющихся курсов",
	"/newCourse" : "запуск помощника по созданию курса"
	}

currentUser = None
courses = []
users = []
fileNameUsers = "Users.txt"
fileNameCourses = "Courses.txt"


def Main():
	users = GetUsersFromFile()
	courses = GetCoursesFromFile()
	command = input("Введите /help для получения справки по командам или введите команду для исполнения: ")
	while (True):
		try:
			operation = commandsOperations[command]
			if (operation != "exit"):
				operation()
			else:
				break

		except KeyError:
			print("Команда \"{0}\" неизвестна. Введите действительную команду.".format(command))
		command = input("Новая команда: ")

	print("Выполнение программы завершено.")
	pass

def GetUsersFromFile():
	fileDescriptor = open(fileNameUsers)
	rawData = fileDescriptor.readlines()
	for line in rawData:
		login, firstName, lastName, role = line.split(';')
	pass

def GetCoursesFromFile():
	pass

Main()