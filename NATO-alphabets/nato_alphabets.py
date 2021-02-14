# extract the data from csv and create a dictionary out of it
import pandas
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_mapping = {row.letter: row.code for (index, row) in data_frame.iterrows()}
# get the input from user and turn the name to upper case because the letters in the dictionary are all upper cases
user_input = input("Enter your name: ").upper()
# loop through each of the letter in the name and return a list of corresponding codes
user_name_codes = [letter_mapping[letter] for letter in user_input]
print(f"Please use this list when you need help differentiating and pronouncing"
      f" letters in your name, {user_input.title()}:\n{user_name_codes}")