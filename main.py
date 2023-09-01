# With this program, the user can extract characters from a given string

import random
input_string = input("Write down a sentence, and I'll extract some part of it" + " ")
index = random.randrange(len(input_string))
answer = "Your random string is:" + " "
print(answer + (input_string[index:]))