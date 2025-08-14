def clean_text(text):
    # Define a simple set of English stop words
    stop_words = set([
        'the', 'and', 'is', 'in', 'to', 'of', 'a', 'an', 'on', 'for', 'with', 'as', 'by', 'at', 'from', 'it', 'this', 'that', 'are', 'was', 'be', 'or', 'but', 'not', 'so', 'if', 'then', 'than', 'too', 'very', 'can', 'will', 'just', 'do', 'does', 'did', 'has', 'have', 'had', 'he', 'she', 'they', 'we', 'you', 'i', 'his', 'her', 'their', 'our', 'your', 'my', 'me', 'him', 'them', 'who', 'whom', 'which', 'what', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'only', 'own', 'same', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
    ])
    # Remove punctuation
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    # Convert to lowercase
    text = text.lower()
    # Remove stop words
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

# Example usage:
if __name__ == "__main__":
    input_text = input("Enter text: ")
    cleaned = clean_text(input_text)
    print("Cleaned text:", cleaned)




