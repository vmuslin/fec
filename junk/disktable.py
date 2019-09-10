import sys
import os.path
import argparse
import timeit

from pprint import pprint

from fsreader import FileStreamReader
from dbconfig import DBConfig


class DiskTable:
    def __init__(self, tablename):
        self.tablename = tablename
        self.datadic = DBConfig.getDataDic(tablename)
        self.fieldindex = DBConfig.getFieldIndex(tablename)
        self.files = DBConfig.getFiles(tablename)
        self.fsr = FileStreamReader(self.files)

    def __str__(self):
        s = ''.join(('--- DiskTable ', self.tablename, ' ---\n'))
        for f in self.files:
            s = s.join(('nFiles = ', self.path, '\n'))
        return s

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.fsr)

    @property
    def dataDic(self):
        return self.datadic

    @property
    def name(self):
        return self.tablename


#--- Tests ---

def tests():
    tablename = 'CANDIDATE'
    DBConfig.setDataDirPattern(os.path.join('..', 'data', 'fec-data', '*'))
    print(DBConfig.str(tablename))
    dt = DiskTable(tablename)

    file = dt.fsr.filename
    for row in dt:
        if file != dt.fsr.filename:
            file = dt.fsr.filename
            print(file)
        #print(row)
    

if __name__ == '__main__':
    tests()
