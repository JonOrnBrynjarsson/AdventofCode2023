import os

"""
Part 1

"""

def part1():
    print(' ')
   
    
"""
Part 2

"""    
def part2(GameSets):
    print(' ')
    
    
        
if __name__ == '__main__': 
    #file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Problem3a-Example.txt','r')
    #file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Problem3b-Example.txt','r')

    file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Input3.txt','r')
    all = file.read().splitlines()
       
    GameSets = []
    
    # Split lines
    for line in all:
        GameSets.append( line.split(':')[1].split(';'))
        
    part1(GameSets)
    part2(GameSets)