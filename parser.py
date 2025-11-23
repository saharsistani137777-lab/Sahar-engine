from tokens import TokenType, Token
from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token(TokenType.EOF)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.advance()
        else:
            raise Exception(f"Expected {token_type} but got {self.current_token.type} at {self.current_token.line}:{self.current_token.col}")

    # ---------- Helpers ----------
    def parse(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
        return Program(statements)

    def statement(self):
        if self.current_token.type == TokenType.LET:
            return self.let_statement()
        elif self.current_token.type == TokenType.PRINT:
            return self.print_statement()
        elif self.current_token.type == TokenType.IF:
            return self.if_statement()
        elif self.current_token.type == TokenType.WHILE:
            return self.while_statement()
        else:
            return self.expression_statement()

    # ---------- Statements ----------
    def let_statement(self):
        self.eat(TokenType.LET)
        name = Identifier(self.current_token.value)
        self.eat(TokenType.IDENT)
        self.eat(TokenType.ASSIGN)
        value = self.expression()
        self.eat(TokenType.SEMI)
        return LetStatement(name, value)

    def print_statement(self):
        self.eat(TokenType.PRINT)
        expr = self.expression()
        self.eat(TokenType.SEMI)
        return PrintStatement(expr)

    def if_statement(self):
        self.eat(TokenType.IF)
        self.eat(TokenType.LPAREN)
        condition = self.expression()
        self.eat(TokenType.RPAREN)
        consequence = self.block()
        alternative = None
        if self.current_token.type == TokenType.ELSE:
            self.eat(TokenType.ELSE)
            alternative = self.block()
        return IfExpression(condition, consequence, alternative)

    def while_statement(self):
        self.eat(TokenType.WHILE)
        self.eat(TokenType.LPAREN)
        condition = self.expression()
        self.eat(TokenType.RPAREN)
        body = self.block()
        return WhileExpression(condition, body)

    def block(self):
        self.eat(TokenType.LBRACE)
        statements = []
        while self.current_token.type != TokenType.RBRACE:
            statements.append(self.statement())
        self.eat(TokenType.RBRACE)
        return BlockStatement(statements)

    # ---------- Expressions ----------
    def expression(self):
        return self.equality()

    def equality(self):
        node = self.comparison()
        while self.current_token.type in (TokenType.EQ, TokenType.NEQ):
            op = self.current_token.value
            self.advance()
            right = self.comparison()
            node = InfixExpression(node, op, right)
        return node

    def comparison(self):
        node = self.term()
        while self.current_token.type in (TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            op = self.current_token.value
            self.advance()
            right = self.term()
            node = InfixExpression(node, op, right)
        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token.value
            self.advance()
            right = self.factor()
            node = InfixExpression(node, op, right)
        return node

    def factor(self):
        node = self.unary()
        while self.current_token.type in (TokenType.STAR, TokenType.SLASH):
            op = self.current_token.value
            self.advance()
            right = self.unary()
            node = InfixExpression(node, op, right)
        return node

    def unary(self):
        if self.current_token.type == TokenType.MINUS:
            op = self.current_token.value
            self.advance()
            right = self.unary()
            return PrefixExpression(op, right)
        else:
            return self.primary()

    def primary(self):
        tok = self.current_token
        if tok.type == TokenType.NUMBER:
            self.advance()
            return NumberLiteral(tok.value)
        elif tok.type == TokenType.TRUE:
            self.advance()
            return BooleanLiteral(True)
        elif tok.type == TokenType.FALSE:
            self.advance()
            return BooleanLiteral(False)
        elif tok.type == TokenType.IDENT:
            self.advance()
            return Identifier(tok.value)
        elif tok.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            expr = self.expression()
            self.eat(TokenType.RPAREN)
            return expr
        else:
            raise Exception(f"Unexpected token {tok}")

