###PART 1###

from collections import Counter

file = open("7.txt")

all = []
disc_weights = {}
disc_programs = {}

for line in file:
    line = line.replace("-> ", "")
    line = line.replace(",", "")
    line = line.strip("\n")
    line = line.split(" ")
    disc_weights[line[0]] = line[1].strip("()")
    disc_programs[line[0]] = line[2::]
    del line[1]
    for i in line:
        all.append(i)
        
base = (Counter(all).most_common()[-1][0])

print (base)

###PART 2###

current_level = []
current_level.append(base)
new_level = []

balanced = True

while balanced:
    weight = 0
    weights = []
    for i in current_level:
        for j in disc_programs[i]:
            print (j)
            weight += int(disc_weights[j])
            new_level.append(j)
            for k in disc_programs[j]:
                weight += int(disc_weights[k])
            weights.append(weight)
            weight = 0
        print (weights)
        if len(set(weights)) > 1:
            print ("UNBALANCED: " +  str(weights))
            balanced = False
        weights = []
    current_level = new_level[::]
    new_level = []
    
print ()
