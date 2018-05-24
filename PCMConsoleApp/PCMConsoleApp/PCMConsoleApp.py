def ShowHelp():
	print("\nВозможные команды:")
	for command in commandsOperations:
		print("{name} — {comment}".format(name=command, comment=commandsComments[command]))
	pass

def ShowCourses():
	pass

def CreateCourse():
	pass

commandsOperations = {
	"/help" : ShowHelp,
	"/exit" : "exit",
	"/showCourses" : ShowCourses,
	"/newCourse" : CreateCourse
	}

commandsComments = {
	"/help" : "вывод всех допустимых комманд",
	"/exit" : "выход из программы",
	"/showCourses" : "отображение всех имеющихся курсов",
	"/newCourse" : "запуск помощника по созданию курса"
	}

def Main():
	command = input("Введите /help для получения справки по командам или введите команду для исполнения: ")
	while (True):
		try:
			operation = commandsOperations[command]
			if (operation != "exit"):
				operation()
			else:
				break

		except:
			print("Команда \"{0}\" неизвестна. Введите действительную команду.".format(command))
		command = input("Новая команда: ")

	print("Выполнение программы завершено.")
	pass

Main()