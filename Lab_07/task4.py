

# Refactored compute_ratios to handle ZeroDivisionError using try-except

def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            try:
                denominator = values[j] - values[i]
                ratio = values[i] / denominator
                results.append((i, j, ratio))
            except ZeroDivisionError:
                # Skip this pair if denominator is zero
                continue
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))
