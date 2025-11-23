from tokens import Token, TokenType

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
        self.line = 1
        self.col = 1

    def advance(self):
        if self.current_char == '\n':
            self.line += 1
            self.col = 0
        self.pos += 1
        self.col += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def number(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(result), self.line, self.col)

    def identifier(self):
        result = ''
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        keywords = {
            'let': TokenType.LET,
            'print': TokenType.PRINT,
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'true': TokenType.TRUE,
            'false': TokenType.FALSE
        }
        token_type = keywords.get(result, TokenType.IDENT)
        return Token(token_type, result, self.line, self.col)

    def tokens(self):
        tokens = []
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                tokens.append(self.number())
            elif self.current_char.isalpha() or self.current_char == '_':
                tokens.append(self.identifier())
            elif self.current_char == '+':
                tokens.append(Token(TokenType.PLUS, '+', self.line, self.col))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TokenType.MINUS, '-', self.line, self.col))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TokenType.STAR, '*', self.line, self.col))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TokenType.SLASH, '/', self.line, self.col))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TokenType.LPAREN, '(', self.line, self.col))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TokenType.RPAREN, ')', self.line, self.col))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token(TokenType.LBRACE, '{', self.line, self.col))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TokenType.RBRACE, '}', self.line, self.col))
                self.advance()
            elif self.current_char == ';':
                tokens.append(Token(TokenType.SEMI, ';', self.line, self.col))
                self.advance()
            elif self.current_char == ',':
                tokens.append(Token(TokenType.COMMA, ',', self.line, self.col))
                self.advance()
            elif self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    tokens.append(Token(TokenType.EQ, '==', self.line, self.col))
                    self.advance()
                else:
                    tokens.append(Token(TokenType.ASSIGN, '=', self.line, self.col))
            else:
                raise Exception(f"Unknown character {self.current_char} at {self.line}:{self.col}")
        tokens.append(Token(TokenType.EOF, None, self.line, self.col))
        return tokens

