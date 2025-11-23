class Node:
    pass

class Program(Node):
    def __init__(self, statements):
        self.statements = statements

class LetStatement(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PrintStatement(Node):
    def __init__(self, expr):
        self.expr = expr

class Identifier(Node):
    def __init__(self, name):
        self.name = name

class NumberLiteral(Node):
    def __init__(self, value):
        self.value = value

class BooleanLiteral(Node):
    def __init__(self, value):
        self.value = value

class InfixExpression(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class PrefixExpression(Node):
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

class IfExpression(Node):
    def __init__(self, condition, consequence, alternative=None):
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

class WhileExpression(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class BlockStatement(Node):
    def __init__(self, statements):
        self.statements = statements

