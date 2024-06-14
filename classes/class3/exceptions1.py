# try:
#     age = int(input("What's your age? "))
#     print(f"Okay {age}.")
# except ValueError:
#     print("Please insert a correct value")

    #  BETTER WAY
# while True:
#     try:
#         age = int(input("What's your age? "))
#     except ValueError:
#         print("Please insert a correct value")
#     else:
#         break
# print(f"Okay {age}.")

  #  OR with funtions

def main():
    age = get_int()
    print(f"Okay {age}")

def get_int():
    # while True:
    #     try:
    #         age = int(input("What's your age? "))
    #     except ValueError:
    #         print("Please insert a correct value")
    #     else:
    #         return age
        
        # OR

    while True:
        try:
            return int(input("What's your age? "))
        except ValueError:
            print("Please insert a correct value")
        
main()