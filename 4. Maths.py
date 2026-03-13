import math
################## 27 #################

# num1 = float(input("enter a number with lots of decimal places:  "))

# print(num1*2)

################## 28 #################

# num = float(input("enter a number with lots of decimal places:  "))
# answer = num * 2
# print(round (answer, 2))

################## 29 #################

# num = int(input("enter an integer over 500:  "))
# answer = math.sqrt(num)

# print(round(answer, 2))

################## 30 #################

# print(round(math.pi, 5))

################## 31 #################

# radius = int(input("enter radius of circle:  "))
# area = math.pi * radius**2

# print(area)

################## 32 #################

# radius = int(input("enter radius of cylinder:  "))
# depth = int(input("enter depth of cylinder:  "))

# area = math.pi * radius**2
# volume = area * depth
# print("the total volume is ", (round(volume, 3)))

################## 33 #################

# num1 = int(input("enter a first number:  "))
# num2 = int(input("enter a second number:  "))

# divide = num1 // num2
# remain = num1 % num2

# print(num1, "divided by",num2, "is",divide, "with",remain, "remaining")

################## 34 #################

print("1) Square\n2) Triangle")
num = int(input("Enter a number:  "))

if num == 1:
    length = int(input("enter length of one side:  "))
    print("the area is",length**2)

elif num == 2:
    base = int(input("Enter a base length: "))
    height = int(input("Enter a height length: "))
    answer = (base*height)/2
    print("the area is", answer)

else:
    print("error, enter correct value")



