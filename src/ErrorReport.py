from antlr4 import *


class ErrorReport(object):
    errorCount = 0

    @classmethod
    def hasError(cls):
        return ErrorReport.errorCount > 0

    @classmethod
    def exitOnErrors(cls):
        if ErrorReport.hasError():
            print(str(ErrorReport.errorCount) + " errors found.")
            exit(-2)

    @classmethod
    def reportError(cls, ctx, msg):
        ErrorReport.errorCount += 1
        print("line:" + str(ctx.line) + ":" + msg)



