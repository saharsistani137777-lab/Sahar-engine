import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    lexer = Lexer(src)
    tokens = lexer.tokens()
    parser = Parser(tokens)
    program = parser.parse()  # فرض می‌کنیم parser کامل است
    interp = Interpreter()
    interp.eval(program)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python engine.py <file.se>")
        sys.exit(1)
    run_file(sys.argv[1])

