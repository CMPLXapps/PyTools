# PyTools (Version 1.1.0)

Just a collection of useful tools.

## Installation

To install this, either:

* Download the  source code from the `main` branch or one of the releases, and use it in your project, or

* Use `pip install pytools-ca` on Windows and some Linux Distros, or
      `pip3 install pytools-ca` on other Linux Distros.

## Features

`nil`  & `null` ::

Shorthand values for for the `None` boolean value.

`findKey(keyvalue, dictionary)` :: 

Finds the value of a specified key in a dictionary.
*Currently will return the first value in the dictionary with the specified key*

	findkey(1, {'first_key': 2, 'second_key': 1, 'third_key': 1}) ==>

	'second_key'

`doLoggedAction(action='pass', log='Logged!', iterateMethod='set', logToScreen=True, logFile=None)` ::

Executes a block of code and logging it either on the screen or in a file. Set `logToScreen` to False
to only print to a file, and pass a path to a file as `logFile` to log the code to the file.

	doLoggedAction(action='print(\'Hello World!\')', log='Printed!') ==>
	
	Hello World!
	Printed!

`clear()` ::

Clears the screen regardless of what system is used.

	clear()

`systemCheck(acceptedMachines=['Windows', 'Darwin', 'Linux'])` ::

Makes sure the machine the program is run on can properly run the program.

	systemCheck(['Windows', 'Linux'])

`replaceLine(file, line, newText)` ::

Takes in a path to a file, the number of the line you want to change in the file, and the string you want to change it to, and replaces that line.

	../text_files/a_file.txt ==>
	
	A
	B
	This is NOT a .txt file!
	
	replaceLine('../text_files/a_file.txt', 3, 'This is a .txt file!') ==>
	
	../text_files/a_file.txt ==>
	
	A
	B
	This is a .txt file!

#### Class `lineBreakdown` :: 

A class with multiple related functions in it.

`length(origText, maxLength)` :: 

Takes a long string and breaks it down into a list of strings that conform to specified length requirements.

	lineBreakdown('Yesterday, I had work from 9:00 AM to 5:00 PM, and then I had to visit the grocery store.', 10) =>
	
	['Yesterday,', 'I had work', 'from 9:00', 'AM to 5:00', 'PM, and', 'then I had', 'to visit', 'the', 'grocery', 'store']
	
	lineBreakdown('Cardiovascular', 10) =>
	
	['Cardiovas-', 'cular']

`raw(line)` :: 

Removes the '\n' at the end of a string if it exists, this is meant for quickly iterating through a file.

	lineBreakdown().raw('Hello World!\n') =>
	
	'Hello World!'
	
	lineBreakdown().raw('Hello World!') =>
	
	'Hello World!'

`list(line)` :: 

Breaks down a line into a list of string that were previously joined by a '\n'.

	lineBreakdown().list('To-do List:\n- Water the plants.\n- Exercise.\n- Go to the grocery store for bread and milk.') =>
	
	['To-do List:', '- Water the plants.', '- Exercise.', '- Go to the grocery store for bread and milk.']


### `build` Submodule

#### `obj` Class

`func(name='unnamed', param=[], func=['pass'], \*\*kwargs)` ::

A function that will build dynamically named and defined functions and classes respectively.
	
	buildFunc(
		name='a_function',
		param=[
			'value_1',
			'value_2'
		],
		func=[
			'a_variable = value_1 + value_2',
			'print(a_variable)'
		],
		)

`classobj`

