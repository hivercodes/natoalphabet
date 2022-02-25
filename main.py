import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")



phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("What do you want natoized?:").upper()

try:
    output_list = [phonetic_dict[letter] for letter in user_input]
except KeyError:
    print("Only letters in the alphabet is allowed")
else:
    print(output_list)