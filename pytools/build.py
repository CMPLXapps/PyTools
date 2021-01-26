class obj:
	def classobj(name='unnamed', param=[], func=['pass'], *args, **kwargs):
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
	def func(name='unnamed', param=[], func=['pass'], *args, **kwargs):
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
	def var(name='unnamed', value=None, *args, **kwargs):
		globals()[name] = value
class classtype:
	def type(name='unnamed_datatype', varAttrs={'class_vars': [], 'instance_vars': []}, funcAttrs=[], initCodeStr=[], internalCode=[], *args, **kwargs):
		#Assertion Block
		assert (isinstance(name, str)), f'Name of type must be str, not {type(name)}'
		assert (isinstance(varAttrs, dict)), f'Variable Attributes must be stored in type \'dict\'\nas keys \'class_vars\' and \'instance_vars\''
		assert (isinstance(varAttrs['class_vars'], ))
		class execblock:
			string = f'class {name}:'
			raw = [
				f'	{classVarsStr}',
				'	def __init__(self)',
				f'		{instanceVarsStr}',
				f'		{initCodeStr}',
				'	def __str__(self):',
				f'		return "{name}()"',
				'	def __repr__(self):',
				f'		{reprStr}',
				f'	{funcAttrsStr}',
				f'	{internalCodeStr}']
		for i in execblock.raw:
			execblock.string += '\n' + i
		exec(execblock.string, globals())