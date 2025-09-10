
def process_scores(scores):
    if len(scores) == 0:
        print("No scores provided.")
        return

    total = 0
    for s in scores:
        total += s
    avg = total / len(scores)

    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s

    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

# Example usage
sample_scores = [85, 92, 78, 90, 88]
process_scores(sample_scores)
