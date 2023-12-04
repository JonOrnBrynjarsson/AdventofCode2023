import os





"""
Part 1

906040027786 too high
511086 too low
"""

def part1():
    print(' ')
    
    
def   check_num(all, rownum, colnum):
    
    punctuation = '*+=%-#@/&$'
    
    rowMax = len(all[0])
    colMax = len(all)
    
    # top
    if rownum > 0:
        if all[rownum-1][colnum-1] in punctuation:
            return True
        elif all[rownum-1][colnum] in punctuation:
            return True
        elif colnum < colMax-1 and all[rownum-1][colnum+1] in punctuation:
            return True
    # bottom
    if rownum < rowMax-1:
        if colnum > 0 and all[rownum+1][colnum-1] in punctuation:
            return True
        elif all[rownum+1][colnum] in punctuation:
            return True
        elif colnum < colMax-1 and  all[rownum+1][colnum+1] in punctuation:
            return True
    # right
    if colnum < colMax-1:
        if all[rownum][colnum+1] in punctuation:
            return True        
    # left
    if colnum > 0:
        if all[rownum][colnum-1] in punctuation:
            return True
    return False
        
    
    
    
    
    
   
    
"""
Part 2

"""    
def part2():
    print(' ')
    
    
"""
The engine schematic (your puzzle input) consists of a visual representation of the engine. 
There are lots of numbers and symbols you don't really understand, 
but apparently any number adjacent to a symbol, even diagonally, 
is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
"""        
if __name__ == '__main__': 
    #file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Problem3a-Example.txt','r')
    #file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Problem3b-Example.txt','r')

    file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Input3.txt','r')
    all = file.read().replace('.',' ').splitlines()
    
    txt = ''
    for line in all:
        for ltr in line:
            if not ltr.isdigit() and ltr != ' ':   
                txt += ltr
    sum = 0
    
    rowMax = len(all[0])
    colMax = len(all)
    isPartnum = False
    num = ''
    for row in range(0,rowMax,1):
        if num != '' and isPartnum == True:
            sum += int(num)
            print(num,' sum: ',sum)
        num = ''
        isPartnum = False
        if row in (83,139):
            print('tékka')
        for col in range(0,colMax,1):       
            if all[row][col].isdigit(): # still adding to num
                if len(num) > 3:
                    print(num, row, col)
                num += all[row][col]    
             
                if isPartnum == False:  # still need to check if next to symbol       
                    isPartnum = check_num(all, row, col) 
            elif num != '' and isPartnum == True:
                sum += int(num)
                print(num,' sum: ',sum)
                num = ''    
                isPartnum = False
            else:
                num = ''
    if isPartnum == True and num != '':
        sum += int(num)      
    print(sum)
                                        
                
                    
                    