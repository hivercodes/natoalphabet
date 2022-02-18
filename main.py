import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

user_input = input("What do you want natoized?:")

user_input_list = [n.upper() for n in user_input]

exit_list = [row.code for (index, row) in data.iterrows() if row.letter in user_input_list]


print(exit_list)
