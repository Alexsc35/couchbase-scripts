#!/usr/bin/python
import sys
import readSQLfromFile

comandos = readSQLfromFile.readSQLfromFileClass ('/Users/alexsc/Documents/python/ZooDatabase.sql')
comandos.listar()
