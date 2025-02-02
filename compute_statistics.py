""" Compute statistics"""
import sys
import time

def read_numbers_from_file(filename):
    """Reads a list of numbers from a file"""
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Warning: Invalid data ignored -> {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return numbers

def compute_mean(numbers):
    """Calculate the mean"""
    return sum(numbers) / len(numbers)

def compute_median(numbers):
    """Calculate the median"""
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid - 1] + numbers[mid]) / 2 if n % 2 == 0 else numbers[mid]

def compute_mode(numbers):
    """Calculate the mode"""
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_count = max(frequency.values())
    return [num for num, count in frequency.items() if count == max_count]

def compute_variance(numbers, mean):
    """Calculate the variance"""
    return sum((num - mean) ** 2 for num in numbers) / len(numbers)

def compute_standard_deviation(variance):
    """Calculte the standard deviation"""
    return variance ** 0.5

def main():
    """Main function to execute the statistical calculations"""
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py <fileWithData.txt>")
        sys.exit(1)
    filename = sys.argv[1]
    start_time = time.time()
    numbers = read_numbers_from_file(filename)
    if not numbers:
        print("Error: No valid numbers found in file.")
        sys.exit(1)
    mean = compute_mean(numbers)
    median = compute_median(numbers)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    standard_deviation = compute_standard_deviation(variance)
    execution_time = time.time() - start_time
    results = (
        f"Mean: {mean}\n"
        f"Median: {median}\n"
        f"Mode: {mode}\n"
        f"Variance: {variance}\n"
        f"Standard Deviation: {standard_deviation}\n"
        f"Execution Time: {execution_time:.6f} seconds\n"
    )
    print(results)
    try:
        with open("StatisticsResults6.txt", "w", encoding='utf-8') as result_file:
            result_file.write(results)
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
