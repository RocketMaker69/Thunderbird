TT_NUMBER   = "Number"
TT_STRING   = "String"
TT_NEWLINE  = "Newline"
TT_EOF      = "EOF"
TT_PLUS     = "Plus"
TT_MINUS    = "Minus"
TT_ASTERISK = "Asterisk"
TT_SLASH    = "Slash"
TT_MODULO   = "Modulo"
TT_POWER    = "Power"
TT_LPAREN   = "LParen"
TT_RPAREN   = "RParen"
TT_IDENT    = "Identifier"

class Token:
    def __init__(self, type_, value=None) -> None:
        self.type  = type_
        self.value = value
    
    def __repr__(self) -> str:
        return f"{self.type}: {self.value}" if self.value else f"{self.type}"
