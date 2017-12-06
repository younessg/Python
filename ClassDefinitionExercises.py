import os
import sys

class File:

     # In this example we are implementing prototype methods as in action script

    def __init__(self, name, extension, start):
        self.name = name
        self.extension = extension
        self.parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
        self.timestamp = ""
        self.size = ""
        self.lines = []
        self.content = self.getFileContent()
        self.counter = start

    def getFileContent(self):
        try:
            with open(self.name+self.extension) as f:
                for line in f:
                    self.lines.append(line.strip()+'\n')
                return self.lines
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)

    def __str__(self):
        return self.timestamp

    def next(self):
        if self.counter < 10:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

    def __iter__(self):
        return iter(self.lines)

    def __eq__(self, other):
        return self.name == other.name and self.lines == other.lines

    def __lt__(self, other):
        return self.name < other.name

    def __has__(self): 
        # For classes to be equal they must also have the same hash string!
        # "lines" string in this example must be the same for all equal classes
        # Files can now also be used as dictionary keys so we can have a set to fetch 
        content = '\n'.join(self.lines) 
        s = self.name + content
        return s.__hash__()

    def read(self):
        return self.lines

    def write(self, string):
        lines = string.splitlines()
        for line in lines:
            self.lines.append(line)
        return self.lines

    def countlines(self):
        return len(self.lines)


class MyFile:
    def __init__(self, n, start):
        self.name = n


f = File('myfile', '.txt', 5)
f.size = "10MB"
print f.name
print f.extension
print f.parent_directory
print f.content
print f.countlines()

#print f.next()
#print f.size

#for line in f.read():
#    print line

#mf = MyFile('README2', 2)
#print mf.name


