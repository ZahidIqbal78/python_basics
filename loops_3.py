print("-------------------------------------------------")
print("Using else in loop")

count = 0
while count < 10:
    print(count)
    count += 3
else:
    print("Current value of count is %s" % count)

print("-------------------------------------------------")

for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("For loop is terminated because of break, not due to failure")
