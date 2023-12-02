def read_file(f_path):
    with open(f_path) as f:
        lines = f.readlines()
    return lines

def part_1(lines):
    desired = {"red": 12, "green": 13, "blue": 14}
    valid_games = []
    for game in lines:
        valid = True
        game_no, all_trials = game.split(": ")
        num_col = all_trials.split(" ")

        for i in range(1, len(num_col), 2):
            col = num_col[i][:-1] #removes trailing ,;\n
            num = int(num_col[i-1])
            if num > desired[col]:
                valid = False
                break

        if valid:
            _, game_no = game_no.split(" ")
            valid_games.append(int(game_no))
        
    print(sum(valid_games)) ##3059

def part_2(lines):
    powers = []
    for game in lines:
        max_col = {"red": 0, "green": 0, "blue": 0}
        game_no, all_trials = game.split(": ")
        num_col = all_trials.split(" ")

        for i in range(1, len(num_col), 2):
            col = num_col[i][:-1]
            num = int(num_col[i-1])
            if num > max_col[col]:
                max_col[col] = num

        power = max_col["red"] * max_col["green"] * max_col["blue"]
        powers.append(power)
    
    print(sum(powers)) #65371


lines = read_file("day2.txt")
part_1(lines)
part_2(lines)
