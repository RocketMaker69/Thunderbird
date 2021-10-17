from .tokens import *
from string import *

class Lexer:
    def __init__(self, code):
        self.code = code
        self.char = ""
        self.idx  = -1
        self.advance()
    
    def advance(self):
        self.idx += 1
        self.char = "(eof)" if self.idx >= len(self.code) else self.code[self.idx]
    
    def peek(self): return "(eof)" if self.idx + 1 >= len(self.code) else self.code[self.idx + 1]

    def build(self) -> list[Token]:
        tokens = []
        while self.char != "(eof)":
            if self.char in "0123456789":
                s = self.idx
                while self.char in "0123456789.": self.advance()
                num = self.code[s:self.idx]
                tokens.append(Token(TT_NUMBER, num))
            
            if self.char == "+":
                tokens.append(Token(TT_PLUS, self.char))
            if self.char == "-":
                tokens.append(Token(TT_MINUS, self.char))
            if self.char == "*":
                if self.peek() != "*": tokens.append(Token(TT_ASTERISK, self.char)) 
                else: 
                    tokens.append(Token(TT_POWER, self.char + self.peek()))
                    self.advance()
            if self.char == "/":
                tokens.append(Token(TT_SLASH, self.char))
            if self.char == "%":
                tokens.append(Token(TT_MODULO, self.char))
            if self.char == "(":
                tokens.append(Token(TT_LPAREN, self.char))
            if self.char == ")":
                tokens.append(Token(TT_RPAREN, self.char))
            if self.char in ascii_letters:
                s = self.idx
                while self.char in ascii_letters + "0123456789": self.advance()
                idt = self.code[s:self.idx]
                tokens.append(Token(TT_IDENT, idt))
            
            if self.char == "\n": tokens.append(Token(TT_NEWLINE))

            self.advance()
        
        tokens.append(Token(TT_EOF))
        return tokens
