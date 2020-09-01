def arithmetic_mean(numbers):
    total = 0
    if len(numbers) >= 1:
        for number in numbers:
            total += number
        return total / len(numbers)
    else:
        return None
