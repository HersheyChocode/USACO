"""
PROG: ride
ID: email.h1
LANG: PYTHON2
TASK: test
"""

alphabet = ['A','B','C','D','E','F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

x = fin.read().splitlines()
print(x)
for line in x:
    line.strip("\n")
    print(line)
first = x[0]
second = x[1]

firstValue = 1
secondValue = 1


for letter in first:
    firstValue = firstValue * (alphabet.index(letter)+1)
for letter in second:
    secondValue = secondValue * (alphabet.index(letter)+1)

if firstValue%47==secondValue%47:
    fout.write("GO\n")
else:
    fout.write("STAY\n")
