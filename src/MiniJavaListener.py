# Generated from E:/python_work/miniJava_compiler/src\MiniJava.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete listener for a parse tree produced by MiniJavaParser.
class MiniJavaListener(ParseTreeListener):

    # Enter a parse tree produced by MiniJavaParser#goal.
    def enterGoal(self, ctx:MiniJavaParser.GoalContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#goal.
    def exitGoal(self, ctx:MiniJavaParser.GoalContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mainClass.
    def enterMainClass(self, ctx:MiniJavaParser.MainClassContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mainClass.
    def exitMainClass(self, ctx:MiniJavaParser.MainClassContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#paramList.
    def enterParamList(self, ctx:MiniJavaParser.ParamListContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#paramList.
    def exitParamList(self, ctx:MiniJavaParser.ParamListContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#type.
    def enterType(self, ctx:MiniJavaParser.TypeContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#type.
    def exitType(self, ctx:MiniJavaParser.TypeContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#statement.
    def enterStatement(self, ctx:MiniJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#statement.
    def exitStatement(self, ctx:MiniJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#ifStatement.
    def enterIfStatement(self, ctx:MiniJavaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#ifStatement.
    def exitIfStatement(self, ctx:MiniJavaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#whileStatement.
    def enterWhileStatement(self, ctx:MiniJavaParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#whileStatement.
    def exitWhileStatement(self, ctx:MiniJavaParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#printStatement.
    def enterPrintStatement(self, ctx:MiniJavaParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#printStatement.
    def exitPrintStatement(self, ctx:MiniJavaParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#assignment.
    def enterAssignment(self, ctx:MiniJavaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#assignment.
    def exitAssignment(self, ctx:MiniJavaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#arrayAssignment.
    def enterArrayAssignment(self, ctx:MiniJavaParser.ArrayAssignmentContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#arrayAssignment.
    def exitArrayAssignment(self, ctx:MiniJavaParser.ArrayAssignmentContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expression.
    def enterExpression(self, ctx:MiniJavaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expression.
    def exitExpression(self, ctx:MiniJavaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#orExpr.
    def enterOrExpr(self, ctx:MiniJavaParser.OrExprContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#orExpr.
    def exitOrExpr(self, ctx:MiniJavaParser.OrExprContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#andExpr.
    def enterAndExpr(self, ctx:MiniJavaParser.AndExprContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#andExpr.
    def exitAndExpr(self, ctx:MiniJavaParser.AndExprContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#compareExpr.
    def enterCompareExpr(self, ctx:MiniJavaParser.CompareExprContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#compareExpr.
    def exitCompareExpr(self, ctx:MiniJavaParser.CompareExprContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#sumExpr.
    def enterSumExpr(self, ctx:MiniJavaParser.SumExprContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#sumExpr.
    def exitSumExpr(self, ctx:MiniJavaParser.SumExprContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#productExpr.
    def enterProductExpr(self, ctx:MiniJavaParser.ProductExprContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#productExpr.
    def exitProductExpr(self, ctx:MiniJavaParser.ProductExprContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#callList.
    def enterCallList(self, ctx:MiniJavaParser.CallListContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#callList.
    def exitCallList(self, ctx:MiniJavaParser.CallListContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#rightValue.
    def enterRightValue(self, ctx:MiniJavaParser.RightValueContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#rightValue.
    def exitRightValue(self, ctx:MiniJavaParser.RightValueContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#atom.
    def enterAtom(self, ctx:MiniJavaParser.AtomContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#atom.
    def exitAtom(self, ctx:MiniJavaParser.AtomContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#nonAtom.
    def enterNonAtom(self, ctx:MiniJavaParser.NonAtomContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#nonAtom.
    def exitNonAtom(self, ctx:MiniJavaParser.NonAtomContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#array.
    def enterArray(self, ctx:MiniJavaParser.ArrayContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#array.
    def exitArray(self, ctx:MiniJavaParser.ArrayContext):
        pass


