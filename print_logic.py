#! /usr/bin/env python3

from pysmt.oracles import get_logic
from pysmt.smtlib.parser import get_formula
import argparse
from sys import stdin
import sys


def main(args):
    parser = argparse.ArgumentParser(
        description='Prints the logic used in a SMT-LIB2 formula(s). The SMT-LIB2 formula(s) should be provided in standard input (STDIN)')

    args = parser.parse_args(args)
    formula = get_formula(stdin)
    logic = get_logic(formula)

    print(logic.name)


if __name__ == '__main__':
    main(sys.argv[1:])
