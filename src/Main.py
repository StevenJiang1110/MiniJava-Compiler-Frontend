from antlr4 import CommonTokenStream
from antlr4 import InputStream
from MiniJavaLexer import MiniJavaLexer
from MiniJavaParser import MiniJavaParser


if __name__ =='__main__':
    f = open('../test_file/binarysearch.java')

    context = ''
    for line in f.readlines():
        context += line

    stream = InputStream(context)
    lexer = MiniJavaLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniJavaParser(tokens)

    tree = parser.goal()

    print(tree.toStringTree(recog=parser))
