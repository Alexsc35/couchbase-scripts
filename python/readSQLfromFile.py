import sys
class readSQLfromFileClass ( object ):

	def __init__(self , File ):

		self.i = 0
		self.comandoSQL = []
		self.comandoSQL.append('')
		self.mi = ''
		self.File = File 
		try:
			self.fd = open(self.File, 'r')
			self.sqlFile = self.fd.readlines()
			for index, lines in enumerate(self.sqlFile):
				self.sqlFile[index] = lines.rstrip().lstrip()
		except IOError , e:
			print 'error: file cannot be opened '  + str(e.errno) + self.File
		except:
			print "Unexpected error:", sys.exc_info()[0]
       			raise
		else:
			print 'msg: se ha leido correctamente el fichero SQL'
			self.fd.close()

			for index , lines in enumerate(self.sqlFile):
				if lines.startswith('#') or lines.startswith('--') or lines=='':
					pass
				else:
					if lines.endswith(';'):
						self.comandoSQL[self.i] = self.comandoSQL[self.i] + str(lines) + ' '
						self.i += 1
						self.comandoSQL.append('')
					else:
						self.comandoSQL[self.i] = self.comandoSQL[self.i] + str(lines) + ' ' 
	def listar(self):
		for  a, i in enumerate(self.comandoSQL):
			self.mi = i
			print self.mi

