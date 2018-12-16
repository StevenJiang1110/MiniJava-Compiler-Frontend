# Generated from E:/python_work/miniJava_compiler/src\MiniJava.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete generic visitor for a parse tree produced by MiniJavaParser.

class MiniJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniJavaParser#goal.
    def visitGoal(self, ctx:MiniJavaParser.GoalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainClass.
    def visitMainClass(self, ctx:MiniJavaParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#paramList.
    def visitParamList(self, ctx:MiniJavaParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#type.
    def visitType(self, ctx:MiniJavaParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#statement.
    def visitStatement(self, ctx:MiniJavaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#ifStatement.
    def visitIfStatement(self, ctx:MiniJavaParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#whileStatement.
    def visitWhileStatement(self, ctx:MiniJavaParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printStatement.
    def visitPrintStatement(self, ctx:MiniJavaParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#assignment.
    def visitAssignment(self, ctx:MiniJavaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arrayAssignment.
    def visitArrayAssignment(self, ctx:MiniJavaParser.ArrayAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression.
    def visitExpression(self, ctx:MiniJavaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#orExpr.
    def visitOrExpr(self, ctx:MiniJavaParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#andExpr.
    def visitAndExpr(self, ctx:MiniJavaParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#compareExpr.
    def visitCompareExpr(self, ctx:MiniJavaParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#sumExpr.
    def visitSumExpr(self, ctx:MiniJavaParser.SumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#productExpr.
    def visitProductExpr(self, ctx:MiniJavaParser.ProductExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#callList.
    def visitCallList(self, ctx:MiniJavaParser.CallListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#rightValue.
    def visitRightValue(self, ctx:MiniJavaParser.RightValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#atom.
    def visitAtom(self, ctx:MiniJavaParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#nonAtom.
    def visitNonAtom(self, ctx:MiniJavaParser.NonAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#array.
    def visitArray(self, ctx:MiniJavaParser.ArrayContext):
        return self.visitChildren(ctx)



del MiniJavaParser