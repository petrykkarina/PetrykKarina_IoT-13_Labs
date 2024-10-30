def count_numbers_without_five(start, end):
    count = 0
    for num in range(start, end + 1):
        if '5' not in str(num):  
            count += 1
    return count

start_range = 0
end_range = 99
result = count_numbers_without_five(start_range, end_range)
print(f"Кількість чисел без '5' в діапазоні від {start_range} до {end_range}: {result}")

