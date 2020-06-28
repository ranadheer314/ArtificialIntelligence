#!/usr/bin/env python
# coding: utf-8

from utils import *

rows="ABCDEFGHI"
cols="123456789"
boxes=cross(rows,cols)
stringSudoku='..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

row_units = [cross(r, cols) for r in rows]

column_units = [cross(rows, c) for c in cols]

square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


sudoku=dictSudoku(boxes,stringSudoku)
values=boxValues(sudoku)

def display(values):
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        sudoku=eliminate(values)
        sudoku=only_choice(sudoku)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def reducePuzzle(values):
    values=reduce_puzzle(values)
    if values is False:
        return False
    length=0
    for b in values.keys():
        if(len(values[b])==1):
            length+=1
    if(length==81):
        return values
    else:
        n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
        temp1=values[s]
        for one in temp1:
            valuesT=values.copy()
            valuesT[s]=one
            check=reducePuzzle(valuesT)
            if check:
                return check 
