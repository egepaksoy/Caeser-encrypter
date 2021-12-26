letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
word = "$CHANGE HERE$"
repeat = $CHANGE HERE$
hashed_word = ""


for i in word:
    if i in letters:
        letter_count = letters.index(i) + repeat


        hashed_word+=(letters[letter_count])


    elif i in upper_letters:
        letter_count = upper_letters.index(i) + repeat


        hashed_word+=(upper_letters[letter_count])


    else:
        hashed_word+=i

print(hashed_word)

