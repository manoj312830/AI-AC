def process_scores(scores):
    if not scores:
        print("No scores provided.")
        return

    avg = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

# ✅ Call the function with sample data
process_scores([85, 92, 78, 90, 88])