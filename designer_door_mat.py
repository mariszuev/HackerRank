'''Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
'''
n, m = map(int, input().split())

s = 'WELCOME'
r = '.|.'

for i in range(n // 2):
    print((r * ((i * 2) + 1)).center(m, '-'))

print(s.center(m, '-'))

for i in range(n // 2 - 1, -1, -1):
    print((r * ((i * 2) + 1)).center(m, '-'))