file = open('2.txt', 'r')
ids = [id.strip() for id in file]

# part 1 = 5704

twos, threes = 0, 0

for id in ids:
    occs = {}
    for letter in id:
        if letter in occs:
            occs[letter] += 1
        else:
            occs[letter] = 1
    for j in occs:
        if occs[j] == 2:
            twos += 1
            break
    for k in occs:
        if occs[k] == 3:
            threes += 1
            break

print (twos * threes)
        
# part 2 = umdryabviapkozistwcnihjqx

for i in ids:
    for j in ids:
        error = 0
        for k in range(26):
            if (i[k] != j[k]):
                error += 1
                if error > 1:
                    break
        if error == 1:
            # does not print actual answer
            print (i)
            print (j)
            
        








