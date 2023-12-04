
"""
The Elf leads you over to the pile of colorful cards. 
There, you discover dozens of scratchcards, all with their opaque 
covering already scratched off. Picking one up, it looks like each 
card has two lists of numbers separated by a vertical bar (|): 
a list of winning numbers and then a list of numbers you have. 
You organize the information into a table (your puzzle input).

Part 1:
As far as the Elf has been able to figure out, you have to figure 
out which of the numbers you have appear in the list of winning numbers. 
The first match makes the card worth one point and each match after the 
first doubles the point value of that card.

Part 2:
Copies of scratchcards are scored like normal scratchcards and have the same
card number as the card they copied. So, if you win a copy of card 10 and 
it has 5 matching numbers, it would then win a copy of the same cards that 
the original card 10 won: cards 11, 12, 13, 14, and 15. 
This process repeats until none of the copies cause you to win any more cards. 
(Cards will never make you copy a card past the end of the table.)
"""        


if __name__ == '__main__': 
    #file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Problem4a-Example.txt','r')
    #file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Problem4b-Example.txt','r')

    file = open('C:\Forritun\PythonStuff\AdventOfCode2023\Input\Input4.txt','r')
    all = file.read().replace('.',' ').splitlines()
    
    sum = 0 
    sum2 = 0   
    cardcopies = [1 for x in range(216)]
    for index, line in enumerate(all):
        line = line.replace('Card ',' ')
        cardnr = line.split(':')[0]
        win, card = line.split(':')[1].split(' | ')
        
        
        card = card.split(' ')            
        win = win.split(' ')
        cardwin = 0
        for w in win:
            if w != '':
                ind = card.count(w)
                if ind > 0:
                    cardwin += 1
        if cardwin > 0:
            sum += 2**(max(0,cardwin-1))
            currwinings = cardcopies[index]
            for i in range(cardwin):       
                if index + i <= len(cardcopies):         
                    cardcopies[index + i+1] += currwinings
    print('Total part 1: ', sum)
    for l in cardcopies:
        sum2 += l
    print('Total part2:', sum2)                
        
# 23941 part 1,         
# 5571760 part 2, 