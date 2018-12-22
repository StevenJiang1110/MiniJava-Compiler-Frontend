from antlr4 import CommonTokenStream
from antlr4 import InputStream
from antlr4 import ParseTreeWalker
from ErrorReport import ErrorReport
from ScopeBuilder import ScopeBuilder
from Class import Class
from SymbolChecker import SymbolChecker
from TypeChecker import TypeChecker
from MiniJavaLexer import MiniJavaLexer
from MiniJavaParser import MiniJavaParser


classes = dict()
virtualSuperScope = Class("<Virtual Super Scope>", "<No Parent Class>", None)

if __name__ =='__main__':
    f = open('../test_file/binarysearch.java')

    context = ''
    for line in f.readlines():
        context += line

    stream = InputStream(context)
    lexer = MiniJavaLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniJavaParser(tokens)

    parser.removeErrorListeners()

    tree = parser.goal()

    print(tree.toStringTree(recog=parser))

    walker = ParseTreeWalker()

    #scope
    scopeBuilder = ScopeBuilder(classes, virtualSuperScope)
    walker.walk(scopeBuilder, tree)
    ErrorReport.exitOnErrors()

    #symbol checker
    symbolChecker = SymbolChecker(classes, virtualSuperScope)
    walker.walk(symbolChecker, tree)
    ErrorReport.exitOnErrors()

    symbolChecker.checkCyclicInheritence()
    ErrorReport.exitOnErrors()

    #type checker
    typeChecker = TypeChecker(classes, virtualSuperScope)
    walker.walk(typeChecker, tree)
    ErrorReport.exitOnErrors()


