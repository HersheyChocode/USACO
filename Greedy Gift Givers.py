"""
PROG: gift1
ID: //////
LANG: PYTHON2
TASK: test
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
file = fin.read().splitlines()

numFriends = int(file[0])
friends = []

for i in range(1,numFriends+1):
    friends.append([file[i],0])

line = numFriends+1 #counter forline

for i in range(numFriends):
    currentPerson = file[line]
    print(currentPerson, "current person")
    amt = int(file[line+1].split()[0])
    numPeople = int(file[line+1].split()[1])

    if amt!=0:
        for item in range(numFriends):
            if currentPerson in friends[item]:
                friends[item][1]-=amt
                friends[item][1]+=amt%numPeople
    line+=2

    if numPeople!=0:
        for j in range(1,numPeople+1):
            for item in range(numFriends):
                if file[line] in friends[item]:
                    friends[item][1]+=amt//numPeople
            line+=1
for each in range(numFriends):
    fout.write(str(friends[each][0])+" "+str(friends[each][1])+"\n")

fout.close()
