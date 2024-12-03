final=0
a=list()
c=open("Advent of code'24/Day2/Day2_input.txt",'r')
cc=c.read()
ccc=cc.splitlines()
for i in ccc:
    a.append(i)

for j in range(1000):
    k=(a[j].split())   #per line list is K
    for l in k:
        if 