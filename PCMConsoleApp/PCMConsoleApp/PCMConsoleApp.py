from datetime import datetime
from CourseClass import Course

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
	pass

commandsOperations = {
	"/help" : ShowHelp,
	"/exit" : "exit",
	"/showCourses" : ShowCourses,
	"/newCourse" : CreateCourse,
	"/newUser" : CreateUser
	}

commandsComments = {
	"/help" : "вывод всех допустимых комманд",
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
	fileDescriptor = open(usersFileName)
	pass

def GetCoursesFromFile():
	pass

Main()