import sys
import os.path
import argparse
import glob
import timeit

from pprint import pprint

from filestream import Filestream
from dbconfig import DBConfig


class DiskTable:
    def __init__(self, table):
        self.table = table
        self.datadic = DBConfig.getDataDic(table)
        self.fieldindex = DBConfig.getFieldIndex(table)
        self.files = DBConfig.getFilesAndArchives(table)
        self.fs = Filestream()
        self.fs.open(DBConfig.get)

    def __str__(self):
        return ''.join('--- DiskTable ' + self.table + ' ---\n',
                       'nDatafile = ', self.path, '\n')

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self.curfile)

    @property
    def dataDic(self):
        return self.datadic

    @property
    def name(self):
        return self.table


def tests():
    dt = DiskTable('CANDIDATE')
    pprint(dt.datadic)
    pprint(dt.fieldindex)

    line = dt.readline()
    print('%s: %s' % (dt.curfilename, line))
    

if __name__ == '__main__':
    tests()
