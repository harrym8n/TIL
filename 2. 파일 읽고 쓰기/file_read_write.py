with open('chicken.txt', 'r') as f:
    sum = 0
    count = 0
    for line in f:
        remove_blank = line.strip()
        sales = int(remove_blank.split(': ')[1])
        sum += sales
        count += 1

average = sum / count
print(average)
