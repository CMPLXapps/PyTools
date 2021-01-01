nil = None
null = None
getFuncParams = lambda func: {"parameters": func.__code__.co_varnames, "count": func.__code__.co_argcount}
def buildClass(name='unnamed', param=[], func=['pass'], getDict=False, funcDict={}, **kwargs):
	if getDict:
		name = funcDict['name']
		param = funcDict['param']
		func = funcDict['func']
	if param != []:
		paramstr = param[0]
		del param[0]
		for i in param:
			paramstr = paramstr + ', ' + i
		paramstr = '(' + paramstr + '):'
	else:
		paramstr = ':'
	funcstr = ''
	for i in func:
		funcstr = funcstr + '\n\t' + i
	exec('class ' + name + paramstr + funcstr, globals())
def buildFunc(name='unnamed', param=[], func=['pass'], funcDict=None, **kwargs):
	if not isinstance(funcDict, dict):
		name = funcDict['name']
		param = funcDict['param']
		func = funcDict['func']
	if param != []:
		paramstr = param[0]
		del param[0]
		for i in param:
			paramstr = paramstr + ', ' + i
	else:
		paramstr = ''
	funcstr = ''
	for i in func:
		funcstr = funcstr + '\n\t' + i
	exec('def ' + name + '(' + paramstr + '):' + funcstr, globals())
def doLoggedAction(action='pass', defaultLog='Action Performed!', logToScreen=True, logFile=None):
	if logFile:
		logFile = open(logFile, 'w')
		logFileText = ''
	if not logToScreen and logFile == None:
		return 'Logging is disabled!'
	if not isinstance(action, str) or not isinstance(action, list) or not isinstance(action, tuple):
		return 'Code not iterable!'
	if isinstance(action, str):
		exec(action, globals())
		if logToScreen:
			print(defaultLog)
		if logFile:
			logFile.write(defaultLog + '\n')
	elif isinstance(action, list):
		for i in action:
			if isinstance(i, tuple):
				exec(i, globals())
				if logToScreen:
					print(i[1])
				if logFile:
					logFile.write(i[1] + '\n')
			elif isinstance(i, str):
				exec(i, globals())
				if logToScreen:
					print(defaultLog)
				if logFile:
					logFile.write(defaultLog + '\n')
	elif isinstance(action, tuple):
		if isinstance(action[0], tuple):
			for i in action[0]:
				exec(i, globals())
			if logToScreen:
				if action[1]:
					print(action[1])
				else:
					print(defaultLog)
			if logFile:
				if action[1]:
					logFile.write(action[1])
				else:
					logFile.write(defaultlog)
		if isinstance(action[0], list):
			for i in action[0]:
				exec(i, globals())
				if logToScreen:
					if action[1]:
						print(action[1])
					else:
						print(defaultLog)
				if logFile:
					if action[1]:
						logFile.write(action[1])
					else:
						logFile.write(defaultLog)
		if isinstance(action[0], str):
			exec(action[0], globals())
			if logToScreen:
				if action[1]:
					print(action[1])
				else:
					print(defaultLog)
			if logFile:
				if action[1]:
					logFile.write(action[1] + '\n')
				else:
					logFile.write(defaultLog + '\n')
	logFile.close()
	return
def clear():
	try:
		with os.listdir('.') as temp:
			pass
	except:
		import os
	try:
		with platform.system() as temp:
			pass
	except:
		import platform
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
def systemCheck(acceptedMachinesList=['Windows', 'Darwin', 'Linux']):
	try:
		with platform.system() as temp:
			pass
	except:
		import platform
	if not platform.system() in accepted_machines:
		return 'Invalid OS!'
	else:
		return 'Valid OS!'
def replaceLine(file, line, newText):
	f = open(file, 'r')
	lines = f.readlines()
	f.close()
	lines[line] = newText
	f = open(file, 'w')
	f.writelines(lines)
	f.close()
def lineBreakdown(origText, maxLength, outputAsList=True):