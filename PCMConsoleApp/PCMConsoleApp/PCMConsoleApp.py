from datetime import datetime
from CourseClass import Course
from UsersClasses import *

def ShowHelp(commands):
	print("\nВозможные команды:")
	for command in commands:
		print("{name} — {description}".format(name=command[0], description=command[1]))
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
	fileDescriptor.write(login, firstName, lastName, role, sep=';', )
	pass

def HandleUserInput():
	commands = (
	("/help", "вывод всех допустимых команд"),
	("/showCourses", "отображение всех имеющихся курсов"),
	("/newCourse", "запуск помощника по созданию курса"),
	("/exit", "выход из программы")
	)

	command = input("Введите /help для получения справки по командам или введите команду для исполнения: ")
	while (True):
		if (command == commands[0][0]):
			ShowHelp(commands)
		elif (command == commands[1][0]):
			ShowCourses()
		elif (command == commands[2][0]):
			CreateCourse()
		elif (command == commands[3][0]):
			break

		else:
			print("Команда \"{0}\" неизвестна. Введите действительную команду.".format(command))
		command = input("Новая команда: ")
	pass


currentUser = None
courses = []
users = []
fileNameUsers = "DataFiles/Users.txt"
fileNameCourses = "DataFiles/Courses.txt"
currentPosition = None

def Main():
	users = GetUsersFromFile()
	courses = GetCoursesFromFile()
	
	HandleUserInput()

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