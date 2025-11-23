from enum import Enum, auto

class TokenType(Enum):
    # Arithmetic
    PLUS = '+'
    MINUS = '-'
    STAR = '*'
    SLASH = '/'

    # Delimiters
    LPAREN = '('
    RPAREN = ')'
    LBRACE = '{'
    RBRACE = '}'
    SEMI = ';'
    COMMA = ','

    # Assignment & comparison
    ASSIGN = '='
    EQ = '=='
    NEQ = '!='
    LT = '<'
    GT = '>'
    LTE = '<='
    GTE = '>='

    # Keywords
    LET = auto()
    PRINT = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    TRUE = auto()
    FALSE = auto()

    # Literals & identifiers
    IDENT = auto()
    NUMBER = auto()
    STRING = auto()
    
    EOF = auto()

class Token:
    def __init__(self, type_, value=None, line=1, col=1):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f"Token({self.type}, {self.value}, {self.line}:{self.col})"

