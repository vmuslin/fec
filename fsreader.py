# FilestreamReader

class FileStreamReader:

    def __init__(self, names):
        self.names = names
        self.len = len(names)
        self.curname = None
        self.index = 0
        self.rowcount = 0
        # self.curfile is a reference to the currently open file object from the files.
        # specified in the list self.names. If the reference is None, then no object
        # current file is open and this is a new list.
        self.curfile = None


    # __enter__ method is used to implement the "with" statement
    def __enter__(self):
        return self


    # __exit__ method is used to implement the "with" statement
    def __exit__(self, type, value, traceback):
        self.close()


    # __iter__ method is used to implement interation over the FileStreamReader object
    def __iter__(self):
        return self


    # __iter__ method is used to implement interation over the FileStreamReader object
    def __next__(self):
        return self.readline()


    def __str__(self):
        return ''.join(('--- FileStreamReader  ---\n',
                        'Current file: ', str(self.curname), '\n',
                        str(self.names)))


    @property
    def count(self):
        return self.rowcount


    @property
    def filename(self):
        return self.curname


    def close(self):
        if self.curfile:
            self.curfile.close()
        self.curfile = None
        self.curname = None
        self.index = 0
        self.len = 0
        self.rowcount = 0
    

    def openNext(self):
        if self.curfile is None:
            self.index = 0
            self.rowcount = 0
        else:
            self.index += 1

        # if we have read the last file an out of range IndexError exception will be raised
        # and the method will exit
        if self.index < self.len:
            self.curname = self.names[self.index]
            self.curfile = open(self.curname)
            return True
        else:
            if self.curfile is not None:
                self.curfile.close() 
            return False


    def readline(self):
        if self.curfile is None:
            if not self.openNext():
                raise StopIteration
        try:
            line = next(self.curfile)
            self.rowcount += 1
        except StopIteration:
            self.curfile.close()
            if not self.openNext():
                raise StopIteration
            line = self.readline()
                
        return line[:-1]


#--- Tests ---

import glob
def tests():
    pattern = '*.py'
    files = glob.glob(pattern)
    
    with FileStreamReader(files) as fs:
        #fs.open(files)
        prevname = ""
        for line in fs:
            if fs.filename != prevname:
                prevname = fs.filename
                print(fs.filename)
        print('[Done %d]' % fs.count)
    

if __name__ == '__main__':
    tests()
