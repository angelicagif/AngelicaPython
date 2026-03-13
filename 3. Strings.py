################## 20 #################

# name = input("enter first name:  ")
# print(len(name))

################## 21 #################

# firstname = input("enter first name:  ")
# surname = input("enter surname:  ")

# fullname = firstname + " " + surname
# print(fullname)
# print(len(fullname))

# name = input("enter first name:  ")

################## 22 #################

# firstname = input("enter first name:  ").title()
# surname = input("enter surname:  ").title()

# name = firstname + " " + surname

# print(name)

################## 23 #################

# rhyme = input("enter first line of nursery rhyme:  ")
# print(len(rhyme))

# start = int(input("enter starting number:  "))
# end = int(input("enter ending number:  "))

# print(rhyme [start:end])

################## 24 #################

# word = input("enter a word:  ").upper()
# print(word)

################## 25 #################

# firstname = input("enter first name:  ")

# if len(firstname) < 5:
#     surname = input("enter surname:  ")
#     fullname = (firstname + surname)
#     print(fullname.upper())
# else:
#     print(firstname.lower())

################## 26 #################

word = input("enter a word:  ")

first = word[0]
length = len(word)
rest = word[1:length]

if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"
    
print(newword.lower())
