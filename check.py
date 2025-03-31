from collections import Counter

def compare_files(file1, file2):
    # Read and split words from both files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        words1 = f1.read().split()
        words2 = f2.read().split()

    # Count word occurrences
    counter1 = Counter(words1)
    counter2 = Counter(words2)

    # Calculate missing words
    missing_words = sum((counter1 - counter2).values())
    total_words = sum(counter1.values())

    # Calculate percentage of loss
    loss_percentage = (missing_words / total_words) * 100 if total_words > 0 else 0

    return missing_words, loss_percentage

# Example usage
file1 = 'o.txt'  # Replace with your file path
file2 = 'p.txt'  # Replace with your file path

missing, percentage_loss = compare_files(file1, file2)
print(f"Missing words: {missing}")
print(f"Percentage of loss: {percentage_loss:.2f}%")

file2 = 'p2.txt'  # Replace with your file path

missing, percentage_loss = compare_files(file1, file2)
print(f"Missing words: {missing}")
print(f"Percentage of loss: {percentage_loss:.2f}%")
file2 = 'p3.txt'  # Replace with your file path

missing, percentage_loss = compare_files(file1, file2)
print(f"Missing words: {missing}")
print(f"Percentage of loss: {percentage_loss:.2f}%")
file2 = 'p4.txt'  # Replace with your file path

missing, percentage_loss = compare_files(file1, file2)
print(f"Missing words: {missing}")
print(f"Percentage of loss: {percentage_loss:.2f}%")
file2 = 'p4.txt'  # Replace with your file path

missing, percentage_loss = compare_files(file1, file2)
print(f"Missing words: {missing}")
print(f"Percentage of loss: {percentage_loss:.2f}%")