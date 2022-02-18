import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

user_input = input("What do you want natoized?:")

user_input_list = [n.upper() for n in user_input]

exit_dict = {row.letter:row.code for (index, row) in data.iterrows()}

exit_list = [code for (letter, code) in exit_dict.items() for l in user_input_list if letter == l]

print(exit_list)
