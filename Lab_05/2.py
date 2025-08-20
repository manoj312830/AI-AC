def analyze_sentiment():
    positive_words = {"awesome", "excellent", "good", "great", "fantastic", "amazing", "happy", "love", "wonderful", "best"}
    negative_words = {"bad", "terrible", "awful", "worst", "sad", "hate", "horrible", "poor", "disappointing", "boring"}

    text = input("Enter a sentence: ").lower()
    words = set(text.split())

    pos_count = len(words & positive_words)
    neg_count = len(words & negative_words)

    if pos_count > neg_count:
        sentiment = "positive"
    elif neg_count > pos_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    analyze_sentiment()