one=0
two=0
c=open("Advent of code'24/Day 1/Day1_inputs.txt",'r')
cc=c.read()
ccc=cc.split()
a,b=list(),list()
for i in range(2000):
    if i%2==0:
        a.append(int(ccc[i]))
    else:
        b.append(int(ccc[i]))

a.sort()
b.sort()

#Puzzle 1
for j in range(1000):
    s=round(abs(a[j] - b[j]))
    one+=s

print(one)


#Puzzle 2
for k in range(1000):
    t=a[k]*b.count(a[k])
    two+=t

print(two)