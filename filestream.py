import sys
import os.path
import glob
import zipfile
import timeit
from pprint import pprint


class Filestream:
    def __init__(self):
        self.files = None
        self.len = 0
        self.curfile = None
        self.curfilename = None
        self.index = 0

    def __exit__(self):
        pass

    def __str__(self):
        return ''.join(('--- Filestream  ---\n',
                        'Current file: ', self.curfilename, '\n',
                        str(self.files)))

#    def __iter__(self):
#        return self

#    def __next__(self):
#        line = next(self.curfile)
#        return line

    def isZipFile(self, filename):
        return '.zip' in filename
            

    def open(self, files):
        self.files = files
        self.len = len(files)
        self.curfile = None
        self.curfilename = None
        self.index = 0

        if self.index < self.len:
            if self.curfile:
                self.curfile.close()
                self.curfile = None
                  
            self.curfilename = self.files[self.index]
            if self.isZipFile(self.curfilename):
                with zipfile.ZipFile(f) as z:
                    with z.open('cn.txt') as zf:
                        self.curfile = zf
            else:
                self.curfile = open(f)
        self.index += 1

    def readline(self):
        line = next(self.curfile)
        if self.isZipFile(self.curfilename):
            line = str(line)[2:].split('|')
        return line


def tests():
    pattern = '~/projects/fec-data/*/cn*.*'
    files = glob.glob(pattern)
    
    fs = Filestream()
    fs.open(files)

    line = fs.readline()
    print('%s: %s' % (str(fs), line))
    

if __name__ == '__main__':
    tests()
