
def cross(a,b):
    return [s+t for s in a for t in b]

def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values



def only_choice(values):
    for box in unitlist:
        #print(box)
        for digit in '123456789':
            collect=[]
            for cell in box:
                if digit in values[cell]:
                    collect.append(cell)
            if(len(collect)==1):
                values[collect[0]]=digit
    return values



#modified sudoku by filling missing values
def boxValues(grid):
    sudoku={}
    for i in grid:
        if(grid[i]=='.'):
            sudoku[i]='123456789'
        else:
            sudoku[i]=grid[i]
    return sudoku


def display(values):
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return


def dictSudoku(boxes,sud):
    sudoku={}
    for i in range(len(sud)):
        sudoku[boxes[i]]=sud[i]
    return sudoku


def eliminate_o(values):
    def peers(A):
        if('ABC'.find(A[0])+1):
            first='ABC'
        elif('DEF'.find(A[0])+1):
            first='DEF'
        elif('GHI'.find(A[0])+1):
            first='GHI'
        if('123'.find(A[1])+1):
            second='123'
        elif('456'.find(A[1])+1):
            second='456'
        elif('789'.find(A[1])+1):
            second='789'
        return [s+t for s in first for t in second]

    for i in values:
        if(len(values[i])!=1):
            for c in cols:
                if(len(values[i[0]+c])==1 and (i[0]+c)!=i):
                    values[i]=values[i].replace(values[i[0]+c],'')
            for r in rows:
                if(len(values[r+i[1]])==1 and (r+i[1])!=i):
                    values[i]=values[i].replace(values[r+i[1]],'')
            for cr in peers(i):
                if(len(values[cr])==1 and cr!=i):
                    values[i]=values[i].replace(values[cr],'')
    return values
