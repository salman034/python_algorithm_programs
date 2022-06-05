def prime_num(lower, upper):

    for number in range(lower, upper + 1):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print(number)


if __name__ == "__main__":
    list = prime_num(0, 1000)
    print(list)