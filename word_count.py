"""
Count Word
"""

import sys
import time

def read_words_from_file(filename):
    """Reads words from a file"""
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words.extend(line.strip().split())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return words

def count_word_frequencies(words):
    """Counts the frequency of each word"""
    word_frequencies = []
    unique_words = []
    for word in words:
        word = word.lower()
        found = False
        for i, unique_word in enumerate(unique_words):  # Use enumerate here
            if unique_word == word:
                word_frequencies[i] += 1
                found = True
                break
        if not found:
            unique_words.append(word)
            word_frequencies.append(1)
    return unique_words, word_frequencies

def main():
    """Main function to execute the word count"""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <fileWithData.txt>")
        sys.exit(1)
    filename = sys.argv[1]
    start_time = time.time()
    words = read_words_from_file(filename)
    if not words:
        print("Error: No valid words found in file.")
        sys.exit(1)
    unique_words, word_frequencies = count_word_frequencies(words)
    results = ""
    for i, unique_word in enumerate(unique_words):  # Use enumerate here as well
        results += f"Word: {unique_word}, Frequency: {word_frequencies[i]}\n"
    execution_time = time.time() - start_time
    results += f"Execution Time: {execution_time:.6f} seconds\n"
    print(results)
    try:
        with open("WordCountResults4.txt", "w", encoding='utf-8') as result_file:
            result_file.write(results)
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
