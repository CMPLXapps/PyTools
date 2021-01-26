__all__ = ['build', 'bc']
__version__ = '1.1.0'
#--------------------------------------------------------------------------------------------------
nil = None
null = None
findKey = lambda keyvalue, dictionary, *args, **kwargs: list(dictionary.keys())[list(dictionary.values()).index(keyvalue)]
objExists = lambda var, *args, **kwargs: bool(var in globals())
def doLoggedAction(action='pass', log='Logged!', iterateMethod='set', logToScreen=True, logFile=None, *args, **kwargs):
	if not log:
		log = action
	assert (logToScreen or logFile), 'Logging is disabled!'
	assert (isinstance(action, str) or isinstance(action, list) or isinstance(action, tuple)), 'Code not processable!'
	if logFile:
		logFile = open(logFile, 'w')
	def doLog(*args, **kwargs):
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
def clear(*args, **kwargs):
	unimportDossier = {'os': False, 'platform': False}
	if not (str(os).find('<module ') == 0 and str(os)[-1] == '>')
		import os
		unimportDossier['os'] = True
	if not (str(platform).find('<module ') == 0 and str(platform)[-1] == '>')
		import platform
		unimportDossier['platform'] = True
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	if unimportDossier['os']:
		del os
	if unimportDossier['platform']:
		del platform
def systemCheck(acceptedMachinesList=['Windows', 'Darwin', 'Linux'], *args, **kwargs):
	unimportDossier = {'os': False, 'platform': False}
	if not (str(platform).find('<module ') == 0 and str(platform)[-1] == '>')
		import platform
		unimportDossier['platform'] = True
	if unimportDossier['platform']:
		del platform
def replaceLine(file, line, newText, *args, **kwargs):
	f = open(file, 'r')
	lines = f.readlines()
	f.close()
	lines[(line - 1)] = newText + '\n'
	f = open(file, 'w')
	f.writelines(lines)
	f.close()
class lineBreakdown:
	def __init__(self, *args, **kwargs):
		print('raw(), list(), and length() are the attributes in this class.')
	def raw(self, line):
		if not isinstance(line, str):
			return 'Code not processable!'
		if isinstance(line, str) and line[-1] == '\n':
			line = line[:-1]
		return line
	def list(self, line, *args, **kwargs):
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
	def length(self, origText, maxLength, *args, **kwargs):
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
def println(string=''):
	import sys
	sys.stdout.write(string)
def execRequest(code='pass', *args, **kwargs):
	pass