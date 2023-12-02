f = open("input.txt", "r")

sum = 0

def string_to_num(s):
    if s == "one":
        return 1
    elif s == "two":
        return 2
    elif s == "three":
        return 3
    elif s == "four":
        return 4
    elif s == "five":
        return 5
    elif s == "six":
        return 6
    elif s == "seven":
        return 7
    elif s == "eight":
        return 8
    elif s == "nine":
        return 9

def is_number_len3(string, start, end):
    if string[start:end] == "two" or string[start:end] == "one" or string[start:end] == "six":
        return True
    return False

def is_number_len4(string, start, end):
    if string[start:end] == "four" or string[start:end] == "five" or string[start:end] == "nine":
        return True
    return False

def is_number_len5(string, start, end):
    if string[start:end] == "three" or string[start:end] == "seven" or string[start:end] == "eight":
        return True
    return False


for line in f:
    # line represents a line of input
    found_first = False

    for i in range(len(line)):
        # see if substring is a spelled-out number
        # 3 letters
        if (is_number_len3(line, i, i+3)) == True:
            if found_first == False:
                first_digit = string_to_num(line[i:i+3])
                last_digit = first_digit
                found_first = True
            else:
                last_digit = string_to_num(line[i:i+3])
        # 4 letters       
        elif is_number_len4(line, i, i+4):
            if found_first == False:
                first_digit = string_to_num(line[i:i+4])
                last_digit = first_digit
                found_first = True
            else:
                last_digit = string_to_num(line[i:i+4])
        # 5 letters        
        elif is_number_len5(line, i, i+5):
            if found_first == False:
                first_digit = string_to_num(line[i:i+5])
                last_digit = first_digit
                found_first = True
            else:
                last_digit = string_to_num(line[i:i+5])

        # if current char is an int
        if (ord(line[i]) > 47 and ord(line[i]) < 58):
            if found_first == False:
                first_digit = ord(line[i]) - 48    # converts from char to int ('1' -> 1)
                last_digit = first_digit
                found_first = True
            else:
                last_digit = ord(line[i]) - 48

    print("Value = " + str(first_digit) + str(last_digit))
    sum += (first_digit*10) + last_digit
    
f.close()
print("Sum:", sum)
    
