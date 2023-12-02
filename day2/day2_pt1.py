'''
Determine which games would have been possible if the bag had been loaded with only 
12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
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
        
        if red > 12 or green > 13 or blue > 14:
            game_is_valid = False 
            break
        
        start_pos = semicolon_loc + 2
    
    # Now that we know if current game is valid or false, update sum
    if game_is_valid:
        sum += ID
    
f.close()
print(sum)
