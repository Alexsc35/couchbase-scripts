#!/usr/bin/python
import sys

# Open and read the file as a single buffer

try:
	fd = open('ZooDatabase.sql', 'r')
	sqlFile = fd.readlines()
	for index, lines in enumerate(sqlFile):
		sqlFile[index] = lines.rstrip().lstrip()
except IOError , e:
	print 'error: file cannot be opened '  + str(e.errno) 
except:
	print "Unexpected error:", sys.exc_info()[0]
        raise
else:
	print 'msg: se ha leido correctamente el fichero SQL'
	fd.close()

# Execute every command from the input file
i = 0
comandoSQL = []
comandoSQL.append('')
for index , lines in enumerate(sqlFile):
	if lines.startswith('#') or lines.startswith('--') or lines=='':
		pass
	else:
		if lines.endswith(';'):
			comandoSQL[i] = comandoSQL[i] + str(lines) + ' '
			i += 1
			comandoSQL.append('')
		else:
			comandoSQL[i] = comandoSQL[i] + str(lines) + ' ' 

for  a, i in enumerate(comandoSQL):
	mi = i
	print mi
