'''Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Function Description
Complete the minion_game in the editor below.
minion_game has the following parameters:
string string: the string to analyze
'''

def minion_game(string):
    stuart, kevin = 0, 0

    for i in range(len(string)):
        if string[i].upper() in 'AIEOU':
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin < stuart:
        print('Stuart', stuart)
    elif kevin == stuart:
        print('Draw')
    else:
        print('Kevin', kevin)


if __name__ == '__main__':
    s = input()
    minion_game(s)
