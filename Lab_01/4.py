def word_frequency(text):
    freq = {}
    words = text.split()
    for word in words:
        word = word.lower().strip('.,!?;:"()[]{}')
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq

# Example usage:
if __name__ == "__main__":
    sample_text = "Hello world! Hello AI. AI is the future."
    print(word_frequency(sample_text))