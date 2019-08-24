import sys
import os.path
import glob
import zipfile
import timeit
from pprint import pprint


class Zipstream:

    def __init__(self, names, pattern):

        self.names = names
        self.pattern = pattern
        self.len = len(names)
        self.curfile = None
        self.curname = None
        self.index = 0


    def __exit__(self):

        pass


    def __str__(self):

        return ''.join(('--- Filestream  ---\n',
                        'Current file: ', self.curname, '\n',
                        str(self.names)))

    #    def __iter__(self):
    #        return self


    #    def __next__(self):
    #        line = next(self.curfile)
    #        return line


    def close():

        if self.curfile:
            self.curfile.close()
            self.curfile = None


    def isZipFile(self, name):
        return zipfile.is_zipfile(name)
        # return '.zip' in name
            

    def openNext(self):

        if self.curfile is None:
            self.index = 0
        else:
            self.index += 1

        # if we have read the last file an out of range exception will be thrown
        # and the method will exit
        self.curname = self.names[self.index]

        if self.isZipFile(self.curname):
            # with zipfile.ZipFile(self.curfilename) as z:
            z = zipfile.ZipFile(self.curname)
            # with z.open('cn.txt') as zf:

            zf = z.open(self.pattern) # FIXME! - a temporary literal pattern
            self.curfile = zf
        else:
            self.curfile = open(self.curname)


    def readline(self):

        if self.curfile is None:
            self.openNext()

        line = next(self.curfile)

        if self.isZipFile(self.curname):
            return str(line)[2:]
        else:
            return line


def tests():
    folder = os.path.join('..', 'fec-data')
    pattern = 'cn.txt' # FIXME! - a temporary literal pattern
    aname = '2019-2020.zip'
    z = zipfile.ZipFile(os.path.join(folder, aname))
    zf = z.open(pattern)
    aname = '*.zip'
    arpath = os.path.join(folder, aname)
    archives = glob.glob(arpath)
    fpath = os.path.join(folder, pattern)
    files = glob.glob(fpath)
    
    zs = Zipstream(files + archives, pattern)
    line = zs.readline()
    print('%s: %s' % (str(zs), line))
    

if __name__ == '__main__':
    tests()
