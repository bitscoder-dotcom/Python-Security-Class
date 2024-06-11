# firstNum = input("Enter First Number: ")
# secondNum = input("Enter Second Number: ")
#
# if int(firstNum) > int(secondNum):
#     print(firstNum)
# elif int(secondNum) > int(firstNum):
#     print(secondNum)
# else:
#     print("The numbers are equal")


# Write a program that prompts the user to enter their score(out of 100) and
# displays their corresponding grade based on the following criteria

"""
Scores 90 and above: Grade A
Scores 80 to 89: Grade B
Scores 70 to 79: Grade C
Scores 60 to 69: Grade D
Scores below 60: Grade E
"""

print("Please enter your Score to get your Grade: ")
score = int(input())
if score >= 90:
    age = int(input("Please enter your Age: "))
    if age <= 12:
        print("Your Grade is A+")
    else:
        print("Your Grade is A")
elif score >= 80:
    age = int(input("Please enter your Age: "))
    if age <= 12:
        print("Your Grade is B+")
    else:
        print("Your Grade is B")
elif score >= 70:
    age = int(input("Please enter your Age: "))
    if age <= 12:
        print("Your Grade is C+")
    else:
        print("Your Grade is C")
elif score >= 60:
    age = int(input("Please enter your Age: "))
    if age <= 12:
        print("Your Grade is D+")
    else:
        print("Your Grade is D")
else:
    print("Grade E")