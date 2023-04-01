# python3

# Define a function to search for a pattern in a given text using Rabin-Karp's algorithm
def rabin_karp(pattern, text):
    # Initialize variables
    p = len(pattern)
    t = len(text)
    result = []

    # Calculate the hash value of the pattern and the first substring of the same length in the text
    pattern_hash = sum([ord(pattern[i]) for i in range(p)])
    text_hash = sum([ord(text[i]) for i in range(p)])
    
    # Loop through each substring of the text of length p
    for i in range(t - p + 1):
        # If the hash values match, check if the substrings match
        if pattern_hash == text_hash:
            if pattern == text[i:i+p]:
                result.append(i)
        # Calculate the hash value of the next substring of length p in the text
        if i < t - p:
            text_hash = text_hash - ord(text[i]) + ord(text[i+p])
    
    # Return the result
    return result

# Read in the pattern and text from input
pattern = input().strip()
text = input().strip()

# Call the rabin_karp function and print the result
result = rabin_karp(pattern, text)
print(*result)
