# MiniJava编译器前端
### 编译原理课程作业，读入miniJava程序文件，转化成AST，并进行错误处理
### 本项目代码在pycharm + python3.6下运行成功，运行前，需要安装antlr4-runtime
### 关于antlr4的下载使用可参见：
+ https://www.antlr.org/download.html
### 实现上主要借助了antlr4完成了对语法规则的解析和生成
### 借助了antlr preview 这个插件实现了AST的可视化
### 在错误处理方面，主要完成了以下几方面工作：
- Syntax Error Checker
- Scope Checker
- Symbol Checker
- Type Checker
### miniJava为Java的一个很小的子集，其介绍具体可参见
+ http://www.cambridge.org/us/features/052182060X/
### miniJava的语法具体可参见
+ http://www.cambridge.org/us/features/052182060X/grammar.html
