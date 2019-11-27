file = open("2.txt")

###PART 1###

tot = 0
for row in file:
    row = row.replace("\n", "")
    line = list(row.split("\t"))
    low = 10000
    high = 0  
    for number in line:
        number = int(number)
        if number < low:
            low = number
        if number > high:
            high = number
    tot += (high-low)

print (tot)

###PART 2###       

tot = 0
for row in open("2.txt"): 
    row = row.replace("\n", "")
    line = list(row.split("\t"))
    for x in line:
        x=int(x)
        for y in line:
            y=int(y)
            if divmod(x,y)[1] == 0 and divmod(x,y)[0] != 1:
                tot += divmod(x,y)[0] 

print (tot)
