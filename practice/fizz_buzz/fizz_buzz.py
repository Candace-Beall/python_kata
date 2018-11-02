def fizz_buzz(upper_bound):
    numbers = []

    for number in range(1, upper_bound + 1):
        if number % 3 == 0 and number % 5 == 0:
            numbers.append('fizzbuzz')
        elif number % 3 == 0:
            numbers.append('fizz')
        elif number % 5 == 0:
            numbers.append('buzz')
        else:
            numbers.append(number)

    return numbers
