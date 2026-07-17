a = " hello i am vansh rana "

count = 0
for ch in a.lower():
    if ch in "a,e,i,o,u":
        count +=1
print(count)        