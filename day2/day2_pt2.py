'''
For each game, find the minimum set of cubes that must have been present. 
What is the sum of the power of these sets?
'''

f = open("input.txt", "r")

def count_semicolon(s):
    # rtype: int
    count = 0
    for i in s:
        if i == ";":
            count+=1
    return count

def nth_occurrence(string, char, n):
    """
    Find the nth occurrence of a character in a string.
    :rtype: int, -1 if not found
    """
    count = 0
    for i, c in enumerate(string):
        if c == char:
            count += 1
            if count == n:
                return i
    return -1

def string_to_int(string):
    string.replace(" ","")
    if string == "":
        return 0
    else:
        return int(string)
    
sum = 0            

for line in f:
    game_is_valid = True
    
    # Get ID of current game
    if line[6] == ":":              # Game 1-9
        ID = ord(line[5]) - 48
        start_pos = 8
    elif line[7] == ":":            # Game 10-99
        ID = (ord(line[5]) - 48)*10 + (ord(line[6]) - 48)
        start_pos = 9
    else:                           # Game 100-999
        ID = (ord(line[5]) - 48)*100 + (ord(line[6]) - 48)*10 + (ord(line[7]) - 48)
        start_pos = 10
        
        
    # Find how many sets were revealed in the current game:
    sets = count_semicolon(line) + 1
    
    # Make lists to store the values of each colour in a game
    reds = []
    greens = []
    blues = []
    
    # Loop through the sets
    for set in range(1, sets+1):
        if set < sets:
            semicolon_loc = nth_occurrence(line, ";", set)  
        else:
            semicolon_loc = len(line)-1
            
        current_set = line[start_pos-1:semicolon_loc+1]
        
        num_red=""
        num_green=""
        num_blue=""
        
        if "red" in current_set:
            num_red = current_set[current_set.index("red") - 3 : current_set.index("red")]
            
        if "green" in current_set:
            num_green = current_set[current_set.index("green") - 3 : current_set.index("green")]

        if "blue" in current_set:
            num_blue = current_set[current_set.index("blue") - 3 : current_set.index("blue")]
        
        red = string_to_int(num_red)
        green = string_to_int(num_green)
        blue = string_to_int(num_blue)       
        
        reds.append(red)
        greens.append(green)
        blues.append(blue)
        
        start_pos = semicolon_loc + 2
    
    # Find maximum of each colour
    min_red = max(reds)
    min_green = max(greens)
    min_blue = max(blues)
    power = min_red*min_green*min_blue
    
    sum += power
    
f.close()
print(sum)