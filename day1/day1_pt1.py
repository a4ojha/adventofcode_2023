f = open("input.txt", "r")

sum = 0

for x in f:
    # x represents a line of input
    found_first = False
    for char in x:
        # if current char is an int
        if (ord(char) > 47 and ord(char) < 58):
            if found_first == False:
                first_digit = ord(char) - 48    # converts from char to int ('1' -> 1)
                last_digit = first_digit
                found_first = True
            else:
                last_digit = ord(char) - 48

    sum += (first_digit*10) + last_digit
    
f.close()
print(sum)
    
