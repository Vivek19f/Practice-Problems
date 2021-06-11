# The Minion Game

# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string,S .
# Both players have to make substrings using the letters of the string S .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String  S= BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

def minion_game(string):
    # your code goes here
    vowel =['A','E','I','O','U']
    K=0
    S=0
    for i in range(len(string)):
        if string[i] in vowel:
            K += len(string)-i
        else:
            S += len(string)-i
    if K>S:
        print("Kevin {0}".format(K))
    elif S>K:
        print("Stuart {0}".format(S))
    else:
        print("Draw")
        
    
if __name__ == '__main__':
    s = input()
    minion_game(s)