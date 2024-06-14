import sys

# if len(sys.argv) < 3:
#     sys.exit("Too Few Arguments")
# elif len(sys.argv) > 3:
#     sys.exit("Too many arguments")

# print ("Your name is", sys.argv[1])

# Working with slice of a list ie, a part or subset of a list

if len(sys.argv) < 3:
    sys.exit("Too Few Arguments")

# The [1:] starts from the element at the second indices to the end
for arg in sys.argv[1:]: 
    print ("Your name is", arg)