# extract the data from csv and create a dictionary out of it
import pandas
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_mapping = {row.letter: row.code for (index, row) in data_frame.iterrows()}

# get the input from user and turn the name to upper case because the letters in the dictionary are all upper cases
# user_input = input("Enter your name: ").upper()
user_name_codes = None

# # use exception handling until the user passes in valid data
# while user_name_codes == None:
#       try:
#             # loop through each of the letter in the name and return a list of corresponding codes
#             user_name_codes = [letter_mapping[letter] for letter in user_input]
#       except KeyError:
#             print("You entered an invalid text, only letters in the alphabet please.")
#             user_input = input("Enter your name: ").upper()
#       else:
#             print(f"Please use this list when you need help differentiating and pronouncing"
#             f" letters in your name, {user_input.title()}:\n{user_name_codes}")

# Another method
def generate_alphabets():
      user_input = input("Enter your name: ").upper()
      try:
            # loop through each of the letter in the name and return a list of corresponding codes
            user_name_codes = [letter_mapping[letter] for letter in user_input]
      except KeyError:
            print("You entered an invalid text, only letters in the alphabet please.")
            # recursively call the function again
            generate_alphabets()
      else:
            print(f"Please use this list when you need help differentiating and pronouncing"
                  f" letters in your name, {user_input.title()}:\n{user_name_codes}")

generate_alphabets()