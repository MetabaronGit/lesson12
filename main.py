lst = [1, 2, 3, 4.04, "a", "b"]
lst = []

def avg(lst):
    numbers = []
    for item in lst:
        try:
            number = float(item)
            if int(number) == number:
                number = int(number)
            numbers.append(item)
        except ValueError:
            continue


        print(number)
    return sum(numbers) / len(numbers)


print("průměr čísel v listu:", avg(lst))


