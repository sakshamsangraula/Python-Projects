# # Understand and test what happens with different exceptions
# # I specifically focus on the FileNotFoundError and also KeyError Exception
#
# # try to run this in a try block because we are not sure if this will work
# try:
#     # try opening a file that doesn't exist using read
#     file = open("new_file.txt")
#     dict = {"key": "value"}
#     print(dict["key"])
# # catch the exception if it happens in the except block (try to provide an exception name after the except block)
# except FileNotFoundError:
#     # create the file
#     print("creating the file")
#     file = open("new_file.txt", mode="w")
#     file.write("File created")
#
# except KeyError as error_reason:
#     print(f"Key error, {error_reason} key doesn't exist")
# # run the code in else section if there are no exception
# else:
#     # if the file is now created, read the contents
#     content = file.read()
#     print(content)
#
# # do anything no matter it fails or not in the finally block (like closing a file)
# # finally is not often used
# finally:
#     file.close()
#     raise KeyError("this is an exception that i made up")


# Summary:

# try:  put code here to try if the code runs - TRY TO RUN THE CODE
# except: catch exception in the except block - CATCH EXCEPTIONS
# else: run the code if there are no exceptions - NO EXCEPTIONS
# finally: run the code no matter what happens - RUN NO MATTER WHAT

# raise an exception if the height is more than 3 meters
height = float(input("What is your height? "))
weight = int(input("What is your weight? "))

if height > 3:
    raise ValueError("Human height cannot be more than 3 meters")
else:
    bmi = weight / pow(height, 2)
    print(bmi)