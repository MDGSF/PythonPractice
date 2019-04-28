#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import collections
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])


def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER', r'\d+(\.\d*)?'),
        ('ASSIGN', r':='),
        ('END', r';'),
        ('ID', r'[A-Za-z]+'),
        ('OP', r'[+\-*/]'),
        ('NEWLINE', r'\n'),
        ('SKIP', r'[ \t]+'),
        ('MISMATCH', r'.'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)


def main():
    statements = '''
IF quantity THEN
    total := total + price * quantity;
    tax := price * 0.05;
ENDIF;
    '''

    for token in tokenize(statements):
        print(token)


if __name__ == "__main__":
    main()
