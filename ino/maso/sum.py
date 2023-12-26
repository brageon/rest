with open('lel') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        for num in line.split():
            if num.isdigit():
                total += int(num)
    print(total)
