import sys
import os.path
import argparse
import glob
import zipfile
import timeit
from pprint import pprint

from datadic import Config

class Args:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Retrieve contributiosn by candidate')
        parser.add_argument('name', help='name of a candidate')
        args = parser.parse_args()
        self.candidate = args.name

    @property
    def name(self):
        return self.candidate


class DataDic:
    def __init__(self, table):
        self.table = table
        self.datadic = Config.getFields(table)
        self.indexdic = self.buildIndex()

    def __str__(self):
        return ''.join(('--- DataDic ', self.table, ' ---\n',
                        str(self.datadic), '\n',
                        str(self.indexdic)))
        

class DiskTable:
    def __init__(self, table):
        self.table = table
        self.datadic = DataDic(table)
        self.files = self.datadic.getFilesAndArchives(table)
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

    def readline():
        
    for f in files:
        if '.zip' in f:
            with zipfile.ZipFile(f) as z:
                with z.open('cn.txt') as zf:
                    for line in zf:
                        print('%s: %s' % (f, str(line)[2:].split('|')))
                        break
        elif '.txt' in f:
            ff = open(f)
            for line in ff:
                print('%s: %s' % (f, str(line).split('|')))
                break


class Table:
    def __init__(self, table, fieldspec=None, data=[]):
        self.data = data
        self.table = table
        self.file = None
        if Config.isFile(table):
            self.path = Config.getPath(table)
            self.datadic = Config.getFields(table)
        else:
            self.path = None
            self.datadic = fieldspec

        self.fields = {} # dictionary { field_name : (index, datatype) }
        for count, tup in enumerate(self.datadic):
            name = tup[0]
            datatype = tup[1]
            self.fields[name] = (count, datatype)

        if self.path:
            self.open()

    def __exit__(self):
        self.file.close()

    def __str__(self):    
        s = 'Table = ' + self.table + '\n'
        if self.path:
            s += '\nDatafile = ' + self.path
        s += '\n' + str(self.data)
        s += 'Fields = ' + str(self.fields)
        return s

    @property
    def name(self):
        return self.table

    @property
    def dataDic(self):
        return self.datadic

    @property
    def resultSet(self):
        return self.data

    def dataType(self, field):
        return self.fields[field][1]

    def filter(self, mFields, value, pFields=None):
        data = []
        sep = Config.getSep()
        value = value.upper()
        index = self.index(mFields)

        fieldspec = self.datadic
        if pFields:
            fieldspec = self.makeFieldSpec(pFields)

        if self.data:
            for row in self.data:
                if row[index] == value:
                    data.append(self.rowProjection(row, pFields))
            return Table(self.table + '_filtered', fieldspec, data)
        else:
            if self.file:
                self.file.seek(0)
            for line in self.file.readlines():
                row = line[:-1].split(sep)
                if row[index] == value:
                    self.data.append(self.rowProjection(row, pFields))
                data = self.data
                if fieldspec:
                    self.datadic = fieldspec
            return Table(self.table + '_filtered', self.datadic, data)

    def index(self, field):
        return self.fields[field][0]

    def makeFieldSpec(self, pFields):
        if not pFields:
            return []

        fspec = []
        for f in pFields:
            fspec.append([f, self.dataType(f)])
        return fspec

    def open(self):
        if self.path:
            self.file = open(self.path, 'r')
        return self

    def printFields(self, fields, prefix='', sep='|'):
        for r in self.resultSet:
            print(self.rowToStr(r, fields, prefix))

    def printResultSet(self):
        for r in self.data:
            print(r)

    def reset(self):
        self.data = []
        if self.file:
            self.file.seek(0)

    def rowProjection(self, row, fields):
        if fields:
            data = []
            for f in fields:
                data.append(self.rowValue(row, f))
            return data
        else:
            return row

    def rowToStr(self, row, fields, prefix='', sep='|'):
        s = prefix
        for f in fields:
            dt = self.dataType(f)
            if dt == AMOUNT:
                s += '$'
            if dt == DATE:
                val = row[self.index(f)]
                s += val[0:2] + '/' + val[2:4] + '/' + val[4:] + sep
            else:
                s += row[self.index(f)] + sep
        return s

    def rowValue(self, row, field):
        return row[self.index(field)]

    def setSelect(self, fields):
        self.selectFields = fields


class Database:
    def __init__(self):
        self.sep = '|'
        self.cbi = Table('CBI')
        self.com = Table('COMMITTEE')
        self.can = Table('CANDIDATE')
        self.ccl = Table('CCL')

    def printDonors(self, candidate):
        print('Candidate = %s' % candidate)

        can = self.can.filter('CAND_NAME', candidate)

        candidate_row = can.resultSet[0]
        candidate_id = candidate_row[tlaib.index('CAND_ID')]
        print('Candidate id = %s' % candidate_id)

        ccl = self.ccl.filter('CAND_ID', candidate_id)

        for com in ccl.resultSet:
            com_id = candidate_committees.rowValue(com, 'CMTE_ID')
            print('Committee id = %s' % com_id)

            committees = self.com.filter('CMTE_ID', com_id)

            for row in committees.resultSet:
                com_name = committees.rowValue(row, 'CMTE_NM')
                print('Committee name = %s' % com_name)
            
            prefix = self.sep.join((candidate, com_name + self.sep))
            
            print('Contributions:')

            donors = self.cbi.filter('CMTE_ID', com_id)

            donors.printFields(fields=('NAME',
                                       'CITY',
                                       'STATE',
                                       'ZIP_CODE',
                                       'EMPLOYER',
                                       'OCCUPATION',
                                       'TRANSACTION_DT',
                                       'TRANSACTION_AMT'),
                               prefix=prefix,
                               sep=self.sep)


def main():
    args = Args()
    candidate = args.candidate.upper()

    Db = Database()
    Db.printDonors(candidate)

def test():
    can = Table('CANDIDATE')
    print(can)
    pprint(can.datadic)

    can.filter('CAND_NAME', 'tlaib, rashida')
    print(can)
    pprint(can.datadic)
    can.printResultSet()

    can2 = can.filter('CAND_NAME', 'tlaib, rashida', ('CAND_ID', 'CAND_NAME', 'CAND_CITY'))
    print(can2)
    pprint(can2.datadic)
    can2.printResultSet()

    can3 = can2.filter('CAND_NAME', 'tlaib, rashida', ('CAND_ID', 'CAND_NAME'))
    print(can3)
    pprint(can3.datadic)
    can3.printResultSet()

if __name__ == '__main__':
#    main()
#    test()

    files = glob.glob('data/*/cn*.zip')
    files.extend(glob.glob('data/*/cn*.txt'))

    pprint(files)

    for f in files:
        if '.zip' in f:
            with zipfile.ZipFile(f) as z:
                with z.open('cn.txt') as zf:
                    for line in zf:
                        print('%s: %s' % (f, str(line)[2:].split('|')))
                        break
        elif '.txt' in f:
            ff = open(f)
            for line in ff:
                print('%s: %s' % (f, str(line).split('|')))
                break
            
