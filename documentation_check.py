#!/usr/bin/python3

import sys
import ast


def check_documentation(filename):
    """
    checks the documentation in the give python file.
    Args:
    filename (str): The name of the python file to check.
    """
    with open(filename, 'r') as file:
        tree = ast.parse(file.read())

    missing_docstrings = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)) and not ast.get_docstring(node):
            missing_docstrings.append(node.name)


            if missing_docstrings:
                print(f"Missing documentation in {filename}:")
                for name in missing_docstrings:
                    print(f"- {name}")
                print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./documentation_check.py <filename.py> [filename2.py ...]")
        sys.exit(1)

    for filename in sys.argv[1:]:
        check_documentation(filename)
        
