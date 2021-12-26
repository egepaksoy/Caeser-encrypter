letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
hashed_word = "$CHANGE HERE$"
repeat = $CHANGE HERE$
decoded_word = ""


for i in hashed_word:
    if i in letters:
        letter_count = letters.index(i) + repeat


        decoded_word+=(letters[letter_count])


    elif i in upper_letters:
        letter_count = upper_letters.index(i) + repeat


        decoded_word+=(upper_letters[letter_count])


    else:
        decoded_word += i


print(decoded_word)
