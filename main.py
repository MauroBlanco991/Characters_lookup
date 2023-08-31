#With this program, the user can see the position of a character in a string
word = input("Give me a word!")
character = input("Give me a character that appears in the word!")
if character in word:
    position = word.find(character)
    print(position)
else:
    print("You have to give me a character that appears in the word!")