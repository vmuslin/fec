import sys
import os.path
import argparse
import glob
import zipfile
import timeit
from pprint import pprint

from datadic import Config


class DiskTable:
    def __init__(self, table):
        self.table = table
        self.datadic = Config.getDataDic(table)
        self.fieldindex = Config.getFieldIndex(table)
        self.files = Config.getFilesAndArchives(table)
        self.curfile = None
        self.curfilename = None

    def __exit__(self):
        self.file.close()

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

    def openNextFile(self):
        for f in self.files:
            self.curfilename = f
            if '.zip' in f:
                with zipfile.ZipFile(f) as z:
                    with z.open('cn.txt') as zf:
                        self.curfile = zf
            else:
                ff = open(f)
                self.curfile = ff

    def readline(self):
        line = next(self.curfile)
        if '.zip' in self.curfilename:
            line = str(line)[2:].split('|')
        return line


def tests():
    dt = DiskTable('CANDIDATE')
    pprint(dt.datadic)
    pprint(dt.fieldindex)

    dt.openNextFile()
    line = dt.readline()
    print('%s: %s' % (dt.curfilename, line))
    

if __name__ == '__main__':
    tests()
