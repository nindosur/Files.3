    # 1
with open('file1.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        for line in input_file:
            words = line.split()
            for word in words:
                if len(word) >= 7:
                    output_file.write(word + '\n')

    # 2
with open('file1.txt', 'r') as input_file:
    with open('output2.txt', 'w') as output_file:
        for line in input_file:
            output_file.write(line)

    # 3
with open('file1.txt', 'r') as f_in, open('output3.txt', 'w') as f_out:
    lines = f_in.readlines()
    lines_reversed = reversed(lines)
    for line in lines_reversed:
        f_out.write(line)

   # 4
with open('file1.txt', 'r') as f_in, open('output4.txt', 'w') as f_out:
    lines = f_in.readlines()
    last_index = -1
    for i in range(len(lines)-1, -1, -1):
        if ',' not in lines[i]:
            last_index = i
            break
    if last_index == -1:
        lines.append('************\n')
    else:
        lines.insert(last_index+1, '************\n')
    for line in lines:
        f_out.write(line)

    # 5
char = input("Введите символ: ")
count = 0
with open('file1.txt', 'r') as f:
    for line in f:
        words = line.split()
        for word in words:
            if word.startswith(char):
                count += 1
print(f"Количество слов, начинающихся на символ {char}: {count}")

    # 6
with open('file2.txt', 'r') as f_in, open('output6.txt', 'w') as f_out:
    for line in f_in:
        swapsimw = ''
        for char in line:
            if char == '*':
                swapsimw += '&'
            elif char == '&':
                swapsimw += '*'
            else:
                swapsimw += char
        f_out.write(swapsimw)

    # 7, 8
arr = ["Это", "массив", "строк", "!"]
with open('output7.txt', 'w') as f:
    for line in arr:
        f.write(line + '\n')

   # 9
chars = 0
with open("file1.txt", "r") as f:
    for line in f:
        chars += len(line)
    print(f"Колличество символов: {chars}")

    # 10
lines = 0
with open("file1.txt", "r") as f:
    for line in f:
        lines += 1
    print(f"Колличество строк: {lines}")