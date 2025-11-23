from ast_nodes import *
from runtime import Environment, truthy

class Interpreter:
    def __init__(self):
        self.env = Environment()

    def eval(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.eval(stmt)
        elif isinstance(node, LetStatement):
            val = self.eval(node.value)
            self.env.set(node.name.name, val)
        elif isinstance(node, PrintStatement):
            val = self.eval(node.expr)
            print(val)
        elif isinstance(node, NumberLiteral):
            return node.value
        elif isinstance(node, BooleanLiteral):
            return node.value
        elif isinstance(node, Identifier):
            return self.env.get(node.name)
        elif isinstance(node, InfixExpression):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.operator == '+': return left + right
            if node.operator == '-': return left - right
            if node.operator == '*': return left * right
            if node.operator == '/': return left // right
            if node.operator == '==': return left == right
            if node.operator == '!=': return left != right
            if node.operator == '<': return left < right
            if node.operator == '>': return left > right
            if node.operator == '<=': return left <= right
            if node.operator == '>=': return left >= right
            raise Exception(f"Unknown operator {node.operator}")
        elif isinstance(node, PrefixExpression):
            right = self.eval(node.right)
            if node.operator == '-': return -right
            raise Exception(f"Unknown prefix operator {node.operator}")
        elif isinstance(node, BlockStatement):
            result = None
            for stmt in node.statements:
                result = self.eval(stmt)
            return result
        else:
            raise Exception(f"Unknown node {node}")

