from Lexer.lexer     import *
from Parser.ast      import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokIdx = -1
        self.ctoken = None
        self.ptoken = tokens[self.tokIdx + 1]
        self.advance()
    
    def advance(self):
        self.tokIdx += 1
        self.ctoken = "(end)" if self.tokIdx >= len(self.tokens) else self.tokens[self.tokIdx]
    
    def advancePeek(self):
        self.tokIdx += 1
        self.ptoken = "(end)" if self.tokIdx + 1 >= len(self.tokens) else self.tokens[self.tokIdx]
    
    def factor(self):
        ct = self.ctoken
        if ct.type == TT_NUMBER:
            self.advance()
            return NumberNode(ct.value)
    
    def term(self):
        left = self.factor()
        while self.ctoken.type in [TT_ASTERISK, TT_SLASH]:
            op = self.ctoken.value
            self.advance()
            right = self.factor()
            left = BinaryOpNode(left, op, right)
        return left
    
    def expr(self):
        left = self.term()
        while self.ctoken.type in [TT_PLUS, TT_MINUS]:
            op = self.ctoken.value
            self.advance()
            right = self.term()
            left = BinaryOpNode(left, op, right)
        return left
