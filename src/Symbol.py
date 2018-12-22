from MainParameter import MainParameter

class Symbol(object):
    def __init__(self, name, type = None):
        self.name = name
        self.type = type

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    @classmethod
    def isPrimitiveType(cls, type):
        return type == 'int' or type == 'int[]' or type == 'boolean'

    @classmethod
    def isTypeCompatible(cls, typeA, typeB):
        if typeA == typeB:
            return True
        elif Symbol.isPrimitiveType(typeA) or Symbol.isPrimitiveType(typeB):
            return False
        else:
            while not typeB == '<No Parent Class>':
                if typeA == typeB:
                    return True
                typeB = MainParameter.classes.get(typeB).getParentName()
            return False

