from ScopeMixin import ScopeMixin
from Symbol import Symbol


class Class(Symbol, ScopeMixin):

    def __init__(self, className, parentName, parentScope):
        Symbol.__init__(self, className)
        self.parentName = parentName
        self.parentScope = parentScope
        self.valid = True

    def isValid(self):
        return self.valid

    def getName(self):
        return self.Name
