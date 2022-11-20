import pandas

alphabets = pandas.read_csv('nato_phonetic_alphabet.csv', index_col = 0, squeeze= True).to_dict()

word = input("Enter a Name: ").upper()
letters_in_word = [alphabets[letter] for letter in word]
print(letters_in_word)
