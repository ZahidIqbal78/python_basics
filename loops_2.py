print("-------------------------------------------------")

count = 0
while count < 5:
    print("This is count %s" % count)
    count += 1
    #count = count + 1

print("-------------------------------------------------")
print("Count & continue")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

print("-------------------------------------------------")