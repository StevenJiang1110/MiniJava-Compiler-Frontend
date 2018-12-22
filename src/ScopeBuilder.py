from MiniJavaListener import MiniJavaListener
from Class import Class
from Method import Method
from Symbol import Symbol
from ErrorReport import ErrorReport

class ScopeBuilder(MiniJavaListener):

    def __init__(self, classes, virtualSuperScope):
        self.classes = classes
        self.currentScope = virtualSuperScope

    def exitScope(self):
        self.currentScope = self.currentScope.getParentScope()

    def enterMainClass(self, ctx):
        className = ctx.name.text
        mainClass = Class(className, "<No Parent Class>", self.currentScope)
        self.currentScope.addSymbol(mainClass)
        self.classes[className] = mainClass

    def exitMainClass(self, ctx):
        self.exitScope()

    def enterClassDeclaration(self, ctx):
        if self.currentScope and self.currentScope.isValid():
            valid = True
        else:
            valid = False
        className = ctx.name.text

        if ctx.parent:
            parentClassName = ctx.parent.text
        else:
            parentClassName = "<No Parent Class>"

        if self.classes.get(className):
            ErrorReport.reportError(ctx.name, "Class already exists.")
            valid = False

        currentClass = Class(className, parentClassName, self.currentScope, valid)
        if valid:
            self.currentScope.addSymbol(currentClass)
        self.classes[className] = currentClass
        self.currentScope = currentClass

    def exitScopeDeclaration(self, ctx):
        self.exitScope()

    def enterMethodDeclaration(self, ctx):
        methodName = ctx.name.text
        methodReturnType = ctx.rtype

        if self.currentScope and self.currentScope.isValid:
            valid = True
        else:
            valid = False

        if self.currentScope.findLocalSymbol(methodName) is not None:
            ErrorReport.reportError(ctx.name, "Method already exists.")
            valid = False

        currentMethod = Method(methodName, methodReturnType, self.currentScope, valid)
        if valid:
            self.currentScope.addSymbol(currentMethod)
        self.currentScope = currentMethod

    def enterVarDeclaration(self, ctx):
        varType = ctx.vtype
        varName = ctx.name.text

        if self.currentScope and self.currentScope.isValid():
            valid = True
        else:
            valid = False

        if self.currentScope.findLocalSymbol(varName) is not None:
            ErrorReport.reportError(ctx.name, "Variable already exists.")
            valid = False

        currentVar = Symbol(varName, varType)
        if valid:
            self.currentScope.addSymbol(currentVar)


    def enterParamList(self, ctx):
        paramName = ctx.name.text
        paramType = ctx.ptype
        if self.currentScope and self.currentScope.isValid():
            valid = True
        else:
            valid = False

        self.currentScope.__class__ = Method
        if self.currentScope.findParam(paramName):
            ErrorReport.reportError(ctx.name, "Parameter already exists.")
            valid = False

        currentParam = Symbol(paramName, paramType)
        if valid:
            self.currentScope.addParam(currentParam)





