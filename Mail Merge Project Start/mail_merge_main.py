# TODO: Create a letter using starting_letter.txt
PLACE_HOLDER = "[name]"
with open(r"C:/app-brewery-python-self-learning/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("C:/app-brewery-python-self-learning/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:

    # read each line of the file
    for line in name_file:
        # read each word and replace [name] with the actual name everytime
        for name in line.split():
            new_letter = letter.replace(PLACE_HOLDER, name)

            # write the letter each time to a new file
            with open(f"C:/app-brewery-python-self-learning/Mail Merge Project Start/Output/ReadyToSend/letter_for"
                      f"{name}.txt",
                      mode="w") as single_letter:
                single_letter.write(new_letter)




# replace name with the actual name
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp