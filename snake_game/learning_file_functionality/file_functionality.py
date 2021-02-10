# file = open("first-file.txt")
# text = file.read()
# print(text)
#
#
# # MUST CLOSE THE FILE WHEN OPENED WITH THIS TECHNIQUE
# file.close()


# DON'T HAVE TO CLOSE THE FILE
# with open("first-file.txt") as file:
#     text = file.read()
#     print(text)


# # Write to a file
# with open("first-file.txt", mode="w") as file:
#     file.write("Overriding the file")


# # Append to a file
# with open("first-file.txt", mode="a") as file:
#     file.write("\nAppending to the file")

# make a new file to write (python will automatically create the file)
# with open("automatically_created_file.txt", mode="w") as automatic_file:
#     automatic_file.write("This file is automatically created by python")

# opening a file in another directory
# put r before the path so it converts the normal string to a raw string
# with open(r"C:\Users\saksh\Downloads\test_downloads_file.txt") as file:
#     content = file.read()
#     print(content)

# IN PYTHON FORWARD AND BACK SLASH DOESN'T MATTER


# Relative path
# with open("../../../Downloads/test_downloads_file.txt") as file:
#     content = file.read()
#     print(content)