from ScopeMixin import ScopeMixin
from Symbol import Symbol


class Class(Symbol):

    def __init__(self, className, parentClassName, parentScope:ScopeMixin, valid = None):
        Symbol.__init__(self, className)
        self.parentClassName = parentClassName
        self.parentScope = parentScope
        self.symbols = dict()
        if valid is None:
            self.valid = True
        else:
            self.valid = valid

    def isValid(self):
        return self.valid

    def getName(self):
        return self.name

    def getParentScope(self):
        return self.parentScope

    def addSymbol(self, symbol):
        self.symbols[symbol.getName()] = symbol

    def findSymbol(self, name):
        if self.symbols.get(name):
            return self.symbols.get(name)
        else:
            if self.parentScope is None:
                return None
            result = self.parentScope.findSymbol(name)
            if result:
                return result
            else:
                parentClass = self.parentScope.findSymbol(self.parentClassName)
                if parentClass is None:
                    return None
                else:
                    parentClass.__class__ = Class
                    return parentClass.findSymbol(name)

    def findLocalSymbol(self,name):
        return self.symbols.get(name)

    def getParentClassName(self):
        return self.parentClassName


