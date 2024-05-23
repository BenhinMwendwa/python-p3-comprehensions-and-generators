#!/usr/bin/env python3

def return_evens(num_list):
    value = [n for n in num_list if n % 2 == 0]
    return value

print(return_evens([0, 1, 3, 5, 7, 8, 9]))

def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]

# Example usage
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
