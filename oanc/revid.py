with open('ab.txt', 'r') as file:
    lines = file.readlines()
new_lines = []
for i in range(0, len(lines), 12):
    new_line = sum(int(line) for line in lines[i:i+12])
    new_line = round(float(new_line / 45), 1)
    new_lines.append(str(new_line) + '\n')
with open('ac.txt', 'w') as file:
    file.writelines(new_lines)