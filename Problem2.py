import os




"""
Part 1
Determine which games would have been possible if the bag had been loaded 
with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
What is the sum of the IDs of those games?
2685
"""

def part1(GameSets):
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    
    sumValidGames = 0
    
    for index, set in enumerate(GameSets):
        setPossible = True
        for game in set:
            if setPossible == False:
                break
            
            move = game.split(',')
            
            for color in move:
                items = color.split(' ')
                if items[2] == 'red' and int(items[1]) > maxRed:
                    setPossible = False
                    break
                elif items[2] == 'green' and int(items[1]) > maxGreen:
                    setPossible = False
                    break
                elif items[2] == 'blue' and int(items[1]) > maxBlue:
                    setPossible = False
                    break     
                
        if setPossible == True:
            sumValidGames += index+1
    print(sumValidGames)
    
"""
Part 2
For each game, find the minimum set of cubes that must have been present. 
What is the sum of the power of these sets?
83707
"""    
def part2(GameSets):
    sumValidGames = 0
    
    for set in GameSets:
        minRed = 0
        minGreen = 0
        minBlue = 0
        
        for game in set:            
            move = game.split(',')            
            for color in move:
                items = color.split(' ')                
                tala = int(items[1])                
                if items[2] == 'red' and tala > minRed:
                    minRed = tala
                    continue
                elif items[2] == 'green' and tala > minGreen:
                    minGreen = tala
                    continue
                elif items[2] == 'blue' and tala > minBlue:
                    minBlue = tala                    
                
        sumValidGames += minRed * minGreen * minBlue
        
    print(sumValidGames)
    
    
        
if __name__ == '__main__': 
    #file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Problem2a-Example.txt','r')
    #file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Problem2b-Example.txt','r')

    file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Input2.txt','r')
    all = file.read().splitlines()
       
    GameSets = []
    
    # Split lines
    for line in all:
        GameSets.append( line.split(':')[1].split(';'))
        
    part1(GameSets)
    part2(GameSets)