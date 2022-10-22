import math

'''Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.
'''

ab = 10
bc = 10

print(round(math.degrees(math.atan(ab/bc))), chr(176), sep='')