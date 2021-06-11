# Monk and Suffix Sort
# Monk loves to play games. On his birthday, his friend gifted him a string S. 
# Monk and his friend started playing a new game called as Suffix Game. 
# In Suffix Game, Monk's friend will ask him lexicographically  smallest suffix of the 
# string S. Monk wants to eat the cake first so he asked you to play the game.


s,k = map(str,input().split())
arr =[]
for i in range(len(s)):
    arr.append(s)
    s = s[1:]
arr.sort()
print(arr[int(k)-1])