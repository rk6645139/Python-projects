#function to count words in a string

def count_words(string):
    words =string.split()
    return len(words)

#take input from the user
input_string=input("Enter a string")
word_count = count_words(input_string)

print(f"the number of words in a a string is:{word_count}")