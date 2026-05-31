# Requirements:

# User se text file ka path lo — ya directly text input lo
# Text ko words mein tod do
# Har word ki frequency count karo dictionary mein
# Top 10 most common words dikhao
# Specific word search kar sako — kitni baar aaya
# All unique words count dikhao
# Punctuation aur case ignore karo — "Hello" aur "hello" ek hi word hai
# Common words exclude karo — "the", "a", "an", "is", "are", "was" wagera
# Results sort karke dikhao — most frequent pehle
# Output ek clean formatted table mein

# Sample text file banao — sample.txt
# Punctuation remove karna:
import string
#converting text to words from sample.txt
with open("sample.txt", "r") as file:    #opened the file and stored everything in text variable
    text = file.read()
words = text.split()  #split() se text ko words mein tod diya
words = [word.strip(string.punctuation) for word in words]  #removed punctuation from each word using strip() and string.punctuation

# Case normalize:
words = [word.lower() for word in words]#lowercase main convert kiya


# Common words — stop words:
stop_words = {"the", "a", "an", "is", "are", "was", 
              "and", "or", "but", "in", "on", "at", 
              "to", "for", "of", "with", "it", "this"}



# Frequency count karna — dict se:
frequency = {}
for word in words: # for each word
    frequency[word] = frequency.get(word, 0) + 1 #agar word pehle se frequency mein hai to uski value 1 badha do, nahi to usko 0 se start karo
print(frequency)

# Sort by frequency:
def sorted_frequency(frequency):
    
    return sorted(frequency.items(), 
                  key=lambda x: x[1], 
                  reverse=True)

sorted_words = sorted_frequency(frequency)

def top_10_words(sorted_words):
    return sorted_words[:10]

def search_word():
    word = input("Enter a word to search: ").lower()
    if word in stop_words:
        print(f"'{word}' is a common word and is excluded from the count.")
    elif word in frequency:
        print(f"'{word}' appears {frequency[word]} times.")
    else:
        print(f"'{word}' does not appear in the text.")
    return frequency.get(word, 0)
def unique_words_count():
    unique_words = set(frequency.keys()) - stop_words
    print(f"Total unique words (excluding common words): {len(unique_words)}")

# Display results in a clean formatted table:
def display_table(sorted_words):
    print(f"{'Word':<15} {'Frequency':<10}")
    for word, count in sorted_words:
        if word not in stop_words:
            print(f"{word:<15} {count:<10}")

# Main function to run the program:
def main():
    #menu
    while True:
        print("\nMenu:")
        print("1. Display top 10 most common words")
        print("2. Search for a specific word")
        print("3. Count unique words")
        print("4. Display all words and frequencies")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            top_words = top_10_words(sorted_words)
            display_table(top_words)
        elif choice == '2':
            search_word()
        elif choice == '3':
            unique_words_count()
        elif choice == '4':
            display_table(sorted_words)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()           