class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print "Doing stuff here without checking if __name__ == __main__"
print "person.py __name__: %s" % __name__
print "Do some inconvenient stuff here on the person package"
print type(__name__)

if __name__ == '__main__':
    print "This is only executed when I mean it to"
    will = Person('Will', 20)
    print("%s is %d years old" % (will.name, will.age))
