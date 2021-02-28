class ImportMirrorObject:
	class MirrorInfoAttributeType:
		def __init__(self, string, *args, **kwargs):
			
		def __repr__(self, *args, **kwargs):
			return 'TemporaryImportMirrorObject.MirrorInfoAttribute()'
	def __init__(self, module, mirror_name=False, *args, **kwargs):
		if not mirror_name:
			mirror_name = module
		exec(f'import {self.__mirror__} as {self.__mirror_name__}', globals())
	def __repr__(self, *args, **kwargs):
		return f'<TemporaryImportMirrorType object mirroring \'{self.__mirror__}\' (\'{self.__mirror_name__}\')>'
	def __str__(self, *args, **kwargs):
		return f'TemporaryImportMirrorObject({self.__mirror__}, {self.__mirror_name__})'
	def __del__(self, *args, **kwargs):
		exec(f'del {self.__mirror__}', globals())
		del self
	@property
	def new(self):
		return ImportMirrorObject()
	def unimport(self, *args, **kwargs):
		self.__del__()
isimported = lambda module: ((str(module).find('<module ') == 0 and str(module)[-1] == '>') and module in list(globals().keys()))