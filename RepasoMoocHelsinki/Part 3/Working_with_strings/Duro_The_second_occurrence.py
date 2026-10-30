string = input("Please type in a string:")
sub_string = input("Please type in a substring:")

index1 = string.find(sub_string)
index2 = -1

if index1 != -1:
    index2 = string.find(sub_string, index1 + len(sub_string))

if index2 != -1:
    print(f"The second occurrence of the substring is at index {index2}.")
else:
    print(f"The substring does not occur twice in the string.")