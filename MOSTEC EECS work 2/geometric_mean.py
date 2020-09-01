def geometric_mean(numbers):
    product = 1
    if len(numbers) >= 1:
        for number in numbers:
            product = product * number
        return product **(1/len(numbers))
    else:
        return None
            
