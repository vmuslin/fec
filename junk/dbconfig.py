import os
import glob
from pprint import pprint

import datadic
from datadic import DBSpec


class DBConfig:


    @staticmethod
    def getDataDic(tablename):
        return DBSpec['Tables'][tablename]['Fields']


    @staticmethod
    def getDataDirPattern():
        return DBSpec['DataDirPattern']


    @staticmethod
    def getFieldIndex(tablename): # dictionary { field_name : (index, datatype) }
        index = {}
        for count, tup in enumerate(DBConfig.getDataDic(tablename)):
            name = tup[0]
            datatype = tup[1]
            index[name] = (count, datatype)
        return index


    @staticmethod
    def getFilePattern(tablename):
        return DBSpec['Tables'][tablename]['FilePattern']


    @staticmethod
    def getFiles(tablename):
        pattern = os.path.join(DBConfig.getDataDirPattern(),
                               DBConfig.getFilePattern(tablename))
        files =  glob.glob(pattern)
        return files


    @staticmethod
    def getSep():
        return DBSpec['FieldSeparator']


    @staticmethod
    def setDataDirPattern(pattern):
        DBSpec['DataDirPattern'] = pattern


    @staticmethod
    def str(tablename):
        s = ''.join(('--- DBConfig ---\n',
                     '[DataDirPattern]\n', DBConfig.getDataDirPattern(), '\n',
                     '[FilePattern]\n', DBConfig.getFilePattern(tablename), '\n',
                     '[DataDic]\n'))
        for d in DBConfig.getDataDic(tablename):
            s += ''.join((str(d), '\n'))
        s += '[FileIndex]\n'
        for i in DBConfig.getFieldIndex(tablename).items():
            s += ''.join((str(i), '\n'))
        s += '[Files]'
        for f in DBConfig.getFiles(tablename):
            s += ''.join(('\n', f))
        return s


#--- Tests ---

def tests():
    tablename = 'CANDIDATE'
    DBConfig.setDataDirPattern(os.path.join('..', 'data', 'fec-data', '*'))
    print(DBConfig.str(tablename))

if __name__ == '__main__':
    tests()
