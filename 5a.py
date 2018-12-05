file = open('5.txt')
polymer = list(file.read())
polymer.pop()

reaction = True
totalDes = 0

while reaction:
    destroyed = False    
    i = 0
    r = True
    
    while r:
        f = polymer[i]
        s = polymer[i+1]
        if (f.isupper() != s.isupper()) and (f.lower() == s.lower()):
            del polymer[i:i+2]
            destroyed = True
            totalDes += 2
        i += 1
        if (i >= (len(polymer)) - 2):
            r = False

    if not destroyed:
        print (len(polymer) - 2)
        reaction = False














            
        

    
