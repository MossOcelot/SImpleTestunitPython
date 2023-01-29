def is_prime_list(numbers):
    for num in numbers:
        for n in range(2, num):
            if num % n == 0:
                return False
    return True


if __name__ == "__main__":
    number = [int(i) for i in input("number list").split()]

    result = is_prime_list(number)
    print(result)
