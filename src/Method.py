from ScopeMixin import ScopeMixin
from Symbol import Symbol


class Method(Symbol, ScopeMixin):
    def __init__(self, methodName, returnType, parentScope, valid = None):
        Symbol.__init__(self, methodName)
        self.returnType = returnType
        self.parentScope = parentScope
        self.params = dict()
        self.locals = dict()
        self.paramTypes = dict()
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

    def addSymnbol(self, symbol):
        self.locals[symbol.getName()] = symbol

    def findSymbol(self, name):
        if self.params.get(name):
            return self.params.get(name)
        elif self.locals.get(name):
            return self.locals.get(name)
        else:
            if self.getParentScope() is None:
                return None
            else:
                return self.getParentScope().findSymbol(name)

    def findLocalSymbol(self,name):
        if self.params.get(name):
            return self.params.get(name)
        else:
            return self.locals.get(name)

    def addParam(self, param):
        self.params[param.getName()] = param
        self.paramTypes.add(param.getType())

    def findParams(self, name):
        return self.params.get(name)

    def getReturnType(self):
        return self.returnType

    def isCallListCompatible(self, callList):
        if callList == '':
            return len(self.paramTypes) == 0
        callNames = callList.spilt(',')
        if len(callNames) != len(self.paramTypes):
            return False
        for i in range(len(callNames)):
            if not Symbol.isTypeCompatible(self.paramTypes.get(i), callNames[i]):
                return False
        return True
