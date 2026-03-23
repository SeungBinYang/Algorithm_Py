list1 = []
list2 = []
value = 12
hap = 0
for i in range(0,4):
    for k in range(0,3):
        list1.append(value)
        hap += value
        value -= 1
    list2.append(list1)
    list1 = []

for i in range(0, 4):
    for k in range(0, 3):
        print("%3d" % list2[i][k], end=" ")
    print(" ")

print("합은 %d" % hap)
