# Sahar-engine
A professional interpreter engine for a custom language — Sahar Engine
# Sahar Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Sahar Engine** is a professional interpreter for a custom language.  
Features:

- Lexer, Parser, AST, Interpreter
- let, print, if/else, while
- Numbers, strings, booleans
- Lexical scoping
- CLI for running `.se` scripts

## Usage
```bash
python engine.py samples/example.se
engine.py        # CLI entrypoint
lexer.py         # Tokenizer
tokens.py        # Token definitions
parser.py        # Parser -> AST
ast_nodes.py     # AST node classes
interpreter.py   # Evaluator
runtime.py       # Environment + builtins
samples/         # Sample programs
tests/           # Test scripts

Clone the repository:
```bash
git clone https://github.com/<saharsistani137777-lab>/Sahar-Engine.git
cd Sahar-Engine

