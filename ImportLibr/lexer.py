import re
import json

f = open("input.cpp", "r") 

with open('test.json') as f1:
  data = json.load(f1)

functions = set()
library = set()
commented = False

for x in f:
    check_cmte = re.findall("\*/", x)
    if len(check_cmte) > 0 and commented:
        commented = False
        for i in range(0,len(x)):
            if i < len(x) - 1 and x[i] == '*' and x[i+1] == '/':
                x = x[i+2:]
    if commented:
        continue
    check_cmts = re.findall("/\*", x)
    check_cmt = re.findall("//", x)
    
    if len(check_cmt) > 0:
        continue
    if len(check_cmts) > 0:
        commented = True
        continue
    xx = re.findall("find|find_of|sort|equal|all_of|for_each|find_if|find_each|find_end|fill|fill_n|max|min|minmax|merge|move\([a-z A-Z 0-9 , \+ \- \* \/]*\)", x)
    find_library = re.findall("#include\<[a-z A-Z  \. \* \/]*\>", x)
    if len(find_library) > 0 :
        #library[find_library[0]] = 1;
        library.add(find_library[0])
    if(len(xx) > 0):
        y = xx[0].split('(')
        #functions.append(y[0])
        functions.add(y[0])

f.close()
for func in functions:
    lbry = "#include<"+data[func]+">"
    if lbry in library:
        print(lbry + " is present!!!!!!")
    else:
        print(lbry + " is required for "+func)
        
