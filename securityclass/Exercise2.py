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
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade E")