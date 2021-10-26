import re

result = []
for _ in range(int(input())):
    string = input()
    if len(string.split()) != 1:
        matches = re.findall(r'[\s:]([#][0-9abcdef]{6}|[#][0-9abcdef]{3})',string,flags=re.IGNORECASE)
        for i in matches:
            result.append(i)
    
for j in result:
    print(j)