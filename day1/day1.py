import time

def read_file(f_path):
    with open(f_path) as f:
        lines = f.readlines()
    return lines

def part_1(lines):
    to_add = []
    for line in lines:
        f_line = line
        b_line = line[::-1]
        found_f = False
        found_b = False

        for f_char, b_char in zip(f_line, b_line):
            if not found_f and f_char.isnumeric():
                found_f = f_char
            if not found_b and b_char.isnumeric():
                found_b = b_char
            
            if found_f and found_b:
                break
        
        line_no = int(found_f + found_b)
        to_add.append(line_no)

    print(sum(to_add)) #54634

def part_2(lines):
    num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    str_to_num = {word: str(num) for num, word in enumerate(num_words, start=1)}
    
    to_add = []
    for line in lines:
        line_dict = {}
        for ind, char in enumerate(line):
            if char.isnumeric():
                line_dict[ind] = char
        
        for num_word, num in str_to_num.items():
            ind = 0-len(num_word)
            while num_word in line[ind+len(num_word):]:
                ind = line.index(num_word, ind+len(num_word))
                line_dict[ind] = num

        min_ind = min(list(line_dict.keys()))
        max_ind = max(list(line_dict.keys()))
        line_no = int(line_dict[min_ind] + line_dict[max_ind])
        to_add.append(line_no)

    print(sum(to_add)) #53855

start = time.time()        
lines = read_file("day1.txt")
read = time.time()
part_1(lines)
end1 = time.time()
part_2(lines)
end2 = time.time()

print("Time taken to read:", read-start)
print("Time taken for part1:", end1-read)
print("Time taken for part2:", end2-end1)
