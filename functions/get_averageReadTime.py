data = [1010, 1342, 1234, 919, 1075]
total = 0

for time in data:
    total = total + (time // 60)

print("The average time spent reading this document is", (total // len(data)), " minutes.")
