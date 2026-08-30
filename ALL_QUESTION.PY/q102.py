
# Q99. Vowel-Starting Words

# Take a sentence as input. Split it into words and print how many words start
# with a vowel.
def count_vowel(sen: str):
    vowels = "aeiouAEIOU"
    count = 0

    for i in sen.split():
        if i[0] in vowels:
            count += 1

    return count


sentence = "Anirudh is an excellent coder and a great engineer"
print(count_vowel(sentence))