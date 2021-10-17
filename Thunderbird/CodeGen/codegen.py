from Parser.ast import *

class CodeGen:
    def __init__(self, inputf, outputf) -> None:
        self.inputFile  = open(inputf, "r")
        self.outputFile = open(outputf, "w")
        self.outputFile.write("#include <stdio.h>\n")
        self.outputFile.write("\n")
        self.outputFile.write("void main() {\n")
        self.outputFile.write("printf(\"%f\", ")
    
    def generateExpr(self, ast):
        if isinstance(ast, BinaryOpNode):
            self.generateExpr(ast.left)
            self.outputFile.write(ast.op)
            self.generateExpr(ast.right)
        if isinstance(ast, NumberNode): self.outputFile.write(str(float(ast.val)))
        if isinstance(ast, MethodCallNode): self.outputFile.write(f"{ast.method}({ast.args});\n")