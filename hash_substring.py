
def rabin_karp(pattern, text):

    p = len(pattern)
    t = len(text)
    result = []


    pattern_hash = sum([ord(pattern[i]) for i in range(p)])
    text_hash = sum([ord(text[i]) for i in range(p)])
    

    for i in range(t - p + 1):

        if pattern_hash == text_hash:
            if pattern == text[i:i+p]:
                result.append(i)

        if i < t - p:
            text_hash = text_hash - ord(text[i]) + ord(text[i+p])
    

    return result

pattern = input().strip()
text = input().strip()


result = rabin_karp(pattern, text)
print(*result)
