import os

#file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Problem1a-Example.txt','r')
#file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Problem1b-Example.txt','r')

file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Input1.txt','r')
all = file.read().splitlines()

textNums = ['  ','one','two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']

def extract_num(line, firstpart):
    nums = []
    txtnum = ''
    for ltr in line:
        # If letter is number, no need to go furhter
        if ltr.isdigit():
            nums.append(ltr)
            continue
        if firstpart:
            continue
            
        txtnum = txtnum + ltr
                
        if len(txtnum) > 2:
            for num in textNums:
                if num in txtnum:
                    nums.append(str(textNums.index(num)))
                    
                    txtnum = txtnum.replace(num[0:1:],str(textNums.index(num)))
                    break
    
    return nums
        

# Adds the numbers for the second part
def sum_all_nums(numss):
    sumAll = 0
    for nums in numss:
        if len(nums) > 1:
            number = nums[0] + nums[::-1][0]
        else:
            number = nums[0]*2
        sumAll += int(number)
    print(sumAll)


"""
    The newly-improved calibration document consists of lines of text; 
    each line originally contained a specific calibration value that the 
    Elves now need to recover. On each line, the calibration value can be 
    found by combining the first digit and the last digit (in that order) 
    to form a single two-digit number.
"""
def run_part_one(all):
    total = 0
    listNums = []
    
    for line in all:
        lineNum = ''
        lineNum = extract_num(line, True)
        
        linerev = line[::-1]
        lineNum = extract_num(linerev, True)
        listNums.append(lineNum)
        
    for num in listNums:
        total += int(num[0]) + int(num[::-1][0])

    print(total)
    
"""
    Your calculation isn't quite right. It looks like some of the digits 
    are actually spelled out with letters: one, two, three, four, five, 
    six, seven, eight, and nine also count as valid "digits".

    Equipped with this new information, you now need to find the real first 
    and last digit on each line.
"""    
def run_part_two(all):
    listNums = []
    
    for line in all:        
        listNums.append(extract_num(line, False))
        
    sum_all_nums(listNums)
    

if __name__ == '__main__':    
    run_part_one(all)
    run_part_two(all)