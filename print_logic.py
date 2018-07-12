#! /usr/bin/env python3

from pysmt.oracles import get_logic
from pysmt.smtlib.parser import SmtLibParser
import argparse
from sys import stdin
import sys


def get_formula(script_stream):
    """
    Returns the formula asserted at the end of the given script

    script_stream is a file descriptor.
    """

    parser = _SmtLibParser(None)
    script = parser.get_script(script_stream)
    return script.get_last_formula(None)

# Not really an error


class LogicFoundException(Exception):

    def __init__(self, logicName: str):
        self.logicName = logicName


class _SmtLibParser(SmtLibParser):
    def _cmd_set_logic(self, current, tokens):
        """(set-logic <symbol>)"""
        # User manually specified the lopic, so no need for pysmt to automatically guess
        elements = self.parse_atoms(tokens, current, 1)
        name = elements[0]
        # This is really hacky
        raise LogicFoundException(name)


def main(args):
    parser = argparse.ArgumentParser(
        description='Prints the logic used in a SMT-LIB2 formula(s). The SMT-LIB2 formula(s) should be provided in standard input (STDIN)')

    name = None

    try:
        args = parser.parse_args(args)
        formula = get_formula(stdin)
        logic = get_logic(formula)
        name = logic.name
    except LogicFoundException as e:
        name = e.logicName

    print(name)


if __name__ == '__main__':
    main(sys.argv[1:])
