"""
Converts_numbers
"""

import sys
import time

def read_numbers_from_file(filename):
    """Reads a list of numbers from a file"""
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Warning: Invalid data ignored -> {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return numbers

def to_binary(n):
    """Converts a number to binary"""
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def to_hexadecimal(n):
    """Converts a number to hexadecimal"""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return hexadecimal

def main():
    """Main function to execute the number conversions."""
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py <fileWithData.txt>")
        sys.exit(1)
    filename = sys.argv[1]
    start_time = time.time()
    numbers = read_numbers_from_file(filename)
    if not numbers:
        print("Error: No valid numbers found in file.")
        sys.exit(1)
    results = ""
    for num in numbers:
        binary = to_binary(num)
        hexadecimal = to_hexadecimal(num)
        results += f"Number: {num}, Binary: {binary}, Hexadecimal: {hexadecimal}\n"
    execution_time = time.time() - start_time
    results += f"Execution Time: {execution_time:.6f} seconds\n"
    print(results)
    try:
        with open("ConversionResults3.txt", "w", encoding='utf-8') as result_file:
            result_file.write(results)
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
