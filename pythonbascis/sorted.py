def is_sorted(numbers):
    for number in numbers:
        if numbers==sorted(numbers):
            return True
        else:
            return False
