nil = None
null = None
def buildClass(name='unnamed', param=[], func=['pass'], **kwargs):
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
def buildFunc(name='unnamed', param=[], func=['pass'], **kwargs):
	if param and param != [] and param != '' and param != ():
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
def doLoggedAction(action='pass', log='Logged!', iterateMethod='set', logToScreen=True, logFile=None):
	if not log:
		log = action
	assert (logToScreen or logFile), 'Logging is disabled!'
	assert (isinstance(action, str) or isinstance(action, list) or isinstance(action, tuple)), 'Code not processable!'
	if logFile:
		logFile = open(logFile, 'w')
	def doLog():
		if logToScreen:
			print(log)
		if logFile:
			logFile.write(log)
	if isinstance(action, str):
		exec(action, globals())
		doLog()
	elif isinstance(action, tuple) or isinstance(action, list):
		if iterateMethod == 'step':
			for i in action:
				exec(i, globals())
				doLog()
		else:
			for i in action:
				exec(i, globals())
			doLog()
	if logFile:
		logFile.close()
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
	lines[(line - 1)] = newText + '\n'
	f = open(file, 'w')
	f.writelines(lines)
	f.close()
class lineBreakdown:
	def __init__(self):
		print('raw(), list(), and length() are the attributes in this class.')
	def raw(self, line):
		if not isinstance(line, str):
			return 'Code not processable!'
		if isinstance(line, str) and line[-1] == '\n':
			line = line[:-1]
		return line
	def list(self, line):
		outLines = []
		itemIndex = 0
		for i in line:
			if i == '\n':
				outLines.append(line[:itemIndex])
				line = line[(itemIndex + 1):]
				itemIndex = 0
			else:
				itemIndex += 1
		if line != '':
			outLines.append(line)
		return outLines
	def length(self, origText, maxLength):
		if len(origText) <= maxLength:
			return origText
		outLines = []
		currentIndex = maxLength - 1
		while True:
			if len(origText) <= maxLength:
				if len(origText) >= 1:
					outLines.append(origText)
				return outLines
			if origText[currentIndex] == ' ' or origText[currentIndex] == '\n':
				outLines.append(origText[:currentIndex])
				origText = origText[(currentIndex + 1):]
				currentIndex = maxLength - 1
			elif not ('\n' in origText[:(maxLength - 1)]) and not (' ' in origText[:(maxLength - 1)]):
				outLines.append(origText[:(maxLength - 2)] + '-')
				origText = origText[(maxLength - 2):]
				currentIndex = maxLength - 1
			else:
				currentIndex -= 1