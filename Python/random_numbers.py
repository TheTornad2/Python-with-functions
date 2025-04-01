import random 

def main():
    
    # The random numbers ----------------------------
    
    numbers = [16.2, 75.1, 52.3]
    
    print(f"Initial list: {numbers}")
    
    # Append one random number to the list
    append_random_numbers(numbers)
    print(f"After adding one number: {numbers}")
    print("-" * 70)  
    
    # Append three random numbers to the list
    append_random_numbers(numbers, 3)
    print(f"After adding three numbers: {numbers}")
    print("-" * 70)  
    
    # Random words ---------------------------------
    
    words = ["dog", "cat", "elephant "]
    
    print(f"Initial list of words: {words}")
    
    # Append one random word to the list
    append_random_words(words)
    print(f"After adding one random word: {words}")
    print("-" * 70)  
    
    # Append three random words to the list
    append_random_words(words, 3)
    print(f"After adding three random words: {words}")
    print("-" * 70)   
    
    # Shuffle the list of words
    random.shuffle(words)
    print(f"After shuffling the list: {words}")


# Function to append random numbers to the list
def append_random_numbers(number_list, quantity=1):  
    for i in range(quantity):
        random_number = round(random.uniform(0, 10), 1)  # Generate a random float between 0 and 10
        number_list.append(random_number)


# Function to append random words to the list
def append_random_words(words_list, quantity=1):
    word_pool = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Kiwi", "Lemon"]
    for i in range(quantity):
        random_word = random.choice(word_pool)  # Randomly select a word from the pool
        words_list.append(random_word)


if __name__ == "__main__":
    main()
