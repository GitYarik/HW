l = [str(i)+str(i-1) for i in range(20)]



a = open("cheklist.txt","w")

for index in l:
    a.write(index + '+')
a.close()

v = open("cheklist.txt","r")
s = [line.strip() for line in v]
print(s)
v.close()