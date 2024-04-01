from collections import Counter

def calculate_metrics(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    sum_nums = sum(numbers)
    average = sum_nums / len(numbers)
    mode = Counter(numbers).most_common(1)[0][0]
    return min_num, max_num, sum_nums, average, mode

def print_metrics(min_num, max_num, sum_nums, average, mode):
    print(f"min, max, sum, average and mode after addition: {min_num}, {max_num}, {sum_nums}, {average}, {mode}")

# Example input
N = int(input())
numbers_stream = list(map(int, input().split()))

# Initialize an empty list to store numbers
numbers_list = []

# Process the stream of numbers
for num in numbers_stream:
    numbers_list.append(num)
    min_num, max_num, sum_nums, average, mode = calculate_metrics(numbers_list)
    print_metrics(min_num, max_num, sum_nums, average, mode)