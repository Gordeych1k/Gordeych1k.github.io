words = ["  hello  ", " world", "python  ", "  code "]

cleaned_words = list(map(str.strip, words))

print(cleaned_words)